from django.contrib import admin

#-------Departments
from . models import Departments
admin.site.register(Departments)

#----------Main Services of Each Departments  
from . models import Main_Services
admin.site.register(Main_Services)

#--------Sub Services of Each Main Services
from . models import Sub_Services
admin.site.register(Sub_Services)

#----------- Technologies for each Main Services
from . models import Technologies
admin.site.register(Technologies)

#-------------about Adwait
from . models import About_Us
admin.site.register(About_Us)

#-------Inquiries
from . models import Inquiries
admin.site.register(Inquiries)

#--------Customer
from . models import Customers
admin.site.register(Customers)

#----------Testimonials
from . models import Testimonials
admin.site.register(Testimonials)

#-------------Industries
from . models import Industries
admin.site.register(Industries)

#------------Blogs
from . models import Blogs
admin.site.register(Blogs)

#------------Contact
from . models import Contact
admin.site.register(Contact)