from rest_framework import viewsets
from truckingApp.models import Driver, Routes
from truckingApp.serializers import RoutesSerializer, DriverSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def find_routes(request): 
    route=Routes.objects.filter(truckdriver=request.data['truckdriver'], departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
    serializer = RoutesSerializer(route, many=True)
    return Response(serializer.data)



# Create your views here.
class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer