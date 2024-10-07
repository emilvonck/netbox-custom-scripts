from extras.scripts import *
from django.utils.text import slugify
from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site
from ipam.models import Prefix, IPAddress, IPRange, VLAN

class CreateSite(Script):
    class Meta: # type: ignore
        name = "Create Gaming Console"
        description = "Script to create a new gaming console and allocate addresssing automatically"

    site_input = ObjectVar(
        description="Site name",
        model=Site
    )

    def run(self, data, commit):
        site = Site.objects.get(name=data['site_input'].name)
        self.log_success(site)

        # Create devices
        # self.log_success(dir(Prefix))
        # self.log_success(dir(IPAddress))
        # self.log_success(dir(IPRange))