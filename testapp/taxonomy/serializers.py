from rest_framework import serializers
from taxonomy.models import Taxonomy, Term


class TaxonomySerializer(serializers.Serializer):
    class Meta:
        model = Taxonomy
        fields = ('id', 'name')


class TermSerializer(serializers.Serializer):
    class Meta:
        model = Term
        fields = ('id', 'name', 'taxonomy')
