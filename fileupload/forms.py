from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file', help_text='Accepted formats: .xlsx, .csv')
    recipient_list = forms.CharField(
        label='Recipient Email(s)',
        widget=forms.TextInput(attrs={'placeholder': 'Enter recipient emails, separated by commas'}),
        help_text='Enter recipient emails, separated by commas.'
    )
    cc_list = forms.CharField(
        label='CC Email(s)',
        widget=forms.TextInput(attrs={'placeholder': 'Enter CC emails, separated by commas'}),
        required=False,  # This field is optional
        help_text='Enter CC emails, separated by commas (optional).'
    )



"""
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
"""
