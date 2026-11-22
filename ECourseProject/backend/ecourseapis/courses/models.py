from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null = True)
    updated_date = models.DateTimeField(auto_now=True, null = True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='courses/%Y/%m/',null=True, blank=True)
    course = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.subject

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Lesson(BaseModel):

    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='lesson/%Y/%m/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons',related_query_name='my_lesson')
    tags = models.ManyToManyField('Tag', blank=True,related_name='lessons')
    class Meta:
        unique_together = ('subject', 'course')

    def __str__(self):
        return self.subject