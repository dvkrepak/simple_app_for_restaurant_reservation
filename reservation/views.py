from rest_framework import generics, filters, viewsets

from .models import Table, Client, Reservation
from .filters import ReservationFilter, TableFilter
from .serializers import (TableSerializer, ClientDetailSerializer, TableDetailSerializer,
ReservationSerializer, ReservationDetailSerializer, ReservationCreateSerializer)


class TableAPIView(generics.ListAPIView):
    """Get information about all tables"""
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    filter_backends = (TableFilter, filters.OrderingFilter)


class TableDetailAPIView(generics.RetrieveAPIView):
    """Get informatiobn about current table"""
    serializer_class = TableDetailSerializer
    queryset = Table.objects.filter()


class ClientDetailAPIView(generics.RetrieveAPIView):
    """Get information about current client"""
    serializer_class = ClientDetailSerializer
    queryset = Client.objects.filter()


class ReservationHistoryAPIView(generics.ListAPIView):
    """Get information about all reservations"""
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = (ReservationFilter, filters.OrderingFilter)


class FutureReservationAPIView(generics.ListAPIView):
    """Get information about future reservations"""
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.filter(is_active=True)
    filter_backends = (ReservationFilter, filters.OrderingFilter)


class ReservationDetailAPIView(generics.RetrieveAPIView):
    """Get information about current reservation"""
    serializer_class = ReservationDetailSerializer
    queryset = Reservation.objects.filter()


class ReservationCreateAPIView(generics.CreateAPIView):
    """Create new reservation"""
    serializer_class = ReservationCreateSerializer
