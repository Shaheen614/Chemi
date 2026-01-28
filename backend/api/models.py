from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="datasets/")

