from django.urls import path

from .views import (TableAPIView, TableDetailAPIView, ReservationHistoryAPIView, FutureReservationAPIView, 
ReservationDetailAPIView, ClientDetailAPIView, ReservationCreateAPIView)


urlpatterns = [
    path('tables/', TableAPIView.as_view()),
    path('tables/<int:pk>/', TableDetailAPIView.as_view()),
    path('clients/<int:pk>/', ClientDetailAPIView.as_view()),
    path('reservations_history/', ReservationHistoryAPIView.as_view()),
    path('reservations/', FutureReservationAPIView.as_view()),
    path('reservations/<int:pk>/', ReservationDetailAPIView.as_view()),
    path('new_reservation/', ReservationCreateAPIView.as_view())
]