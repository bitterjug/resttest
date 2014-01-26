from rest_framework import viewsets
from taxonomy.models import Taxonomy, Term
from taxonomy.serializers import TaxonomySerializer, TermSerializer


class TaxonomyViewSet(viewsets.ModelViewSet):
    queryset = Taxonomy.objects.all()
    serializer_class = TaxonomySerializer


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
