from django.db import models


class Service(models.Model):
    Service_category = models.CharField(max_length=254,)

    def __str__(self):
        return self.Service_category


class Sub_Service(models.Model):
    Service_category = models.ForeignKey('Service', null=False, blank=False, on_delete=models.SET_NULL)
    Sub_Service_name = models.CharField(max_length=254,)

    def __str__(self):
        return self.Sub_Service_name


class tasker(models.Model):
    Tasker_service_category = models.ForeignKey('Service', null=False, blank=False, on_delete=models.SET_NULL)
    tasker_services = models.ForeignKey('Sub_Service', null=False, Blank=False, on_delete=models.SET_NULL)
    Name = models.CharField(max_length=254,)
    Price = models.DecimalField(max_digits=6, decimal_places=2, null=True, Blank=True)
    image_url = models.URLField(max_length=1054, null=True, Blank=True)
    image = models.ImageField(null=True, Blank=True)
    rating = models.DecimalField(max_lenth=5, decimal_places=2, null=True, Blank=True)

    def __str__(self):
        return self.Name
