from extras.scripts import *
from django.utils.text import slugify
from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site
from ipam.models import Prefix, IPAddress, IPRange

class CreateSite(Script):
    class Meta: # type: ignore
        name = "Create Site"
        description = "Script to create a new Site"

    site_input = ObjectVar(
        description="Site name",
        model=Site
    )
    device_count = IntegerVar(
        description="Number of devices to create"
    )
    device_type = ObjectVar(
        description="Device type to create",
        model=DeviceType
    )
    def run(self, data, commit):
        site = Site.objects.get(name=data['site_input'].name)
        device_role = DeviceRole.objects.get(name='Access-AP')
        # Create devices
        self.log_success(dir(Prefix))
        self.log_success(dir(IPAddress))
        self.log_success(dir(IPRange))
        for i in range(1, data['device_count'] + 1):
            device = Device(
                device_type=data['device_type'],
                name=f'{site.slug.upper()}-dev-{i}',
                site=site,
                status=DeviceStatusChoices.STATUS_PLANNED,
                device_role=device_role
            )
            device.save()
            self.log_success(f"Created new {device_role.name}: {device} in site: {site.name}")