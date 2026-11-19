"""
Media Library model
"""
import os
from django.db import models
from django.contrib.auth.models import User


def media_upload_path(instance, filename):
    return f'blog/{filename}'


class MediaFile(models.Model):
    file = models.ImageField(upload_to=media_upload_path)
    filename = models.CharField(max_length=255, blank=True)
    alt_text = models.CharField(max_length=255, blank=True)
    caption = models.CharField(max_length=500, blank=True)
    file_size = models.PositiveIntegerField(default=0)
    mime_type = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uploads')

    class Meta:
        ordering = ['-uploaded_at']

    def save(self, *args, **kwargs):
        if self.file and not self.filename:
            self.filename = os.path.basename(self.file.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.filename or str(self.file)

    @property
    def url(self):
        return self.file.url if self.file else ''

    @property
    def site_image_path(self):
        """
        Relative path from Congo Prime site root (images/blog/filename).
        Used by publishing engine to generate correct img src.
        """
        return f'images/blog/{self.filename}' if self.filename else ''

