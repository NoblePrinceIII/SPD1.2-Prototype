from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from entries.models import Entry
from api.serializers import EntrySerializer


class EntryList(APIView):
    def get(self, request):
        entries = Entry.objects.all()[:20]
        data = EntrySerializer(entries, many=True).data
        return Response(data)

class EntryDetail(APIView):
    def get(self, request, pk):
        entries = get_object_or_404(Entry, pk=pk)
        data = EntrySerializer(entries).data
        return Response(data)
