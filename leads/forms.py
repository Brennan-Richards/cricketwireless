
from django.forms import ModelForm
from .models import Lead
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, HTML, Div, ButtonHolder

class ContactForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['phone_number', 'email_address', 'first_name', 'last_name', 'message_from_client', 'desired_service']

    def __init__(self, *args, **kwargs):

        # NOTE: Must always pop keyword arguments before calling super().__init__
        update = kwargs.pop('update')

        super(ContactForm, self).__init__(*args, **kwargs)

        button_text = 'Contact us' if not update else 'Update'

        header_content = '''<h5>Service request
                                <img src="/static/question-icon.png" class="icon-sm" data-toggle="tooltip" data-placement="right" 
                                    title="Fill in the form with your information, and a Cricket representative will be in touch
                                    with you in a timely manner to start you on the process to fulfilling your request." >
                                </h5>
                                <br>
                              '''
        
        form_header_content = header_content if not update else ''

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                HTML(form_header_content),
                Div(
                    Div(
                        Field('first_name', css_class='form-control'),
                    css_class="col"),
                    Div(
                    Field('last_name', css_class='form-control'),
                    css_class="col"),
                css_class="form-row"    
                ),

                HTML('<br>'),

                Div(
                    Div(
                        Field('phone_number', css_class='form-control'),
                    css_class="col"),
                    Div(
                        Field('email_address', css_class='form-control'),
                    css_class="col"),
                css_class="form-row"    
                ),

                HTML('<br>'),

                Field('desired_service', css_class='form-control'),
                
                HTML('<br>'),

                Field('message_from_client', css_class='form-control', style='max-height: 100px; overflow:scroll;'),
                HTML('<br>'),

                ButtonHolder(
                    Submit('submit', button_text, css_class='btn btn-light btn-outline-secondary form-control'),                        
                ),

                css_class="contact-us-form"
            )
        )
