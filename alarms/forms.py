from django import forms
from .models import Alarm

class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        # 自动排除不可编辑字段，避免 'created_at' 导致 FieldError
        exclude = [f.name for f in model._meta.fields if not f.editable]
        # 如果你明确知道只想展示的字段，可以改成 fields = ["device","status", ...]
