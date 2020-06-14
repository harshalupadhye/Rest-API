from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from newapp.models import boot
from newapp.serializers import bootSerializer

# Create your views here.
class bootView(APIView):
    def get(self, request):
        queryset = boot.objects.filter(Email=request.data.get("Email")).values().first()
        return Response(queryset)

    def post(self, request):
        queryset = request.data
        serializer = bootSerializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
            return Response("data saved")
     
    

