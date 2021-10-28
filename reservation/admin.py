from django.contrib import admin

from .models import Table, Client, Reservation


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'capacity', 'is_reserved')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'date_of_birth')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_and_time_of_reservation', 'number_of_people', 'table', 'is_active')


admin.site.register(Table, TableAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Reservation, ReservationAdmin)
