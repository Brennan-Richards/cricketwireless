
from django.forms import ModelForm
from .models import Lead, Line
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

                css_class="basic-form"
            )
        )


class EmployeeLeadForm(ModelForm):
    class Meta:
        model = Lead
        exclude = [ 'date_created', 'date_sold']

    def __init__(self, *args, **kwargs):

        # NOTE: Must always pop keyword arguments before calling super().__init__
        update = kwargs.pop('update')

        super(EmployeeLeadForm, self).__init__(*args, **kwargs)

        button_text = 'Contact us' if not update else 'Update'

        header_content = '''<h5>Employee view
                                <img src="/static/question-icon.png" class="icon-sm" data-toggle="tooltip" data-placement="right" 
                                title="You are viewing this contact page as an employee. Clients will see less fields for simplicity's sake. To view the page from the perspective of
                                a client, you must navigate to this URL without being logged in." >
                            </h5>
                            <br>
                        '''

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                
                HTML(header_content),

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

                Div(
                    Div(
                        Field('city', css_class='form-control'),
                    css_class="col"),
                    Div(
                        Field('state', css_class='form-control'),
                    css_class="col"),
                css_class="form-row"    
                ),

                HTML('<br>'),

                Div(
                    Div(
                        Field('zip_code', css_class='form-control'),
                    css_class="col"),
                    Div(
                        Field('street_address', css_class='form-control'),
                    css_class="col"),
                css_class="form-row"    
                ),

                HTML('<br>'),

                Field('message_from_client', css_class='form-control'),

                HTML('<br>'),

                Field('desired_service', css_class='form-control'),

                HTML('<br>'),

                Field('current_status', css_class='form-control'),
                
                HTML('<br>'),

                Field('date_last_interacted', css_class='form-control', autocomplete="off"),
                HTML('<br>'),

                Field('rate_plan', css_class='form-control', style='max-height: 100px; overflow:scroll;'),
                HTML('<br>'),

                Field('auto_pay', css_class='form-control', style='max-height: 100px; overflow:scroll;'),
                HTML('<br>'),

                ButtonHolder(
                    Submit('submit', button_text, css_class='btn btn-light btn-outline-secondary form-control'),                        
                ),

                css_class="basic-form"
            )
        )

class LineForm(ModelForm):
    class Meta:
        model = Line
        exclude = ['lead']

    def __init__(self, *args, **kwargs):

        # NOTE: Must always pop keyword arguments before calling super().__init__
        update = kwargs.pop('update')

        super(LineForm, self).__init__(*args, **kwargs)

        button_text = 'Create line' if not update else 'Update line'

        form_header_content = f'''<h5>
                                { button_text }
                                </h5>
                                <br>
                              '''
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                HTML(form_header_content),

                Field('phone_number', css_class='form-control', value="+1"),
                HTML('<br>'),


                Field('cricket_protect', css_class='form-control'),
                HTML('<br>'),

                Field('current_device_type', css_class='form-control'),
                HTML('<br>'),

                Field('upgrade_eligibility_date', css_class='form-control', autocomplete="off"),
                HTML('<br>'),

                ButtonHolder(
                    Submit('submit', button_text, css_class='btn btn-light btn-outline-secondary form-control'),                        
                ),

                css_class="basic-form"
            )
        )