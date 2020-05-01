from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

from events.models import Event
from babies.models import Baby
from events.serializers import EventSerializer

from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory

def evaluar_notify(user, obj, request):
    #   user making request === baby parent name
    return user.name == obj.parent.name
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
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
                    'create_event': evaluar_notify,
                }
            }
        ),
    )

    #POST method    
    def create_event(self, serializer):
        # Get user making request and check if user.name == baby.parent.name
        user = self.request.user
        baby = Baby.objects.get(pk=self.request.data['baby'])
        print(baby.parent.name != user.name)
        
        if(baby.parent.name != user.name):
            raise PermissionDenied('Wrong baby')
        else:
            event = serializer.save()
            #   asociar permisos de evento/bebe y usuario/parent
            assign_perm('events.change_event', user, event)
            assign_perm('events.view_event', user, event)
            return Response(serializer.data)