from django.contrib import admin

# Allows users to create Topics and associate Entries to them.
# The . tells Django to look in the current directory
from .models import Topic, Entry

# The superuser can now accesss http://localost:8000/admin
admin.site.register(Topic)
admin.site.register(Entry)
