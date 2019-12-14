from rest_framework.serializers import ModelSerializer

from entries.models import Entry

class EntrySerializer(ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
