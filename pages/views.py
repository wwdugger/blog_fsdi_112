from django.views.generic import TemplateView
from posts.models import Post

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    #add the database info from ListView here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(category="Products").order_by('created_on').reverse()[0:5]
        
        return context

class AboutPageView(TemplateView):
    template_name = "pages/about.html"