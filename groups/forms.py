from django import forms
from .models import Elem

class ElemCreateForm(forms.ModelForm):
	class Meta:
		model = Elem
		fields = ['elem_parent_group', 'name', 'description', 'icon']