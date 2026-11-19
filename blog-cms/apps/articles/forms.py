"""
Articles forms
"""
from django import forms
from .models import Article
from apps.categories.models import Category
from apps.tags_app.models import Tag
from apps.authors.models import Author
from apps.media_library.models import MediaFile


class ArticleForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Article
        fields = [
            'title', 'slug', 'excerpt', 'content',
            'featured_image', 'featured_image_alt',
            'author', 'categories', 'tags',
            'seo_title', 'seo_description', 'canonical_url', 'og_image',
            'published_at', 'scheduled_at',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Article title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'url-slug'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Short summary (shown on listing page)'}),
            'content': forms.Textarea(attrs={'id': 'article-content-editor', 'class': 'form-control content-editor', 'rows': 20}),
            'featured_image_alt': forms.TextInput(attrs={'class': 'form-control'}),
            'seo_title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 70}),
            'seo_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'maxlength': 160}),
            'canonical_url': forms.URLInput(attrs={'class': 'form-control'}),
            'published_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'scheduled_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

