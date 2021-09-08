from django.contrib import admin

from .models import KawasanBerikat, UploadDocument
# Register your models here.


@admin.register(KawasanBerikat)
class KawasanBerikatAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadDocument)
class UploadDocumentAdmin(admin.ModelAdmin):
    pass
