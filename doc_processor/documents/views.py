from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from .models import Document, OCRResult, AIResult
import pytesseract
from PIL import Image
import spacy
from transformers import pipeline

# Create your views here.

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            process_document(document.id)
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def process_document(doc_id):
    document = Document.objects.get(id=doc_id)
    ocr_text = extract_text(document.file.path)
    ocr_result = OCRResult.objects.create(document=document, extracted_text=ocr_text)
    
    ai_results = analyze_text(ocr_text)
    AIResult.objects.create(
        ocr_result=ocr_result,
        entities=ai_results['entities'],
        classification=ai_results['classification'],
        sentiment=ai_results['sentiment']
    )

def extract_text(file_path):
    return pytesseract.image_to_string(Image.open(file_path))

def analyze_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    classifier = pipeline('text-classification')
    classification = classifier(text)[0]['label']

    sentiment_analyzer = pipeline('sentiment-analysis')
    sentiment = sentiment_analyzer(text)[0]['label']

    return {
        'entities': entities,
        'classification': classification,
        'sentiment': sentiment,
    }

@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'document_list.html', {'documents': documents})
