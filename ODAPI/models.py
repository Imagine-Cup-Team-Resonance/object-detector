from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO

# Create your models here.

class image(models.Model):
    object_image = models.FileField(upload_to = 'uploads/objects/')
    background_image = models.FileField(upload_to='uploads/backgrounds/')
    description = models.CharField(max_length=30)
    result_image = models.FileField(upload_to='uploads/results/', blank=True)

    def __str__(self):
        return self.description
    
    # def saveResultImage(self, result_image_detected, *args, **kwargs):

    #     buffer = BytesIO()
    #     result_image_detected.save(buffer, format='png')
    #     result_image_png = buffer.getvalue()

    #     self.result_image.save(str(self.result_image), ContentFile(result_image_png), save=False)

    #     super().save(*args, **kwargs)
