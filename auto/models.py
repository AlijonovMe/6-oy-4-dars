from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
