from django.forms import ModelForm, widgets
from .models import Soul, Swag

class NewSoulForm(ModelForm):
	class Meta:
		model = Soul
		fields = ['name', 'key', 'kind']
		#widgets = {'kind': widgets.Select(attrs={'readonly':True, 'disabled':True})}
