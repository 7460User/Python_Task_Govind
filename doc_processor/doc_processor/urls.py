"""
URL configuration for doc_processor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from documents import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',views.upload_document),
    path('home/',views.process_document),
    path('home1',views.extract_text),
    path('home2',views.analyze_text),
    path('home3',views.document_list),
]
