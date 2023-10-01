# views.py

from rest_framework import views
from rest_framework.response import Response
from .models import Video
from .transcriber import main as transcribe
from .serializers import VideoSerializer

class VideoTranscriptionView(views.APIView):

    def post(self, request):
        video_file = request.FILES['video']
        # query = Video.objects.all()
        serializer = VideoSerializer()

        # Upload the video file to the server
        video = Video(title=video_file.name, file=video_file)
        video.save()
        print('-------------------')
        print(video.file.path)
        print("####################")
        videoPath = video.file.path
        #video_file.path

        # Transcribe the video file
        # transcript = transcribe(videoPath)
        transcript  = transcribe(PATH_TO_FILE = videoPath)

        # Save the transcript to the database
        video.transcript = transcript
        video.save()

        return Response({'transcript': transcript})
