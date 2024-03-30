from .models import Image, UploadedImage
from django.contrib import admin
from .models import User
admin.site.register(User),
admin.site.register(Image)
admin.site.register(UploadedImage)