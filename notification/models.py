from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from custom_user.models import CustomUser
# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPE=("Post","Like","Follow")

    content_type=models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id=models.BigIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(
        CustomUser,
        related_name='user_notification',
        on_delete=models.CASCADE
    )
    
    text = models.CharField(max_length=200,null=True)
    is_seen = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=200,choices=list(zip(NOTIFICATION_TYPE,NOTIFICATION_TYPE)))
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
    pass