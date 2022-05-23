from django.views.generic import CreateView, ListView, TemplateView, UpdateView
import gift_listings.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class GiftCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Gift
    template_name = 'gifts/gift_reg.html'
    success_url = reverse_lazy("index")
    #Translators: This message is shown after successful gift registration
    success_message = _('Dárek zapsán!')

class GiftUpdateView(PermissionRequiredMixin, UpdateView):
    fields = ['name', 'description', 'wished_by', 'link', 'status_choices']

class GiftListView(ListView):
    model = models.Gift
    template_name = 'gifts/gift_list.html'