from django.db import models


class Taxonomy(models.Model):
    name = models.CharField(max_length=100)
    # Other shit here about, e.g.
    # Whether terms may overlap
    # Whether there is hierarcy
    # etc.


class Term(models.Model):
    taxonomy = models.ForeignKey(Taxonomy)
    name = models.CharField(max_length=100)
