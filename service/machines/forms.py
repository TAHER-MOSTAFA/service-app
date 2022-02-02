from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=90,
        error_messages={
        'required': "يجب ان تدخل الاسم",
        },)
    company = forms.CharField(max_length=90, required=False)
    message = forms.CharField(
        widget=forms.Textarea,
        error_messages={
        'required': "يجب ان تدخل الرسالة",
        })
    email = forms.EmailField(required=False)
    phone_num = forms.CharField(
        max_length=11,
        min_length=11,
        error_messages={
        'required': "يجب ان تدخل الهاتف",
        'max_length': "يجب ان تدخل الهاتف صحيح",
        'min_length': "يجب ان تدخل الهاتف صحيح"

        })
    
    def clean_phone_num(self):
        data = self.cleaned_data['phone_num']
        try:
            int(data)
        except:
            raise ValidationError("ادخل رقم هاتف صحيح")
        return data