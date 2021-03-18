from django.db import models

from tinymce.models import HTMLField

# Create your models here.

INQUIRED = "Inquired"
CONTACTED = "Contacted"
SOLD = "Sold"
UNSELLABLE = "Unsellable"

LEAD_STATUS_CHOICES = [
    (INQUIRED, "Inquired"),
    (CONTACTED, "Contacted"),
    (SOLD, "Sold"),
    (UNSELLABLE, "Unsellable")

]


# PHONE = "Phone call"
# ONLINE_FORM = "Online form"
# MANUAL = "Manually created"

# LEAD_TYPE_CHOICES = [
#     (PHONE, "Phone call"),
#     (ONLINE_FORM, "Online form"),
#     (MANUAL, "Manually created")
# ]
# medium = models.CharField('How was the lead generated?', blank=True, null=True, max_length=16, choices=LEAD_TYPE_CHOICES, default=MANUAL) # How was the lead generated?


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


MORE = 'More'
CORE = 'Core'
TENGB = '10GB'
TWOGB = '2GB'

RATE_PLANS = [
    (MORE, 'More'),
    (CORE, 'Core'),
    (TENGB, '10GB'),
    (TWOGB, '2GB')
]

class Lead(models.Model):

    source = models.CharField(blank=True, null=True, max_length=64, default=None) # The source that generated the lead.

    current_status = models.CharField(blank=True, null=True, max_length=10, choices=LEAD_STATUS_CHOICES, default=INQUIRED) # The status of the lead.

    desired_service = models.CharField(blank=True, null=True, max_length=43, choices=DESIRED_SERVICES, default=QUOTE_TO_SWITCH) # Stores the service that the client desires, the reason they're contacting.
    
    notes = HTMLField(blank=True, null=True, default=None) # A field for keeping notes on the client.

    message_from_client = HTMLField('Other messages/information', blank=True, null=True, default=None) # A field for any messages from the client which may come in from online forms.
    
    rate_plan = models.CharField(blank=True, null=True, max_length=4, choices=RATE_PLANS, default=None) 

    date_last_interacted = models.DateField(blank=True, null=True, default=None)

    auto_pay = models.BooleanField(blank=True, null=True, default=False)

    # Contact information
    phone_number = models.CharField(max_length=20, blank=True, null=True, default=None)
    email_address = models.CharField(max_length=100, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=150, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=150, blank=True, null=True, default=None)
    
    city = models.CharField(max_length=150, blank=True, null=True, default=None)
    state = models.CharField(max_length=150, blank=True, null=True, default=None)
    zip_code = models.CharField(max_length=20, blank=True, null=True, default=None)
    street_address = models.CharField(max_length=150, blank=True, null=True, default=None)

    # Date fields.
    date_created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    date_sold = models.DateField(blank=True, null=True, default=None) # Track this attributed when the lead's status becomes "Sold"


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

class Line(models.Model):
    """
    This object represents a phone line, attached to a Lead/customer. A customer may have any number of lines.
    """
    lead = models.ForeignKey(Lead, blank=False, null=False, default=None, on_delete=models.CASCADE)
    cricket_protect = models.BooleanField(blank=True, null=True, default=False)
    current_device_type = models.CharField(blank=True, null=True, max_length=128, default=None)
    upgrade_eligibility_date = models.DateField(blank=True, null=True, default=None)
