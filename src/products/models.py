from django.db import models
import random
import os


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 51313546541)
    ext = get_filename_ext(filename)[0]
    final_filename = f'{new_filename}{ext}'  # .format(new_filename=new_filename, ext=ext)
    return f'products/{new_filename}/{final_filename}'


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title
