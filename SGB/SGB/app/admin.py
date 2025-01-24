from django.contrib import admin
from app.models import User, Bem  # Substitua "app" pelo nome do seu aplicativo

# Registrando os modelos no admin
admin.site.register(User)
admin.site.register(Bem)
