from django.db import models
from ckeditor.fields import RichTextField


class Posts(models.Model):
    title = models.CharField(max_length=500)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    cover_photo = models.ImageField(upload_to='picture')
    active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'
