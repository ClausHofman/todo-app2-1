# API = Application Programming Interface

from rest_framework import serializers, viewsets

from .models import Tehtava

# Serializers define the API representation.
class TehtavaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tehtava
        fields = ['otsikko', 'tehty']

# ViewSets define the view behavior.
class TehtavaViewSet(viewsets.ModelViewSet):
    queryset = Tehtava.objects.all()
    serializer_class = TehtavaSerializer
