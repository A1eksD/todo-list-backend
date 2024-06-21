from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView

from todolist.models import ToDoItem
from todolist.serializers import TodoSerializer
from django.db import models

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
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        todos = ToDoItem.objects.filter(author=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save(author=request.user)
          return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, id, format=None):
        if request.method =="delete":
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                todo_id = serializer.validated_data.get('id')
                todo_id.delete()
            return Response(serializer.errors)

            # todo = ToDoItem.objects.get(id=id)
            # todo.delete()
            # return HttpResponseRedirect(status=204)
    
    
    # def delete(self, request, format=None):
    #     try:
    #         todo_id = int(request.data['id'])  # ID aus dem Request-Body holen
    #         todo_item = ToDoItem.objects.get(id=todo_id, author=request.user)  # ToDo anhand der ID und des Autors suchen
    #         todo_item.delete()  # ToDo löschen
    #         return Response({'message': 'ToDo erfolgreich gelöscht'})
    #     except (ValueError, ToDoItem.DoesNotExist):
    #         return Response({'error': 'Ungültige ToDo-ID oder ToDo nicht gefunden'}, status=400)
