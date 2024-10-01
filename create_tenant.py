from tenancy.models import Tenant
from extras.scripts import Script, StringVar
from django.utils.text import slugify

class CreateTenant(Script):
    class Meta: # type: ignore
        name = "Create Tenant"
        description = "My demo script"


    tenant_name = StringVar(label="Tenant Name")
    tenant_desc = StringVar(label="Tenant Desc", required=False)

    def run(self, data, commit):
        tenant = Tenant(
            name=data['tenant_name'],
            slug=slugify(data['tenant_name']),
            description=data['tenant_desc']
        )
        tenant.save()
        self.log_success(f"Created new tenant: {tenant}")