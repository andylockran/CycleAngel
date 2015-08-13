from django.conf.urls import url, include

from rest_framework import routers, serializers, viewsets

from wagtail.wagtailcore.fields import RichTextField

from . import views
from account.models import Item, Manufacturer, Variation

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    description = serializers.CharField()
    class Meta:
        model = Item
        fields = ('name','value','manufacturer','variation','description','transferable')

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:	
        model = Manufacturer
        fields = ('name',)

class VariationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:	
        model = Variation
        fields = ('name',)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'variations', VariationViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
