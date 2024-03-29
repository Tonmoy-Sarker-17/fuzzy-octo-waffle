from django.db import models

# Create your models here.

class MyModel(models.Model):
    auto_field=models.AutoField(primary_key=True)
    # big_auto_field=models.BigAutoField(primary_key=True)
    big_integer_field=models.BigIntegerField()
    binary_field=models.BinaryField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField()
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField()
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()
    

