from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60, blank=True)
    dob = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    about = models.CharField(blank=True)
    created_date = models.DateField(default=timezone.now())

    def __str__(self):
        return ("{} {}".format(self.first_name, self.last_name) +
                " {}".format(self.surname) if self.surname else "")


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
