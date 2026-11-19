"""
Imported HTML record
"""
from django.db import models
from django.contrib.auth.models import User
from apps.articles.models import Article


class ImportedHTML(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='html_imports')
    original_filename = models.CharField(max_length=255, blank=True)
    original_html = models.TextField()
    imported_at = models.DateTimeField(auto_now_add=True)
    imported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='html_imports')

    class Meta:
        ordering = ['-imported_at']

    def __str__(self):
        return f'Import: {self.original_filename} → {self.article}'

