from django.db import models
from django.contrib.auth.models import User
import hashlib

def video_upload_path(instance, filename):
    return f'videos/{filename}'

class Video(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=video_upload_path)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_hash = models.CharField(max_length=64, unique=True, blank=True, null=True)
    size = models.PositiveBigIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.file:
            hasher = hashlib.sha256()
            for chunk in self.file.chunks():
                hasher.update(chunk)
            self.file_hash = hasher.hexdigest()
            self.size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title or self.file.name} ({self.uploaded_by})"