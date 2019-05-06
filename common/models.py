from django.db import models

# Create your models here.


class AddImage(models.Model):
    image = models.ImageField(upload_to='images')

    # def save(self, *args, **kwargs):
    #     if self.id is None:
    #         saved_image = self.profile_image
    #         self.profile_image = None
    #         super(AddImage, self).save(*args, **kwargs)
    #         self.profile_image = saved_image
    #         if 'force_insert' in kwargs:
    #             kwargs.pop('force_insert')
    #
    #     super(AddImage, self).save(*args, **kwargs)