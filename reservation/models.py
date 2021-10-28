from django.db import models


class Table(models.Model):
    capacity = models.IntegerField(verbose_name='Capacity')
    description = models.CharField(max_length=100, verbose_name='Description')
    is_reserved = models.BooleanField(default=False, verbose_name='Is Reserved')

    def __str__(self) -> str:
        return f'ID - {self.pk}. {self.description}'

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'


class Client(models.Model):
    name = models.CharField(max_length=40, verbose_name='Name')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Number')
    date_of_birth = models.DateField(verbose_name='Date of birth')

    def __str__(self) -> str:
        return f'{self.name}. Phone number - {self.phone_number} ' 

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Reservation(models.Model):
    client = models.ForeignKey('Client', on_delete=models.PROTECT, verbose_name='Client')
    date_and_time_of_reservation = models.DateTimeField(verbose_name='Date and time of reservation')
    number_of_people = models.IntegerField(verbose_name='Number of people')
    table = models.ForeignKey('Table', on_delete=models.PROTECT, verbose_name='Table')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    
    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
