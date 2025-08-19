from django.db import models
from django.contrib.auth.models import User


class Testimonials(models.Model):
    # User-submitted details
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # role = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # 1–5 stars

    # Optional links
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)

    # Meta info
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company if self.company else 'No Company'}"
