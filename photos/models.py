from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Photo(models.Model):
        Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
        description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name