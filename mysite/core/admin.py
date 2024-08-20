from django.contrib import admin  # Import Django's admin interface
from .models import Company, Department, Employee  # Import the models

admin.site.register(Company)  # Register the Company model with the admin site
admin.site.register(Department)  # Register the Department model with the admin site
admin.site.register(Employee)  # Register the Employee model with the admin site
