from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Incident
from .serializers import IncidentSerializer
from .permission import IsOwner
from .pagination import IncidentPageNumberPagination
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def incidents(request):
    if request.method == 'GET':
        incidents = Incident.objects.filter(user=request.user).order_by('-date_creation')
        
        paginator = IncidentPageNumberPagination()
        result_paginator = paginator.paginate_queryset(incidents, request)
        
        serializer = IncidentSerializer(result_paginator, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsOwner])
def getOne(request, pk):
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return Response({'error': 'Incident non trouvé.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        incident.delete()
        return Response({'message': 'Incident supprimé avec succès.'}, status=status.HTTP_204_NO_CONTENT)
