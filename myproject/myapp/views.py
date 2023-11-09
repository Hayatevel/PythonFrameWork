from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import PhotoLibrary

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
    
class PortFolioView(ListView):
    template_name = 'portfolio.html'
    queryset = PhotoLibrary.objects.order_by('id')
    
    def get_image(self, request):
        images = PhotoLibrary.objects.all()
        return render(request, self.template_name, {'images': images})
    
    
