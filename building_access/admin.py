from django.contrib import admin
from .models import Tag
from .models import Door
from .models import Group
from .models import Phone



admin.site.register(Tag)
admin.site.register(Door)
admin.site.register(Group)
admin.site.register(Phone)