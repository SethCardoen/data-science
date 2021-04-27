from django.contrib import admin
from .models import Position
from .models import Sale
from .models import CSV

admin.site.register(Position) #classes toevoegen op de admin pagina
admin.site.register(Sale)
admin.site.register(CSV)
