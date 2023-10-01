# urls.py

from django.urls import path

from .views import VideoTranscriptionView

urlpatterns = [
    path('video-transcription/', VideoTranscriptionView.as_view(), name='video-transcription')
]
