from django.db import models
from django.contrib.auth.models import User
from PIL import Image

ROLE_CHOICES = (
    ('Teacher','TEACHER'),
    ('Representative', 'REPRESENTATIVE'),
    ('Student','STUDENT'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    valid = models.CharField(default="",max_length=4)
    district = models.CharField(default="",max_length=30)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 550 or img.width > 550:
            output_size = (550,550)
            img.thumbnail(output_size)
            img.save(self.image.path)