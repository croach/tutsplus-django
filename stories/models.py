from urlparse import urlparse

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Story(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    points = models.IntegerField(default=1)
    moderator = models.ForeignKey(User, related_name='moderated_stories')
    voters = models.ManyToManyField(User, related_name='liked_stories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def domain(self):
        return urlparse(self.url).netloc

    def get_absolute_url(self):
        return reverse('stories:story_detail', args=(self.id,))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "stories"

class Comment(models.Model):
    story = models.ForeignKey(Story, related_name='comments')
    body = models.TextField()

