from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='Accepted formats: .xlsx, .csv'
    )


"""
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
"""
