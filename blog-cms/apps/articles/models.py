"""
Article model — central model of the Blog CMS
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from apps.categories.models import Category
from apps.tags_app.models import Tag
from apps.authors.models import Author
from apps.media_library.models import MediaFile
from apps.utils import slugify, unique_slug


class Article(models.Model):
    STATUS_DRAFT = 'draft'
    STATUS_SCHEDULED = 'scheduled'
    STATUS_PUBLISHED = 'published'
    STATUS_UNPUBLISHED = 'unpublished'
    STATUS_TRASH = 'trash'

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_SCHEDULED, 'Scheduled'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_UNPUBLISHED, 'Unpublished'),
        (STATUS_TRASH, 'Trash'),
    ]

    # Core fields
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=320, unique=True, blank=True)
    excerpt = models.TextField(max_length=500, blank=True, help_text='Short summary shown on listing page')
    content = models.TextField(help_text='Rich HTML content of the article')
    featured_image = models.ForeignKey(
        MediaFile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='featured_articles'
    )
    featured_image_alt = models.CharField(max_length=255, blank=True)

    # Relationships
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='articles')
    categories = models.ManyToManyField(Category, blank=True, related_name='articles')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')

    # Status & dates
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT, db_index=True)
    published_at = models.DateTimeField(null=True, blank=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='created_articles')

    # SEO fields
    seo_title = models.CharField(max_length=70, blank=True, help_text='Overrides title in <title> tag (max 70 chars)')
    seo_description = models.CharField(max_length=160, blank=True, help_text='Meta description (max 160 chars)')
    canonical_url = models.URLField(blank=True, help_text='Leave blank to auto-generate from slug')
    og_image = models.ForeignKey(
        MediaFile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='og_articles'
    )

    # Soft delete
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(Article, self.title, exclude_pk=self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def public_url(self):
        return f'/blog/{self.slug}'

    @property
    def html_filename(self):
        return f'congo-prime-{self.slug}.html'

    @property
    def effective_seo_title(self):
        return self.seo_title or f'{self.title} | Congo Prime Construction'

    @property
    def effective_canonical(self):
        return self.canonical_url or f'https://congoprime.com/blog/{self.slug}'

    def soft_delete(self):
        self.status = self.STATUS_TRASH
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.status = self.STATUS_DRAFT
        self.deleted_at = None
        self.save()

