from django.forms import ModelForm, widgets
from .models import *

class NewCashierForm(ModelForm):
    class Meta:
        model = Cashier
        fields = [
			'login', 
			'key', 
			'first_name',
			'family',
			'surname',
			'passportCode',
		]
