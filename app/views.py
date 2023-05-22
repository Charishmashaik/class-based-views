from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model = school
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=school
    context_object_name='sclobject'


class SchoolCreate(CreateView):
    model=school
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=school
    fields='__all__'


class Schooldelete(DeleteView):
    model=school
    context_object_name='schoolobject'
    success_url=reverse_lazy('SchoolList')
