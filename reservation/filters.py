from rest_framework import filters
from django.db.models import Q


class ReservationFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        client = request.query_params.get('client')
        table = request.query_params.get('table')
        date = request.query_params.get('date')
        all_params = Q()

        if client:
            current_param = Q(client_id=client)
            all_params.add(current_param, Q.AND)
        
        if table:
            current_param = Q(table_id=table)
            all_params.add(current_param, Q.AND)

        if date:
            if len(date) == 10: 
                start_of_the_day = date + 'T00:00:01Z'
                end_of_the_day = date + 'T23:59:59Z'
                current_param = Q(date_and_time_of_reservation__lte=end_of_the_day, date_and_time_of_reservation__gte=start_of_the_day)
                all_params.add(current_param, Q.AND)
            if len(date) != 10:
                raise AttributeError('Put into date-sorting correct data: YYYY-MM-DD')

        return queryset.filter(all_params)
    

class TableFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        reserved = request.query_params.get('is_reserved')
        capacity = request.query_params.get('capacity')
        all_params = Q()

        if reserved:
            if reserved == '1':
                current_param = Q(is_reserved=True)
            else:
                current_param = Q(is_reserved=False)
            all_params.add(current_param, Q.AND)

        if capacity:
            current_param = Q(capacity=capacity)
            all_params.add(current_param, Q.AND)

        return queryset.filter(all_params)
