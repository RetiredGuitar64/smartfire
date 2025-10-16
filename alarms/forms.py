from django import forms
from .models import Alarm
class AlarmForm(forms.ModelForm):
    class Meta:
        model=Alarm
        fields=['device','level','message','status','cleared_at']
