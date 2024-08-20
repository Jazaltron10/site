from django.contrib.auth.forms import UserCreationForm  # Import Django's form to handle user creation 
from django.urls import reverse_lazy  # Import reverse_lazy to lazily reverse URL names after user actions
from django.views.generic import CreateView  # Import Django's generic CreateView to handle form submission 
from django.shortcuts import render  # Import render to return an HttpResponse that contains the rendered text (template)
from django.contrib.auth.decorators import login_required  # Import login_required to restrict access to authenticated users only

# Create your views here.

class SignUpView(CreateView):
    """
    View to handle user sign-up.
    Inherits from Django's generic CreateView, which provides the necessary methods to handle form submissions.
    """
    form_class = UserCreationForm  # Specify the form class to be used for user creation
    success_url = reverse_lazy('login')  # Redirect to the login page after a successful signup
    template_name = 'registration/signup.html'  # Specify the template to render the signup form

@login_required # Decorator to ensure that only logged-in users can access this view
def profile_view(request):
    """
    View to display the user's profile after login.
    This view is only accessible to logged-in users, enforced by the @login_required decorator.
    Renders a template that shows a welcome message to the user and provides a logout button.
    """
    return render(request, 'profile.html', {'user': request.user})  # Pass the current user to the template and render it
