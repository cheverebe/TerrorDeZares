from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, ListView, FormView, CreateView
from TerrorDeZares.forms import FileForm
from TerrorDeZares.models import Request, PostedFile


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        req = Request.objects.create()
        if len(self.request.GET.keys()):
            context['get'] = ", ".join([key + " - " + self.request.GET[key] for key in self.request.GET.keys()])
            req.get = context['get']
        if len(self.request.POST.keys()):
            context['post'] = ", ".join([key + " - " + self.request.POST[key] for key in self.request.POST.keys()])
            req.post = context['post']
        req.save()
        return context


class All(ListView):
    template_name = 'all.html'
    model = Request


class PostFile(CreateView):
    form_class = FileForm
    template_name = 'postfile.html'

    def get_success_url(self):
        return reverse('allfiles')


class AllFiles(ListView):
    template_name = 'all_files.html'
    model = PostedFile