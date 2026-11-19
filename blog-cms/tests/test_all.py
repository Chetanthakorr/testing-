"""
Congo Prime Blog CMS — Comprehensive Tests
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'congoprime_cms.settings.development')
django.setup()

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone

from apps.categories.models import Category
from apps.tags_app.models import Tag
from apps.authors.models import Author
from apps.articles.models import Article
from apps.media_library.models import MediaFile
from apps.history.models import ArticleRevision, PublishingEvent
from apps.utils import slugify, unique_slug
from apps.publishing.engine import validate_article, render_article_html


# ─── UNIT TESTS: Utilities ───────────────────────────────────────
class SlugifyTest(TestCase):
    def test_basic(self):
        self.assertEqual(slugify('Hello World'), 'hello-world')

    def test_special_chars(self):
        self.assertEqual(slugify('Construction & Infrastructure!'), 'construction-infrastructure')

    def test_dashes_preserved(self):
        self.assertEqual(slugify('Haut-Katanga DRC'), 'haut-katanga-drc')

    def test_unicode_stripped(self):
        result = slugify('Développement')
        self.assertIn('d', result)

    def test_empty(self):
        self.assertEqual(slugify(''), '')


# ─── UNIT TESTS: Models ──────────────────────────────────────────
class CategoryModelTest(TestCase):
    def test_create_category(self):
        cat = Category.objects.create(name='Construction')
        self.assertEqual(cat.slug, 'construction')

    def test_unique_slug_auto(self):
        """Category slug must be unique — duplicate name should raise an error or use get_or_create."""
        Category.objects.create(name='Infrastructure')
        # Slug uniqueness is enforced at DB level; use get_or_create for duplicates
        cat2, created = Category.objects.get_or_create(name='Infrastructure')
        self.assertFalse(created)  # second creation returns existing
        self.assertEqual(cat2.slug, 'infrastructure')


class TagModelTest(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name='Lubumbashi')
        self.assertEqual(tag.slug, 'lubumbashi')


class AuthorModelTest(TestCase):
    def test_create_author(self):
        author = Author.objects.create(name='Congo Prime Editorial')
        self.assertEqual(str(author), 'Congo Prime Editorial')


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('editor', password='pass123')
        self.author = Author.objects.create(name='Test Author')

    def test_create_draft(self):
        article = Article.objects.create(
            title='Test Article',
            content='<p>Content here.</p>',
            created_by=self.user,
        )
        self.assertEqual(article.status, 'draft')
        self.assertIn('test-article', article.slug)

    def test_slug_auto_generated(self):
        article = Article.objects.create(title='My New Article', content='<p>x</p>')
        self.assertEqual(article.slug, 'my-new-article')

    def test_html_filename(self):
        article = Article.objects.create(title='Kolwezi Housing', content='<p>x</p>')
        self.assertEqual(article.html_filename, f'congo-prime-{article.slug}.html')

    def test_public_url(self):
        article = Article.objects.create(title='Kolwezi Housing', content='<p>x</p>')
        self.assertEqual(article.public_url, f'/blog/{article.slug}')

    def test_soft_delete(self):
        article = Article.objects.create(title='Delete Me', content='<p>x</p>')
        article.soft_delete()
        self.assertEqual(article.status, 'trash')
        self.assertIsNotNone(article.deleted_at)

    def test_restore(self):
        article = Article.objects.create(title='Restore Me', content='<p>x</p>', status='trash')
        article.restore()
        self.assertEqual(article.status, 'draft')
        self.assertIsNone(article.deleted_at)

    def test_effective_seo_title(self):
        article = Article.objects.create(title='My Article', content='<p>x</p>')
        self.assertIn('My Article', article.effective_seo_title)
        article.seo_title = 'Custom SEO'
        article.save()
        self.assertEqual(article.effective_seo_title, 'Custom SEO')

    def test_categories_m2m(self):
        article = Article.objects.create(title='Cat Test', content='<p>x</p>')
        cat = Category.objects.create(name='Residential')
        article.categories.add(cat)
        self.assertIn(cat, article.categories.all())

    def test_tags_m2m(self):
        article = Article.objects.create(title='Tag Test', content='<p>x</p>')
        tag = Tag.objects.create(name='Haut-Katanga')
        article.tags.add(tag)
        self.assertIn(tag, article.tags.all())


# ─── UNIT TESTS: Publishing Engine ───────────────────────────────
class PublishingEngineTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('pub_editor', password='pub123')
        self.author = Author.objects.create(name='Engine Tester')

    def test_validate_missing_title(self):
        article = Article(title='', slug='some-slug', content='<p>x</p>')
        errors = validate_article(article)
        self.assertIn('Title is required.', errors)

    def test_validate_missing_content(self):
        article = Article(title='Test', slug='test', content='')
        errors = validate_article(article)
        self.assertIn('Content is required.', errors)

    def test_validate_valid_article(self):
        article = Article(title='Valid Article', slug='valid-article', content='<p>Some content here.</p>')
        errors = validate_article(article)
        self.assertEqual(errors, [])

    def test_render_article_html_contains_title(self):
        article = Article.objects.create(
            title='Lubumbashi Construction',
            slug='lubumbashi-construction',
            content='<p>Test content.</p>',
            status='draft',
        )
        html = render_article_html(article)
        self.assertIn('Lubumbashi Construction', html)
        self.assertIn('<!DOCTYPE html>', html)
        self.assertIn('congoprime.com', html)
        self.assertIn('schema.org', html)

    def test_render_contains_breadcrumb_schema(self):
        article = Article.objects.create(
            title='Schema Test',
            slug='schema-test',
            content='<p>Content.</p>',
        )
        html = render_article_html(article)
        self.assertIn('BreadcrumbList', html)

    def test_render_contains_blogposting_schema(self):
        article = Article.objects.create(
            title='Blog Schema',
            slug='blog-schema',
            content='<p>Content.</p>',
        )
        html = render_article_html(article)
        self.assertIn('BlogPosting', html)


# ─── INTEGRATION TESTS: Authentication ───────────────────────────
class AuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('blogtest', password='secure123')

    def test_login_page_loads(self):
        resp = self.client.get('/cms/login/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Sign In')

    def test_login_valid(self):
        resp = self.client.post('/cms/login/', {'username': 'blogtest', 'password': 'secure123'}, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_login_invalid(self):
        resp = self.client.post('/cms/login/', {'username': 'blogtest', 'password': 'wrong'})
        self.assertContains(resp, 'Invalid')

    def test_dashboard_requires_login(self):
        resp = self.client.get('/cms/dashboard/')
        self.assertEqual(resp.status_code, 302)
        self.assertIn('login', resp['Location'])

    def test_dashboard_accessible_when_logged_in(self):
        self.client.login(username='blogtest', password='secure123')
        resp = self.client.get('/cms/dashboard/')
        self.assertEqual(resp.status_code, 200)

    def test_logout(self):
        self.client.login(username='blogtest', password='secure123')
        resp = self.client.post('/cms/logout/')
        self.assertEqual(resp.status_code, 302)


# ─── INTEGRATION TESTS: Articles CRUD ────────────────────────────
class ArticleCRUDTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('crud_editor', password='crud123')
        self.client.login(username='crud_editor', password='crud123')

    def test_article_list(self):
        resp = self.client.get('/cms/articles/')
        self.assertEqual(resp.status_code, 200)

    def test_article_create_page(self):
        resp = self.client.get('/cms/articles/create/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'New Article')

    def test_article_create_post(self):
        resp = self.client.post('/cms/articles/create/', {
            'title': 'Integration Test Article',
            'slug': '',
            'excerpt': 'Test excerpt',
            'content': '<p>Test body content</p>',
            'seo_title': '',
            'seo_description': '',
            'canonical_url': '',
            'featured_image_alt': '',
            'action': 'save_draft',
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Article.objects.filter(title='Integration Test Article').exists())

    def test_article_edit_page(self):
        article = Article.objects.create(title='Edit Test', content='<p>x</p>', created_by=self.user)
        resp = self.client.get(f'/cms/articles/{article.pk}/edit/')
        self.assertEqual(resp.status_code, 200)

    def test_article_trash(self):
        article = Article.objects.create(title='Trash Test', content='<p>x</p>')
        resp = self.client.post(f'/cms/articles/{article.pk}/delete/', follow=True)
        self.assertEqual(resp.status_code, 200)
        article.refresh_from_db()
        self.assertEqual(article.status, 'trash')

    def test_article_restore(self):
        article = Article.objects.create(title='Restore Test', content='<p>x</p>', status='trash', deleted_at=timezone.now())
        resp = self.client.post(f'/cms/articles/{article.pk}/restore/', follow=True)
        self.assertEqual(resp.status_code, 200)
        article.refresh_from_db()
        self.assertEqual(article.status, 'draft')

    def test_trash_list(self):
        resp = self.client.get('/cms/articles/trash/')
        self.assertEqual(resp.status_code, 200)

    def test_slug_check_available(self):
        resp = self.client.get('/cms/articles/slug-check/?slug=unique-slug-xyz')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data['available'])

    def test_slug_check_taken(self):
        Article.objects.create(title='Existing', slug='existing-slug', content='<p>x</p>')
        resp = self.client.get('/cms/articles/slug-check/?slug=existing-slug')
        data = resp.json()
        self.assertFalse(data['available'])


# ─── INTEGRATION TESTS: Categories ───────────────────────────────
class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('cat_editor', password='cat123')
        self.client.login(username='cat_editor', password='cat123')

    def test_category_list(self):
        resp = self.client.get('/cms/categories/')
        self.assertEqual(resp.status_code, 200)

    def test_category_create(self):
        resp = self.client.post('/cms/categories/create/', {'name': 'Architecture'}, follow=True)
        self.assertTrue(Category.objects.filter(name='Architecture').exists())


# ─── INTEGRATION TESTS: Tags ─────────────────────────────────────
class TagViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('tag_editor', password='tag123')
        self.client.login(username='tag_editor', password='tag123')

    def test_tag_list(self):
        resp = self.client.get('/cms/tags/')
        self.assertEqual(resp.status_code, 200)

    def test_tag_create(self):
        resp = self.client.post('/cms/tags/create/', {'name': 'Kolwezi'}, follow=True)
        self.assertTrue(Tag.objects.filter(name='Kolwezi').exists())


# ─── INTEGRATION TESTS: Authors ──────────────────────────────────
class AuthorViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('auth_editor', password='auth123')
        self.client.login(username='auth_editor', password='auth123')

    def test_author_list(self):
        resp = self.client.get('/cms/authors/')
        self.assertEqual(resp.status_code, 200)

    def test_author_create(self):
        resp = self.client.post('/cms/authors/create/', {
            'name': 'Jane Doe', 'email': 'jane@example.com', 'bio': 'Editor'
        }, follow=True)
        self.assertTrue(Author.objects.filter(name='Jane Doe').exists())


# ─── INTEGRATION TESTS: Preview ──────────────────────────────────
class PreviewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('prev_editor', password='prev123')
        self.client.login(username='prev_editor', password='prev123')

    def test_preview_returns_html(self):
        article = Article.objects.create(
            title='Preview Article',
            slug='preview-article',
            content='<p>Preview body</p>',
        )
        resp = self.client.get(f'/cms/preview/{article.pk}/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Preview Article', resp.content)
        self.assertIn(b'<!DOCTYPE html>', resp.content)


# ─── INTEGRATION TESTS: Importer ─────────────────────────────────
class ImporterTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('imp_editor', password='imp123')
        self.client.login(username='imp_editor', password='imp123')

    def test_import_page_loads(self):
        resp = self.client.get('/cms/import/')
        self.assertEqual(resp.status_code, 200)

    def test_import_preview(self):
        sample_html = '''<!DOCTYPE html><html><head>
        <title>Test Import Article | Congo Prime</title>
        <meta name="description" content="Test description here.">
        <link rel="canonical" href="https://congoprime.com/blog/test-import">
        </head><body>
        <h1>Test Import Article</h1>
        <div class="blog-single"><div class="text"><p>Imported paragraph content.</p></div></div>
        </body></html>'''
        resp = self.client.post('/cms/import/', {
            'html_content': sample_html, 'action': 'preview'
        })
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test Import Article')


# ─── INTEGRATION TESTS: History ──────────────────────────────────
class HistoryTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('hist_editor', password='hist123')
        self.client.login(username='hist_editor', password='hist123')

    def test_publishing_log(self):
        resp = self.client.get('/cms/history/log/')
        self.assertEqual(resp.status_code, 200)

    def test_article_history(self):
        article = Article.objects.create(title='History Article', content='<p>x</p>')
        resp = self.client.get(f'/cms/history/article/{article.pk}/')
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    import unittest
    unittest.main()
