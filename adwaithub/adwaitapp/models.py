from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from datetime import datetime

#-------Departments
class Departments(models.Model):
   name = models.CharField(max_length=50)
   def __str__(self): 
     return self.name

#-------------Service content imgs
def service_upload_path(instance, filename):
   return f"uploads/service/{instance.url}/{filename}"
 
#----------Main Services of Each Departments  
class Main_Services(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   name = models.CharField(max_length=255)
   url = models.CharField(max_length=255, blank=True, null=True)
   show = models.SmallIntegerField(blank=True, null=True)
   tagline = models.TextField(blank=True, null=True)
   icon = models.CharField(max_length=50, blank=True, null=True)
   dept_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
   img = models.FileField(upload_to=service_upload_path, blank=True, null=True,max_length=255)
   content = models.TextField(blank=True, null=True)
   seo_keywords = models.TextField(blank=True, null=True)
   def __str__(self): 
     return self.name

#-------------Sub Service content imgs
def sub_service_upload_path(instance, filename):
   return f"uploads/subservice/{instance.url}/{filename}"
   
#--------Sub Services of Each Main Services
class Sub_Services(models.Model):
   name = models.CharField(max_length=255)
   url = models.CharField(max_length=255, blank=True, null=True)
   icon = models.CharField(max_length=50, blank=True, null=True)
   tagline = models.TextField(blank=True, null=True)
   main_service_id = models.ForeignKey(Main_Services, on_delete=models.CASCADE)
   img = models.FileField(upload_to=sub_service_upload_path, blank=True, null=True,max_length=255)
   content = models.TextField(blank=True, null=True)
   seo_keywords = models.TextField(blank=True, null=True)
   def __str__(self): 
     return self.name
   
#-------------Technologies icons
def technologies_upload_path(instance, filename):
   if instance.pk:
        main_service_names = [service.main_services.name for service in Technologies_Service.objects.filter(technologies=instance)]
        main_service_name = main_service_names[0] if main_service_names else "default"
        return f"uploads/technologies/{main_service_name}/{filename}"
   else:
        return f"uploads/technologies/temp/{filename}"

class Technologies(models.Model):
   name = models.CharField(max_length=255)
   icon = models.FileField(upload_to=technologies_upload_path, blank=True, null=True,max_length=255)
   def __str__(self): 
     return self.name
   
class Technologies_Service(models.Model):
   technologies = models.ForeignKey(Technologies, on_delete=models.CASCADE)
   main_services = models.ForeignKey(Main_Services, on_delete=models.CASCADE)

   def __str__(self):
        return f"{self.technologies}"
   
#-------------about content imgs
def about_upload_path(instance, filename):
   return f"uploads/about/{instance.subject}/{filename}"

#-------------about Adwait
class About_Us(models.Model):
   subject = models.CharField(max_length=255)
   description = models.TextField(blank=True, null=True)
   img = models.FileField(upload_to=about_upload_path, blank=True, null=True)
   def __str__(self): 
     return self.subject

#-------Inquiries
class Inquiries(models.Model):
   name = models.CharField(max_length=255)
   subject = models.CharField(max_length=255)
   email = models.EmailField(max_length=50, blank=True, null=True)
   message = models.TextField(blank=True, null=True)
   notes = models.TextField(blank=True, null=True)
   status = models.SmallIntegerField()
   creation_date = models.DateTimeField(default=datetime.now)
   def __str__(self): 
     return self.subject

#--------Customer Uploads
def customer_upload_path(instance, filename):
   return f"uploads/customers/{instance.name}/{filename}"

#--------Customers 
class Customers(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   name = models.CharField(max_length=255)
   business = models.SmallIntegerField(blank=True, null=True)
   company_name = models.CharField(max_length=255, blank=True, null=True)
   email = models.EmailField(max_length=50)
   phone = models.CharField(max_length=50)
   address = models.CharField(max_length=255)
   zip = models.CharField(max_length=255)
   state = models.CharField(max_length=255)
   country = models.CharField(max_length=255)
   more_info = models.TextField(blank=True, null=True)
   status = models.SmallIntegerField(blank=True, null=True)
   file = models.FileField(upload_to=customer_upload_path, blank=True, null=True)
   def __str__(self): 
     return self.name
   
#----------Testimonials
class Testimonials(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   name = models.CharField(max_length=255)
   position = models.CharField(max_length=50)
   message = models.TextField(blank=True, null=True)
   customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
   dept_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
   def __str__(self): 
      return self.name
    
#-------------Industries
class Industries(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   name = models.CharField(max_length=255)
   url = models.CharField(max_length=255)
   def __str__(self): 
     return self.name

#-------------Blog content imgs
def blog_upload_path(instance, filename):
   return f"uploads/blogs/{instance.url}/{filename}"
#------------Blogs
class Blogs(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   subject = models.CharField(max_length=255)
   url = models.CharField(max_length=255, blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   content = models.TextField(blank=True, null=True)
   tags = models.CharField(max_length=255, blank=True, null=True)
   img = models.FileField(upload_to=blog_upload_path, blank=True, null=True,max_length=255)
   status = models.SmallIntegerField(blank=True, null=True)
   dept_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
   main_service_id = models.ForeignKey(Main_Services, on_delete=models.CASCADE)
   seo_keywords = models.TextField(blank=True, null=True)
   def __str__(self): 
      return self.subject

#------------contact
class Contact(models.Model):
   location = models.CharField(max_length=255, blank=True, null=True)
   email = models.EmailField(blank=True, null=True)
   phone = models.CharField(max_length=25, blank=True, null=True)
   address = models.TextField(blank=True, null=True)
   map = models.TextField(blank=True, null=True)
   def __str__(self): 
      return self.location

#-------------Blog content imgs
def portfolio_upload_path(instance, filename):
   return f"uploads/portfolio/{instance.portfolio.url}/{filename}"
    
class Portfolio(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   title = models.CharField(max_length=255)
   url = models.CharField(max_length=255, blank=True, null=True)
   content = models.TextField(blank=True, null=True)
   tags = models.CharField(max_length=255, blank=True, null=True)
   status = models.SmallIntegerField(blank=True, null=True)
   dept_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
   def __str__(self): 
      return self.title
   
class Portfolio_Uploads(models.Model):
   portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
   files = models.FileField(upload_to=portfolio_upload_path, blank=True, null=True)
   uploaded_at = models.DateTimeField(default=datetime.now)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return f"{self.portfolio}"
   
class NewsletterSubscriber(models.Model):
   email = models.EmailField(unique=True)
   subscribed_on = models.DateTimeField(default=datetime.now)
   
   def __str__(self):
        return self.email

#--------Developers Uploads
def developer_upload_path(instance, filename):
   return f"uploads/developers/{instance.name}/{filename}"

#---------------Developers
class Developers(models.Model):
   name = models.CharField(max_length=255)
   email = models.EmailField(blank=True, null=True)
   phone = models.CharField(max_length=25, blank=True, null=True)
   country = models.CharField(max_length=25, blank=True, null=True)
   more_info = models.TextField(blank=True, null=True)
   file = models.FileField(upload_to=developer_upload_path, blank=True, null=True)
   rate = models.SmallIntegerField(blank=True, null=True)
   dept_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
   def __str__(self): 
     return self.name

class ProjectPhase(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   name = models.CharField(max_length=255)
   def __str__(self): 
     return self.name
      
#-------------Project
def project_upload_path(instance, filename):
   return f"uploads/projects/{instance.projects.dept_id}/{instance.projects.project_code}/{filename}"
    
class Projects(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   project_name = models.CharField(max_length=255)
   project_code = models.CharField(max_length=255, blank=True, null=True)
   details = models.TextField(blank=True, null=True)
   project_notes = models.CharField(max_length=255, blank=True, null=True)
   project_phase = models.ForeignKey(ProjectPhase, on_delete=models.CASCADE)
   starting_date = models.DateField(null=True, blank=True)
   deadline = models.DateField(null=True, blank=True)
   finish_date = models.DateField(null=True, blank=True)
   status = models.SmallIntegerField(blank=True, null=True)
   customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
   dept_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
   main_service_id = models.ForeignKey(Main_Services, on_delete=models.CASCADE)
   def __str__(self): 
      return self.project_name
   
class Project_Uploads(models.Model):
   project = models.ForeignKey(Projects, on_delete=models.CASCADE)
   files = models.FileField(upload_to=project_upload_path, blank=True, null=True)
   uploaded_at = models.DateTimeField(default=datetime.now)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return f"{self.project}"
   
class project_developers(models.Model):
   creation_date = models.DateTimeField(default=datetime.now)
   wage = models.FloatField(blank=True, null=True)
   hrs = models.FloatField(blank=True, null=True)
   more_info = models.TextField(blank=True, null=True)
   file = models.FileField(upload_to=project_upload_path, blank=True, null=True)
   project = models.ForeignKey(Projects, on_delete=models.CASCADE)
   developer = models.ForeignKey(Developers, on_delete=models.CASCADE)
   
   def __str__(self):
      return f"{self.project}"