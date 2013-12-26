from django.conf.urls import patterns, include, url
from rest_framework import routers
from moneymaker import views

router = routers.DefaultRouter()
router.register(r'outcome', views.OutcomeViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'outcomecategory', views.OutcomeCategoryViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
