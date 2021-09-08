from django import forms


from .models import KawasanBerikat, UploadDocument


class KawasanBerikatForm(forms.ModelForm):
    class Meta:
        model = KawasanBerikat
        fields = ('nama_KB', 'alamat', 'kabupaten')


class UploadDocumentForms(forms.ModelForm):
    class Meta:
        model = UploadDocument
        fields = ('kawasanBerikat', 'jenisDocument', 'tahun', 'bulan', 'pdf')
