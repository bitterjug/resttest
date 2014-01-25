from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Taxonomy(models.Model):
    name = models.CharField(
            max_length=100,
            unique=True)
    # Other shit here about, e.g.
    # Whether terms may overlap
    # Whether there is hierarcy
    # etc.

    def __str__(self):
        """String represenation """
        return self.name


@python_2_unicode_compatible
class Term(models.Model):
    class Meta:
        unique_together = ('name', 'taxonomy')

    taxonomy = models.ForeignKey(Taxonomy)
    name = models.CharField(max_length=100)

    def __str__(self):
        """String represenation """
        return self.name
