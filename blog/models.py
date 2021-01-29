from django.db import models


class Author(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self):
    return self.name

class Post(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  title = models.CharField(max_length=40)
  content = models.TextField(max_length=300)
  slug = models.SlugField(max_length=200, unique_for_date='publish')
  postedAt = models.DateField()

  def __str__(self):
    return self.title