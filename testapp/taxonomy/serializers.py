from rest_framework import serializers
from taxonomy.models import Taxonomy, Term


class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
