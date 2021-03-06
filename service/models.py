from django.db import models


class Service_category(models.Model):

    class Meta:
        verbose_name_plural = 'service'

    category = models.CharField(max_length=30,)
    icon = models.ImageField(blank=True)

    def __str__(self):
        return self.category


class Sub_service(models.Model):

    class Meta:
        verbose_name_plural = 'sub_Service'

    category = models.ForeignKey(
        'Service_category', null=True, blank=False, on_delete=models.SET_NULL,)
    sub_service_name = models.CharField(max_length=254,)

    def __str__(self):
        return self.sub_service_name


class Charge_type(models.Model):

    class Meta:
        verbose_name_plural = 'Charge_type'

    type = models.CharField(max_length=30,)

    def __str__(self):
        return self.type


class Tasker(models.Model):

    class Meta:
        verbose_name_plural = 'tasker'

    service_category = models.ForeignKey(
        'Service_category', null=True, blank=False,
        on_delete=models.SET_NULL)

    tasker_services = models.ForeignKey(
        'Sub_Service', null=True,
        blank=False, on_delete=models.SET_NULL)
    charge_type = models.ForeignKey(
        'Charge_type', null=True,
        blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254,)
    about = models.CharField(max_length=1024, blank=False,)
    price = models.DecimalField(
        max_digits=6, decimal_places=2,)
    image_url = models.URLField(
        max_length=10000, blank=True,
    )
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
