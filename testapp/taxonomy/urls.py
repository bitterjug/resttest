from django.conf.urls import url, patterns, include
from rest_framework import routers
from taxonomy import views

router = routers.DefaultRouter()
router.register(r'taxonomies', views.TaxonomyViewSet)
router.register(r'terms', views.TermViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    )
)
