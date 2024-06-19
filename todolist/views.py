from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView

from todolist.models import ToDoItem
from todolist.serializers import TodoSerializer


# Create your views here.


"""
    https://www.django-rest-framework.org/api-guide/authentication/ 
    doc zu der function
"""
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        #nimmt die daten auf and wandelt die mit dem serializer in python code um
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        #überprüft ob die anfage valide ist
        serializer.is_valid(raise_exception=True)
        #hole user aus dem post request
        user = serializer.validated_data['user']
        #token wird erstellt oder durch get_or_create abgerufen, wenn der schon vorhanden ist
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
        
class TodoItemView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []

    def get(self, request, format=None):
        todos = ToDoItem.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)