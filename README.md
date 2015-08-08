django-good-choices
===================

Simple and convenient approach to "choices" in Django

Example:

```python
from django.db import models
from django.utils.translation import ugettext_lazy as _
from good_choices import Choices

class Order(models.Model):
    class Status(Choices):
        PLACED = 1, _('Placed')
        PAID = 2, _('Paid')
        SENT = 3, _('Sent')
        DELIVERED = 4, _('Delivered')

    product = models.ForeignKey('Product')
    status = models.SmallIntegerField(
        choices=Status.choices,
        default=Status.PLACED)
```

Changelog
---------

### 1.5

* declare dependencies in the setup script

### 1.4

* fix for choices with ``None`` as a value

### 1.3

* fix name in metaclass

### 1.2

* add ``labels`` attribute

### 1.1

* implemented iterator protocol

### 1.0

* Choices class
