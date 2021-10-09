from django.db import models


class Application(models.Model):
    option1 = 1
    option2 = 2
    OPTION_CHOICES = (
        (option1, 'Do Somethings'),
        (option2, 'Do Somethings')
    )

    name = models.CharField(verbose_name="Name", max_length=50, blank=False, null=False)
    pkg_name = models.CharField(verbose_name="Package Name", max_length=50, blank=False, null=False)
    icon = models.ImageField(verbose_name="App Icon")
    url = models.URLField(verbose_name="App URL", blank=False, null=False)
    store_type = models.IntegerField(verbose_name="Store Type", choices=OPTION_CHOICES)
    version_number = models.IntegerField(verbose_name="Version Number")
    created_time = models.DateField(verbose_name="Created Time", auto_now_add=True)
    updated_time = models.DateField(verbose_name="Updated Time", auto_now=True)

    class Meta:
        db_table = 'applications'
        verbose_name = 'application'
        verbose_name_plural = 'applications'
