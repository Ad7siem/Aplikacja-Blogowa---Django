from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

STATUS = (
    (1, 'Draft'), 
    (2, 'Published'),
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=55)
    subhead = models.CharField(max_length=55, blank=True, null=True)
    slug = models.SlugField(max_length=55, unique=True)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'get_slug': self.slug})