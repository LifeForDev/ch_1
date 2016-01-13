from django.views.generic import TemplateView
from django.views.generic import CreateView

from .models import Lead
from .forms import LeadForm


class LeadsList(TemplateView):
    template_name = 'leads/list.html'


class LeadAdd(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/create.html'

