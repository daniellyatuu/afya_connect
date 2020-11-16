from django.shortcuts import render
from django.http import HttpResponse
from app.home.models import Posts
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404


class Home(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Afya-connect'
        context['objects'] = Posts.objects.filter(active=True)
        return render(request, self.template_name, context)


class AboutUs(View):
    template_name = 'home/about_us.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'About Us'
        return render(request, self.template_name, context)


class Team(View):
    template_name = 'home/team.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Team'
        return render(request, self.template_name, context)


class Blog(View):
    template_name = 'home/blog.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Blog'
        context['objects'] = Posts.objects.filter(active=True)
        return render(request, self.template_name, context)


class ContactUs(View):
    template_name = 'home/contact_us.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = 'Contact Us'
        return render(request, self.template_name, context)


class Artical(DetailView):
    model = Posts

    def get_object(self):
        return get_object_or_404(Posts, pk=self.kwargs['pk'], active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post'
        return context
