from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory
#   los permisos de samuel

from parents.models import Parent
from babies.models import Baby
from parents.serializers import ParentSerializer
from babies.serializers import BabySerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    @action(detail=True, methods=['get'])
    def babies(self, request, pk=None):
        parent = self.get_object()
        queryset = Baby.objects.filter(parent = parent)
        data = BabySerializer(queryset, many = True).data
        return Response(data)