from django.test import TestCase
from django.test import TestCase
from .models import Document, OCRResult, AIResult
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

class DocumentProcessingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_document_upload_and_processing(self):
        with open('test_image.png', 'rb') as img:
            document = SimpleUploadedFile(name='test_image.png', content=img.read(), content_type='image/png')
            response = self.client.post('/upload/', {'title': 'Test Image', 'file': document})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(OCRResult.objects.count(), 1)
        self.assertEqual(AIResult.objects.count(), 1)
