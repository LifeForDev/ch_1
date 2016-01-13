from django.conf.urls import patterns, url

from .views import LeadsList, LeadAdd

urlpatterns = patterns(
    '',
    url(r'^add/$', LeadAdd.as_view(), name='lead-add'),
    url(r'^$', LeadsList.as_view(), name='leads-list'),
)
