# Import Django's forms module
from django import forms

# Import our Topic model from the current directory, models.py
from .models import Topic


# Create a class for our model's form
class TopicForm(forms.ModelForm):
    class Meta:
        # Build a form from our model
        model = Topic
        # Don't generate a text label for the textfield
        labels = {'text': ''}
        # Define our textfields to be displayed on the form
        fields = ['text']


