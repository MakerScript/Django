from django.contrib import admin
from .models import Genre, Language, App, Author

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(App)
admin.site.register(Author)

