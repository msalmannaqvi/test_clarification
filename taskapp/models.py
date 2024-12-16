from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
from django.core.exceptions import ValidationError


# Create your models here.
class ClarificationType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Rfx(models.Model):
    rfxid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    description = models.TextField()




class ClarificationCategory(models.Model):
    clarification = models.CharField(max_length=100)

    def __str__(self):
        return self.clarification


class Assign_To(models.Model):
    assign = models.ForeignKey(User, on_delete=models.CASCADE)


class General(models.Model):
    clarificationtype = models.ForeignKey(ClarificationType, on_delete=models.CASCADE,
                                          related_name='clairifictiontype')
    rfx = models.ForeignKey(Rfx, on_delete=models.CASCADE, related_name='rfx')
    clarification = models.ForeignKey(ClarificationCategory, on_delete=models.CASCADE,
                                      related_name='clarificationcategory')
    assigned_to = models.ForeignKey(Assign_To, on_delete=models.CASCADE, related_name='assign_to')

    expires = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(General, self).__init__(*args, **kwargs)
        self.__old_expires = self.expires

    def clean(self):
        "Make sure expiry time cannot be in the past"
        if (not self.id or self.__old_expires != self.expires) and self.expires <= now():
            raise ValidationError('Entries cannot expire in the past.')

    def __str__(self):
        return f'{self.assigned_to}'


class ClarificationFiles(models.Model):
    general = models.ForeignKey(General, on_delete=models.CASCADE, related_name='general')

    files = models.FileField(upload_to='file/')
