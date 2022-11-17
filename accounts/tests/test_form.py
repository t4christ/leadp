from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from accounts.forms import RegisterForm

class RegisterFormTest(TestCase):

    def test_register_form_email_field_label(self):
        form = RegisterForm()        
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'email')

    
    def test_register_form_username_field_label(self):
        form = RegisterForm()        
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'username')



    def test_register_form_first_name_field_label(self):
        form = RegisterForm()        
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'first_name')



    
    def test_register_form_last_name_field_label(self):
        form = RegisterForm()        
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'last_name')
    
    
    # def test_renew_form_date_field_help_text(self):
    #     form = RenewBookForm()
    #     self.assertEqual(form.fields['renewal_date'].help_text,'Enter a date between now and 4 weeks (default 3).')
