from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from designer.models import Designer

class HomeView(TemplateView):
    """
    This is the home page and will typically live at /
    """
    model = Designer
    template_name = 'promotions/home.html'

    # @vivek: Created context to show on the first page 
    # so created context for designer
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context['name'] = self.name
        # context['image'] = self.profile_pic
        context['designers'] = Designer.objects.all()
        #context['count']=Designer.objects.count()
        return context

class RecordClickView(RedirectView):
    """
    Simple RedirectView that helps recording clicks made on promotions
    """
    permanent = False
    model = None

    def get_redirect_url(self, **kwargs):
        try:
            prom = self.model.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExist:
            return reverse('promotions:home')

        if prom.promotion.has_link:
            prom.record_click()
            return prom.link_url
        return reverse('promotions:home')
