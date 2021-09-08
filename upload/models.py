from django.core.exceptions import PermissionDenied
from django.db import models
from django.db.models.deletion import CASCADE


class KawasanBerikat(models.Model):
    nama_KB = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)

    kabupaten = (
        ('t', 'Tasikmalaya'),
        ('g', 'Garut')
    )

    kabupaten = models.CharField(max_length=1, choices=kabupaten)

    def kabupaten_detail(self):
        if self.kabupaten == 't':
            return 'Tasikmalaya'
        elif self.kabupaten == 'g':
            return 'Garut'

    def __str__(self):
        return str(self.nama_KB)


JenisDoc = (
    ('LapBul', 'Laporan Bulanan'),
    ('LapKegBul', 'Laporan Kegiatan Bulanan'),
)

Year = (
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
)

Bulan = (
    ('Januari', 'Januari'),
    ('Februari', 'Februari'),
    ('Maret', 'Maret'),
    ('April', 'April'),
    ('Mei', 'Mei'),
    ('Juni', 'Juni'),
    ('Juli', 'Juli'),
    ('Agustus', 'Agustus'),
    ('September', 'September'),
    ('Oktober', 'Oktober'),
    ('November', 'November'),
    ('Desember', 'Desember'),
)


class UploadDocument(models.Model):
    kawasanBerikat = models.ForeignKey(KawasanBerikat, on_delete=CASCADE)
    jenisDocument = models.CharField(max_length=10, choices=JenisDoc)
    tahun = models.CharField(max_length=4, choices=Year, default='2021')
    bulan = models.CharField(max_length=10, choices=Bulan)
    pdf = models.FileField(upload_to='laporan/pdfs')

    def __str__(self):
        return self.bulan

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
