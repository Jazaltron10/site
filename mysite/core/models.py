from django.db import models

# Create your models here.
class Company(models.Model):
    # Represents a Company entity
    name = models.CharField(max_length=100) # The name of the company
    location = models.CharField(max_length=100) # The location of the company
    
    def __str__(self) -> str:
        return self.name  # Returns the company name for easy identification in admin or queries
    
class Department(models.Model):
    # Represents a department within a company 
    name = models.CharField(max_length=100) # The name of the department 
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='departments'
    ) # Links to company, deletes departments if the company is deleted
    
    def __str__(self) -> str:
        return f"{self.name} - {self.company.name}"  # Returns department and company name for easy identification
    
class Employee(models.Model):
    # Represents an employee working in a department
    name = models.CharField(max_length=100) # The name of the employee
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="employees"
    ) # Links to the department, deletes employee if the department is deleted
    
    def __str__(self) -> str:
        return f"{self.name} - {self.department.name}" # Returns employee and department name for easy identification 
    

