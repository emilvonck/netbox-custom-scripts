from extras.scripts import *
from django.utils.text import slugify
from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site

class CreateSite(Script):
    class Meta: # type: ignore
        name = "Create Site"
        description = "Script to create a new Site"

    site = ObjectVar(
        description="Access switch model",
        model=Site
    )
    device_count = IntegerVar(
        description="Number of devices to create"
    )
    device_type = ObjectVar(
        description="Device type",
        model=DeviceType
    )
    def run(self, data, commit):
        site = Site(
            name=data['site_name'],
            slug=slugify(data['site_name']),
            status=SiteStatusChoices.STATUS_PLANNED
        )
        site.save()
        self.log_success(f"Created new site: {site}")
        device_role = DeviceRole.objects.get(name='Access Point')
        # Create devices
        device_role = DeviceRole.objects.get(name='Access Switch')
        for i in range(1, data['device_count'] + 1):
            device = Device(
                device_type=data['device_type'],
                name=f'{site.slug.upper()}-dev-{i}',
                site=site,
                status=DeviceStatusChoices.STATUS_PLANNED,
                device_role=device_role
            )
            device.save()
            self.log_success(f"Created new switch: {device}")