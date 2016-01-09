from django.contrib import admin

# Register your models here.

from .models import MenuItem
from .models import Restaurant
from .models import Monument

admin.site.register(MenuItem)
admin.site.register(Restaurant)
admin.site.register(Monument)