from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        urlpatterns=['admin/', 'doc/', 'gateway/']
        for module in settings.MODULES:
            urlpatterns += ['{}/'.format(module)]
        context['urls'] = urlpatterns

        return context