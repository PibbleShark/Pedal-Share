from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..user_profile import models as user_model


class Equipment(models.Model):
    """Model for users to show details about their gear."""
    user = models.ForeignKey(user_model.CustomUser, on_delete=models.CASCADE)
    device_name = models.CharField(_('device name'), max_length=115)
    type = models.CharField(_('primary device type'), max_length=20)
    secondary_type = models.CharField(_('secondary type (optional)'),
                                      max_length=20,
                                      blank=True)
    description = models.TextField(_('describe your device'), default="")
    weekly_cost = models.DecimalField(_('set your price per week'), max_digits=6, decimal_places=2)
    replacement_cost = models.DecimalField(_('how much to replace your pedal if it is lost or broken\n'
                                             'the renter will be charges this amount '
                                             'if the pedal is not safely returned\n'
                                             '(if your amount is outrageous, '
                                             'you may have more difficulty finding renters)'),
                                           max_digits=6, decimal_places=2
                                           )
    image = models.ImageField(
        _('upload an image'),
        upload_to='images/',
        blank=True)


