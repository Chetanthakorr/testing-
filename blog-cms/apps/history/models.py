"""
Article Revision model — version history
"""
from django.db import models
from django.contrib.auth.models import User
from apps.articles.models import Article


class ArticleRevision(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='revisions')
    title = models.CharField(max_length=300)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    seo_title = models.CharField(max_length=70, blank=True)
    seo_description = models.CharField(max_length=160, blank=True)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='revisions')
    changed_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-changed_at']

    def __str__(self):
        return f'Revision of "{self.article.title}" at {self.changed_at:%Y-%m-%d %H:%M}'


class PublishingEvent(models.Model):
    ACTION_PUBLISH = 'publish'
    ACTION_UNPUBLISH = 'unpublish'
    ACTION_SCHEDULE = 'schedule'
    ACTION_DELETE = 'delete'
    ACTION_RESTORE = 'restore'
    ACTION_UPDATE = 'update'

    ACTION_CHOICES = [
        (ACTION_PUBLISH, 'Published'),
        (ACTION_UNPUBLISH, 'Unpublished'),
        (ACTION_SCHEDULE, 'Scheduled'),
        (ACTION_DELETE, 'Deleted'),
        (ACTION_RESTORE, 'Restored'),
        (ACTION_UPDATE, 'Updated'),
    ]

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='publishing_events')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='publishing_events')
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)
    error_message = models.TextField(blank=True)
    detail = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.action} "{self.article.title}" by {self.performed_by} at {self.timestamp:%Y-%m-%d %H:%M}'

