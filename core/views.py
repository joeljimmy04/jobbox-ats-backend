from django.shortcuts import render
from django.http import HttpResponse
from .models import application,job,user
from .serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse("Hello Zecpath Backend")

class JobListAPI(APIView):
    def get(self,request):
        jobs=job.objects.all()
        serializer=JobSerializer(jobs,many=True)
        return Response(serializer.data)
        
class JobCreateAPI(APIView):
    def post(self,request):
        serializer=JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
