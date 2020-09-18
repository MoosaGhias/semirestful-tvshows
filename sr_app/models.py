from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = "Must include title"
        elif len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        if len(postData['network']) == 0:
            errors['network'] = "Must include network"
        elif len(postData['network']) < 2:
            errors['network'] = "Must be at least 3 characters"
        if len(postData['description']) == 0:
            errors['description'] = "Must include description"
        elif len(postData['description']) < 5:
            errors['description'] = "Description must be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ShowManager()