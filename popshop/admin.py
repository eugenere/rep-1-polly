from django.contrib import admin

from .models import Client, Owner, Cashier, Pledge, User

admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Cashier)
admin.site.register(Client)
admin.site.register(Pledge)

