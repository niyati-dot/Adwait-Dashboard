from django.contrib.auth.models import User
from multiupload.fields import MultiFileField
from django import forms
from .models import Contact, Main_Services, Sub_Services, Departments, Blogs, Technologies, Portfolio, Portfolio_Uploads, Inquiries, Customers, Developers
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, TextInput


# - Login a User
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-material'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-material'}))

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None

# Contact

class ContactEditForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['location', 'address', 'email', 'phone']
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].required = False

#Main Services__________________
#Add Service
class MainServicesAddForm(forms.ModelForm):
  class Meta:
    model = Main_Services
    fields = ['name', 'url', 'tagline', 'icon', 'img', 'dept_id', 'content', 'seo_keywords']
    widgets = {
            'tagline': forms.Textarea(attrs={'rows': 2}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['content'].required = False
      self.fields['seo_keywords'].required = False
      self.fields['img'].required = False

#Edit Services
class MainServicesEditForm(forms.ModelForm):
  class Meta:
    model = Main_Services
    fields = ['name', 'url', 'tagline', 'icon', 'img', 'dept_id', 'content', 'seo_keywords']
    widgets = {
            'tagline': forms.Textarea(attrs={'rows': 2}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['content'].required = False
      self.fields['seo_keywords'].required = False
      self.fields['img'].required = False

#Sub Services__________________
#Add Service
class SubServicesAddForm(forms.ModelForm):
  class Meta:
    model = Sub_Services
    fields = ['name', 'url', 'tagline', 'icon', 'img', 'main_service_id', 'content', 'seo_keywords']
    widgets = {
            'tagline': forms.Textarea(attrs={'rows': 2}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['content'].required = False
      self.fields['seo_keywords'].required = False
      self.fields['img'].required = False

#Edit Services
class SubServicesEditForm(forms.ModelForm):
  class Meta:
    model = Sub_Services
    fields = ['name', 'url', 'tagline', 'icon', 'img', 'main_service_id', 'content', 'seo_keywords']
    widgets = {
            'tagline': forms.Textarea(attrs={'rows': 2}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['content'].required = False
      self.fields['seo_keywords'].required = False
      self.fields['img'].required = False

#Technologies_____________
class TechnologiesAddForm(forms.ModelForm):
    class Meta:
        model = Technologies 
        fields = ['name', 'icon', 'main_services']  

    main_services = forms.ModelMultipleChoiceField(queryset=Main_Services.objects.all(), widget=forms.CheckboxSelectMultiple, required=True, label="Main Services")

class TechnologiesEditForm(forms.ModelForm):
    class Meta:
        model = Technologies 
        fields = ['name', 'icon', 'main_services']  

    main_services = forms.ModelMultipleChoiceField(queryset=Main_Services.objects.all(), widget=forms.CheckboxSelectMultiple, required=True, label="Main Services")

#Blogs__________________
#Add Blog
class BlogAddForm(forms.ModelForm):
  class Meta:
    model = Blogs
    fields = ['subject', 'url', 'description', 'content', 'tags', 'img', 'dept_id', 'main_service_id', 'seo_keywords']
    widgets = {
            'description': forms.Textarea(attrs={'rows': 2}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['content'].required = False
      self.fields['tags'].required = False
      self.fields['seo_keywords'].required = False
    

#Edit Blog
class BlogEditForm(forms.ModelForm):
  class Meta:
    model = Blogs
    fields = ['subject','url', 'description', 'content', 'tags', 'img', 'dept_id', 'main_service_id', 'seo_keywords']
    widgets = {
            'description': forms.Textarea(attrs={'rows': 4}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['content'].required = False
      self.fields['tags'].required = False
      self.fields['seo_keywords'].required = False
      self.fields['img'].required = False

#Portfolio__________________
#Add Portfolio
class PortfolioForm(forms.ModelForm):
  class Meta:
    model = Portfolio
    fields = ['title', 'url', 'content', 'tags', 'dept_id']
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['content'].required = False
      self.fields['tags'].required = False

class PortfolioUploadForm(forms.ModelForm):
  class Meta:
    model = Portfolio_Uploads
    fields = [
       'files', 
       ]
    files = MultiFileField(max_file_size=20 * 1024 * 1024)

class InquiriesEditForm(forms.ModelForm):
  class Meta:
      model = Inquiries
      fields = ['name', 'subject', 'email', 'message', 'status', 'notes']
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['status'].required = False
      self.fields['notes'].required = False
      self.fields['name'].required = False
      self.fields['subject'].required = False
      self.fields['email'].required = False
      self.fields['message'].required = False

#Customers__________________
#Add/Edit Customer
class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customers
    fields = ['name', 'business', 'company_name', 'email', 'phone', 'address', 'zip', 'state', 'country', 'more_info', 'file']
    widgets = {
            'more_info': forms.Textarea(attrs={'rows': 2}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['business'].required = False
      self.fields['company_name'].required = False
      self.fields['phone'].required = False
      self.fields['address'].required = False
      self.fields['more_info'].required = False
      self.fields['file'].required = False

#Developers__________________
#Add/Edit Developer
class DeveloperForm(forms.ModelForm):
  class Meta:
    model = Developers
    fields = ['name', 'email', 'phone', 'country', 'more_info', 'file', 'rate', 'dept_id']
    widgets = {
            'more_info': forms.Textarea(attrs={'rows': 2}) 
        }
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['more_info'].required = False
      self.fields['file'].required = False
      self.fields['rate'].required = False