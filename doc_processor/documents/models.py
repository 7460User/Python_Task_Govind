from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class OCRResult(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    extracted_text = models.TextField()

class AIResult(models.Model):
    ocr_result = models.OneToOneField(OCRResult, on_delete=models.CASCADE)
    entities = models.TextField()  # JSON field could be used
    classification = models.CharField(max_length=255)
    sentiment = models.CharField(max_length=50)
