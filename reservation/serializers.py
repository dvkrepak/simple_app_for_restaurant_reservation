from rest_framework import serializers

from .models import Table, Client, Reservation

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ('pk', 'capacity', 'is_reserved', 'table_link')


class TableDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'


class ClientDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('pk', 'name', 'phone_number')


class ReservationSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='name', read_only=True)
    table = serializers.SlugRelatedField(slug_field='pk', read_only=True)

    class Meta:
        model = Reservation
        fields = ('pk', 'client', 'date_and_time_of_reservation', 'table')


class ReservationDetailSerializer(ReservationSerializer):

    class Meta:
        model = Reservation
        fields = ('pk', 'client', 'date_and_time_of_reservation',
         'table', 'number_of_people', 'is_active')


class ReservationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'
