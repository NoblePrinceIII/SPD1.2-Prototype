from django.urls import path

from api.views import EntryDetail, EntryList

urlpatterns = [
    path('', EntryList.as_view(), name='polls_list'),
    path('<int:pk>', EntryDetail.as_view(), name='entry_detail')
]
