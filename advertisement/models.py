from django.db import models


class Advertisement(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50, blank=False, null=False)
    description = models.CharField(verbose_name="Description", max_length=250)
    avatar = models.ImageField(verbose_name="Avatar")
    url = models.URLField(verbose_name="Advertisement URL")
    pub_date = models.DateTimeField(verbose_name="Publish Date", auto_now_add=True)
    updated_time = models.DateField(verbose_name="Updated Time", auto_now=True)

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'advertisement'
        verbose_name_plural = 'advertisements'
        ordering = ['pub_date']
