from django.db import models


class service(models.Model):

    class Meta:
        verbose_name_plural = 'service'

    Service_category = models.CharField(max_length=254,)

    def __str__(self):
        return self.Service_category


class sub_Service(models.Model):

    class Meta:
        verbose_name_plural = 'sub_Service'

    Service_category = models.ForeignKey(
        'service', null=True, blank=False, on_delete=models.SET_NULL,)
    Sub_Service_name = models.CharField(max_length=254,)

    def __str__(self):
        return self.Sub_Service_name


class tasker(models.Model):

    class Meta:
        verbose_name_plural = 'tasker'

    Tasker_service_category = models.ForeignKey(
        'service', null=True, blank=False,
        on_delete=models.SET_NULL)
    tasker_services = models.ForeignKey(
        'sub_Service', null=True,
        blank=False, on_delete=models.SET_NULL)
    Name = models.CharField(max_length=254,)
    about = models.CharField(max_length=1024, blank=False,)
    Price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=2054, blank=True,
    )
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.Name
