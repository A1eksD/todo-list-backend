from todolist.models import ToDoItem
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'