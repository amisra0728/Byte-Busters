from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.http import JsonResponse


@api_view()
def hello_world(request):
    return Response({"status": 200, "message": "Hello, World!"})
# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({"status": 403, "message": "Invalid req","error": serializer.errors})

        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user = user)
        return Response({"status": 200, "data": serializer.data, "message": "Successful", "token": str(token_obj)})
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })

class UserView(APIView):
    def get(self, request):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        print(request.user)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"status": 200, "data": serializer.data, "message": "Successful"})

class FlatCreateAPIView(APIView):
    def post(self, request):
        serializer = FlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetFlatSearchAPI(APIView): 
    def get(self,request):
        flat = Flat.objects.all()
        data = {'flat': list(flat.values())}
        return JsonResponse(data)

class get_flats_by_location(APIView):
    def get(self,request):
        location = request.GET.get('location')
        flats = Flat.objects.filter(location=location)
        data = {'flats': list(flats.values())}
        return JsonResponse(data)

class FlatmateCreateAPIView(APIView):
    def post(self, request):
        serializer = FlatmateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class get_flatmates_by_location(APIView):
    def get(self,request):
        location = request.GET.get('location')
        flatmate = Flatmate.objects.filter(location=location)
        data = {'flatmates': list(flatmate.values())}
        return JsonResponse(data)

class GetFlatmateSearchAPI(APIView): 
    def get(self,request):
        flatmate = Flatmate.objects.all()
        data = {'flat': list(flatmate.values())}
        return JsonResponse(data)