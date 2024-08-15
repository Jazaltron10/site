from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Student, Course

# Create your views here.
def hello_view(request):
    """This view returns a simple greeting message."""
    return HttpResponse("Hello, World!")

def king_view(request, name):
    """This view returns a simple greeting message from king kong."""
    return HttpResponse(f"Hello, King {name}")

class WelcomeView(TemplateView):
    """This view renders a template with a greeting message"""
    template_name = 'welcome.html'

class ListView(ListView):
    """This view renders a template with a greeting message"""
    template_name = 'list.html'
    
    def get_context_data(self, **kwargs):
        """Pass a list of items to the template."""
        context = super().get_context_data(**kwargs)
        context['items'] = ['Item 1', 'Item 2', 'Item 3' ]
        return context
    
class ListStudentsView(ListView):
    model = Student
    template_name = 'liststudent.html'
    context_object_name = 'student_list'
    
class ListCoursesView(ListView): 
    model = Course
    template_name = 'listcourses.html'
    context_object_name = 'course_list'
    
class ListAllView(ListView): 
    model = Course
    template_name = 'listall.html'
    context_object_name = 'course_list'
    
