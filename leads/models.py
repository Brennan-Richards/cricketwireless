from django.db import models

from tinymce.models import HTMLField

# Create your models here.

INQUIRED = "Inquired"
CONTACTED = "Contacted"
SOLD = "Sold"

LEAD_STATUS_CHOICES = [
    (INQUIRED, "Inquired"),
    (CONTACTED, "Contacted"),
    (SOLD, "Sold")
]


PHONE = "Phone call"
ONLINE_FORM = "Online form"
MANUAL = "Manually created"

LEAD_TYPE_CHOICES = [
    (PHONE, "Phone call"),
    (ONLINE_FORM, "Online form"),
    (MANUAL, "Manually created")
]


QUOTE_TO_SWITCH = "Request a quote for switching to Cricket"
PROMOTIONS = "Request a call regarding ongoing promotions"
UPGRADES = "Upgrading existing devices/plans"
SPECIFIC_DEVICE = "Looking to purchase a specific device"
ADD_LINES = "Need information on adding new lines"
OTHER = "Other"

DESIRED_SERVICES = [
    (QUOTE_TO_SWITCH, "Request a quote for switching to Cricket"),
    (PROMOTIONS, "Request a call regarding ongoing promotions"),
    (UPGRADES, "Upgrading existing devices/plans"),
    (SPECIFIC_DEVICE, "Looking to purchase a specific device"),
    (ADD_LINES, "Need information on adding new lines"),
    (OTHER, "Other")
]

class Lead(models.Model):
    # property = models.ForeignKey(Property, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    # The source that generated the lead.
    source = models.CharField(blank=True, null=True, max_length=64, default=None)

    # The status of the lead.
    current_status = models.CharField(blank=True, null=True, max_length=9, choices=LEAD_STATUS_CHOICES, default=INQUIRED)

    # Stores the service that the client desires, the reason they're contacting.
    desired_service = models.CharField(blank=True, null=True, max_length=43, choices=DESIRED_SERVICES, default=QUOTE_TO_SWITCH)

    # A field for keeping notes on the client.
    notes = HTMLField(blank=True, null=True, default=None)

    # A field for any messages from the client which may come in from online forms.
    message_from_client = HTMLField('Other messages/information', blank=True, null=True, default=None)

    # How was the lead generated?
    medium = models.CharField('How was the lead generated?', blank=True, null=True, max_length=16, choices=LEAD_TYPE_CHOICES, default=MANUAL)

    phone_number = models.CharField(max_length=20, blank=True, null=True, default=None)
    email_address = models.CharField(max_length=100, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=150, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=150, blank=True, null=True, default=None)
    
    city = models.CharField(max_length=150, blank=True, null=True, default=None)
    state = models.CharField(max_length=150, blank=True, null=True, default=None)
    zip_code = models.CharField(max_length=20, blank=True, null=True, default=None)
    street_address = models.CharField(max_length=150, blank=True, null=True, default=None)

    date_created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    
    # Track this attributed when the lead's status becomes "Sold"
    date_sold = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        name = ""

        if self.first_name is None and self.last_name is None:
            return "Unnamed lead"

        if self.first_name is not None:
            name += self.first_name + ' '
        else:
            name += '-'

        if self.last_name is not None:
            name += self.last_name
        else:
            name += '-'
        
        return name