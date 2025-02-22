# Library Calls

from django.contrib import admin
from .models import Topic, Entry

# call a model
admin.site.register(Topic)
admin.site.register(Entry)