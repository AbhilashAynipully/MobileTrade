from django.forms import ModelForm
from .models import Mobile


class MobileAdditionForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        exclude = ['seller']