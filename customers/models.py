import uuid
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Client(TenantMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on= models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
