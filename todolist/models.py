from django.conf import settings
from django.db import models
from datetime import datetime

# Create your models here.
class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(default=datetime.today())
    done = models.BooleanField(default=False)
    
    def __str__(self): # bearbeite die anzeige(überschrift9) bei der adminansicht
        # return str(self.text) + '' + self.text # zeige id + den titel an / schreibweise 1
        return f'({self.id}) {self.text}' # zeige id + den titel an / schreibweise 2