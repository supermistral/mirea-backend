import PyPDF2

from django import forms
from django.core.exceptions import ValidationError


class UploadPdfFileForm(forms.Form):
    file = forms.FileField(
        label="PDF-файл",
        widget=forms.FileInput(attrs={'accept': 'application/pdf'})
    )

    def clean_file(self):
        file = self.cleaned_data['file']

        try:
            PyPDF2.PdfFileReader(file)
        except PyPDF2.errors.PdfReadError:
            raise ValidationError('Загрузка только PDF')
        except Exception:
            raise ValidationError('Произошла неизвестная ошибка при чтении файла')

        return file
