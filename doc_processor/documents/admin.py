# documents/admin.py
from django.contrib import admin
from .models import Document, OCRResult, AIResult

# Registering models individually
admin.site.register(Document)
admin.site.register(OCRResult)
admin.site.register(AIResult)
