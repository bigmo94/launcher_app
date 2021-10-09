from django.db import models

from devices.models import Device


class Message(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50, blank=False, null=False)
    body = models.TextField(verbose_name="Body", blank=False, null=False)
    picture = models.ImageField(verbose_name="Message Picture", )
    created_time = models.DateField(verbose_name="Created Time", auto_now_add=True)
    updated_time = models.DateField(verbose_name="Updated Time", auto_now=True)

    class Meta:
        db_table = 'message'
        verbose_name = 'message'
        verbose_name_plural = 'admin_messages'


class Receiver(models.Model):
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    read = models.BooleanField(verbose_name="Read Status", default=False)
    created_time = models.DateField(verbose_name="Created Time", auto_now_add=True)
    updated_time = models.DateField(verbose_name="Updated Time", auto_now=True)
