from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

from babies.models import Baby
from events.models import Event
from babies.serializers import BabySerializer
from events.serializers import EventSerializer

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

def evaluar_notify(user, obj, request):
    #   user making request === baby parent name
    return user.name == obj.parent.name

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': evaluar_notify,
                    'destroy': evaluar_notify,
                    'update': evaluar_notify,
                    'partial_update': evaluar_notify,
                    'events': evaluar_notify,
                    'create': evaluar_notify,
                    # 'update_permissions': 'users.add_permissions'
                    # 'archive_all_students': phase_user_belongs_to_school,
                    # 'add_clients': True,
                }
            }
        ),
    )

    def create(self, serializer):
        #   get user making request and check auth.
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied('Unauthenticated')
        else:
            baby = serializer.save()
            assign_perm('baby.change_baby', user, baby)
            assign_perm('baby.view_baby', user, baby)
            return Response(serializer.data)

    # GET method
    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        queryset = Event.objects.filter(baby = baby)
        data = EventSerializer(queryset, many = True).data
        return Response(data)