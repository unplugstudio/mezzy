from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from mezzanine.core.models import Slugged, Orderable


@python_2_unicode_compatible
class Titled(models.Model):
    '''
    Simple titled model.
    '''
    title = models.CharField('Title', max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class TitledInline(Orderable, Titled):
    '''
    Simple inline with a title and manual sorting.
    '''
    class Meta:
        abstract = True


class SluggedInline(Orderable, Slugged):
    '''
    Simple inline with a title, a slug and manual sorting.
    '''
    class Meta:
        abstract = True
