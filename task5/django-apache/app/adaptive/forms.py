from django import forms
from django.core.exceptions import ValidationError


class UploadPdfFileForm(forms.Form):
    file = forms.FileField(
        label="PDF-файл",
        widget=forms.FileInput(attrs={'accept': 'application/pdf'})
    )

    def clean_file(self):
        file = self.cleaned_data['file']

        if not file.name.endswith('.pdf'):
            raise ValidationError('Загрузка только PDF')

        return file
