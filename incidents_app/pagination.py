from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class IncidentPageNumberPagination(PageNumberPagination):  
    page_size = 10

class IncidentLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10
