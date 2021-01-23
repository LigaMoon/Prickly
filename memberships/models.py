from django.db import models

from checkout.models import DeliveryType

# Add for clean method to add custom validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Membership(models.Model):
    """
    Creates a membership type model containing details
    of each different membership
    """
    HIGH = 'High'
    MEDIUM = 'Med'
    LOW = 'Low'
    PRIORITY = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    name = models.CharField(max_length=50)
    pic = models.ImageField('Membership Picture', null=True, blank=True)
    free_delivery = models.ForeignKey(DeliveryType, on_delete=models.CASCADE,
                                      null=True, blank=True)
    first_order_disc = models.IntegerField('First Order Discount', default=0)
    overall_discount = models.IntegerField(default=0)
    priority = models.CharField(max_length=10,
                                choices=PRIORITY,
                                help_text=('Priority of announcements'))
    q_gift = models.CharField('Quarterly Gift', max_length=50,
                              null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Raise a validation error if user entered first order discount,
        overall discount or price below 0
        """
        if self.price and self.price < 0:
            raise ValidationError(_("Price can't be negative"))
        elif self.first_order_disc and self.first_order_disc < 0:
            raise ValidationError(_("First Order Discount"
                                    " Value can't be negative"))
        elif self.overall_discount and self.overall_discount < 0:
            raise ValidationError(_("Overall Discount"
                                    " Value can't be negative"))
