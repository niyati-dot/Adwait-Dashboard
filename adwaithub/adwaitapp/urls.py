from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

  path('', views.dashboard, name=""),

  path('favicon.ico', views.favicon),

  path('login', views.my_login, name="login"),

  #Change Password
  path('password', views.change_password, name="password"),
  
  #Dashboard
  path('dashboard', views.dashboard, name="dashboard"),

  #ContactUs
  path('contact', views.contact, name="contact"),

  #MainServices
  path('main_service', views.main_service, name="main_service"),
  path('main_service_add', views.main_service_add, name="main_service_add"),
  path('main_service_edit/<int:pk>', views.main_service_edit, name="main_service_edit"),
  path('main_service_delete/<int:pk>', views.main_service_delete, name="main_service_delete"),

  #SubServices
  path('sub_service', views.sub_service, name="sub_service"),
  path('sub_service_add', views.sub_service_add, name="sub_service_add"),
  path('sub_service_edit/<int:pk>', views.sub_service_edit, name="sub_service_edit"),
  path('sub_service_delete/<int:pk>', views.sub_service_delete, name="sub_service_delete"),

  #Blogs
  path('blogs', views.blogs, name="blogs"),
  path('blogs_add', views.blogs_add, name="blogs_add"),
  path('blogs_edit/<int:pk>', views.blogs_edit, name="blogs_edit"),
  path('blogs_delete/<int:pk>', views.blogs_delete, name="blogs_delete"),

  #Blogs
  path('technologies', views.technologies, name="technologies"),
  path('technologies_add', views.technologies_add, name="technologies_add"),
  path('technologies_edit/<int:pk>', views.technologies_edit, name="technologies_edit"),
  path('technologies_delete/<int:pk>', views.technologies_delete, name="technologies_delete"),

  #Portfolio
  path('portfolio', views.portfolio, name="portfolio"),
  path('portfolio_add', views.portfolio_add, name="portfolio_add"),
  path('portfolio_edit/<int:pk>', views.portfolio_edit, name="portfolio_edit"),
  path('portfolio_delete/<int:pk>', views.portfolio_delete, name="portfolio_delete"),
  path('portfolio/img/delete/<int:pk>/', views.portfolio_img_delete, name="portfolio_img_delete"),

  #WebInquiry
  path('inquiry', views.inquiry, name="inquiry"),
  path('inquiry_edit/<int:pk>', views.inquiry_edit, name="inquiry_edit"),

  #Customers
  path('customers', views.customers, name="customers"),
  path('customers_add', views.customers_add, name="customers_add"),
  path('customers_edit/<int:pk>', views.customers_edit, name="customers_edit"),

  #Developers
  path('developers', views.developers, name="developers"),
  path('developers_add', views.developers_add, name="developers_add"),
  path('developers_edit/<int:pk>', views.developers_edit, name="developers_edit"),

  #Logout
  path('logout', views.user_logout, name="logout"),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)