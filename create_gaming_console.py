from extras.scripts import *
from django.utils.text import slugify
from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site
from ipam.models import Prefix, IPAddress, IPRange, VLAN

class CreateSite(Script):
    class Meta: # type: ignore
        name = "Create New Router"
        description = "Script to create a new router on site and allocate adressing autmatically"

    site_input = ObjectVar(
        description="Site name",
        model=Site
    )
    vlan_input = ObjectVar(
        description="Vlan",
        model=VLAN
    )

    def run(self, data, commit):
        site = Site.objects.get(name=data['site_input'].name)
        self.log_success(site)

        # Create devices
        # self.log_success(dir(Prefix))
        # self.log_success(dir(IPAddress))
        # self.log_success(dir(IPRange))