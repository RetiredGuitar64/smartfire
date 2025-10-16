from django import forms
from .models import Alarm

def editable_fields(model):
    names = []
    for f in model._meta.get_fields():
        # 只收集“真实字段 & 非自动创建 & 非ID & 可编辑”
        if not getattr(f, "concrete", False):
            continue
        if getattr(f, "auto_created", False):
            continue
        if f.name == "id":
            continue
        if hasattr(f, "editable") and not f.editable:
            continue
        names.append(f.name)
    return names

class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = editable_fields(Alarm)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            # 下拉用 form-select，其它用 form-control（兼容 bootstrap）
            if isinstance(f.widget, forms.Select):
                f.widget.attrs.update({"class": "form-select"})
            else:
                f.widget.attrs.update({"class": "form-control"})
