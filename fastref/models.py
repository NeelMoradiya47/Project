from django.db import models

# Table 1: Stores a list of categories
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    language_name = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

# Table 2: Represents languages associated with categories
class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.TextField()
    category_id = models.IntegerField()
    description = models.TextField()
    is_deleted = models.IntegerField()
    bg_color = models.CharField(max_length=255)
    html = models.TextField(default=None)

# Table 3: Taking feedbacks from users
class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email_id = models.EmailField()
    feedback = models.TextField()
