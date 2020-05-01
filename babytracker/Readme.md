#   Django Rest Framework Lab

Creacion de modelos, migraciones y autenticación.

##  Add user/parent event or babies:

```python

from django.contrib.auth.models import User

User.objects.create_superuser('name', 'username', 'pw')


from parents.models import Parent

parent = Parent()
parent.name = 'name'
parent.age = 16
parent.save()

from babies.models import Baby

baby = Baby()
baby.name = 'name'
baby.parent = parent
baby.save()

from events.models import Event

event = Event()
event.description = 'string'
event.baby = baby
event.save()
```