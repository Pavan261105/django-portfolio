from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=250, help_text="Comma-separated list of technologies")
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.name} ({self.email})"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    cover_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    description = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # leave blank if current
    tech_stack = models.CharField(max_length=250, help_text="Comma-separated technologies used")
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"
