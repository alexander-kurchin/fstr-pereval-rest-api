from django.db import models


class Users(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronym = models.CharField(max_length=255)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Pereval(models.Model):
    STATUS = [('new', 'new'),
              ('pending', 'pending'),
              ('accepted', 'accepted'),
              ('rejected', 'rejected')]

    status = models.CharField(choices=STATUS,
                              max_length=10,
                              default='new')
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users,
                             on_delete=models.SET_NULL,
                             null=True)
    coord_id = models.ForeignKey(Coords,
                                 on_delete=models.CASCADE)
    level_winter = models.CharField(max_length=5)
    level_spring = models.CharField(max_length=5)
    level_summer = models.CharField(max_length=5)
    level_autumn = models.CharField(max_length=5)


class Image(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.BinaryField()


class PerevalImage(models.Model):
    pereval = models.ForeignKey(Pereval,
                                on_delete=models.CASCADE,
                                related_name='images')
    image = models.ForeignKey(Image,
                              on_delete=models.CASCADE)
