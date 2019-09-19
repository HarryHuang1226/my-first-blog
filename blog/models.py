from django.conf import settings
from django.db import models
from django.utils import timezone

# use an uppercase for class name
class Post(models.Model):
    # link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # define text with a limited text
    title = models.CharField(max_length=200)
    # without a limit
    text = models.TextField()
    # Date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # when we call __str__() we will get a text (string) with a Post title.
    def __str__(self):
        return self.title