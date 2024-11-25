from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.contrib.staticfiles.finders import find
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.db.models import Count
from django.db import connection
from .forms import LoginForm, ChangePasswordForm, ContactEditForm, MainServicesAddForm, MainServicesEditForm, SubServicesAddForm, SubServicesEditForm, BlogAddForm, BlogEditForm, TechnologiesAddForm, TechnologiesEditForm, PortfolioForm, PortfolioUploadForm, InquiriesEditForm, CustomerForm, DeveloperForm
from django.contrib.auth.models import auth
from .models import Contact, Main_Services, Sub_Services, Departments, Blogs, Technologies, Technologies_Service, Portfolio, Portfolio_Uploads, Inquiries, Customers, Developers
from django.contrib.auth import authenticate, login, update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib import messages

def favicon(request):
    icon_path = find('img/favicon.ico')
    if icon_path:
        with open(icon_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/x-icon')
    else:
        return HttpResponse(status=404)

#login user
def my_login(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
              login(request, user)
              return redirect("dashboard")
           else:
            # Handle authentication failure with display an error message
            error_message = "Invalid username or password. Please try again."
            context = {'error_message': error_message}
            return render(request, 'adwaitapp/login.html', context=context)
    context = {'form':form}
    return render(request, 'adwaitapp/login.html', context=context)

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        print(form)
        if form.is_valid():
            print("I am inside of form is valid")
            user = form.save()
            update_session_auth_hash(request, user)  # Important to maintain the user's session
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            print("I am out side so form is not valid")
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'adwaitapp/password.html', {'form': form})


#Dashboard___________________
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'adwaitapp/dashboard.html')

#ContactUs____________________
@login_required(login_url='login')
def contact(request):
    
    contact = Contact.objects.get(id=1)
    form = ContactEditForm(instance=contact)
    if request.method == 'POST':
        form = ContactEditForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            messages.success(request, "Your contact record was Updated!")
            return redirect("contact")
        else:
         messages.error(request, "Something is wrong, Please try again!!")
         print("Form errors:", form.errors)

    context = {'form': form, 'contact': contact}
    return render(request, 'adwaitapp/contact.html', context=context)

# Main Services____________
@login_required(login_url='login')
def main_service(request):
   ser = Main_Services.objects.all().order_by('-id')
   dep = Departments.objects.all()
   paginator = Paginator(ser,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {'services': page_obj, 'is_edit': False, 'dep': dep, }
   return render(request, 'adwaitapp/main_service.html', context=context)

@login_required(login_url='login')
def main_service_add(request):
    form = MainServicesAddForm()
    if request.method == 'POST':
        form = MainServicesAddForm(request.POST, request.FILES)
        if form.is_valid():
            ser_form = form.save(commit=False)
            ser_form.content = request.POST.get('content', '')
            ser_form.save()
            messages.success(request, "Your record was created!")
            return redirect('main_service') 
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors)
    else:
        form = MainServicesAddForm()
        print("Form errors:", form.errors)
    departments = Departments.objects.all()
    context = {'form': form, 'departments': departments, 'is_edit': False}
    return render(request, 'adwaitapp/main_service.html', context=context)

@login_required(login_url='login')
def main_service_edit(request, pk):
    
    ser = Main_Services.objects.get(id=pk)
    form = MainServicesEditForm(instance=ser)
    if request.method == 'POST':
        form = MainServicesEditForm(request.POST, request.FILES, instance=ser)
        if form.is_valid():
            ser_form = form.save(commit=False)
            ser_form.content = request.POST.get('content', '')
            ser_form.save()
            messages.success(request, "Your record was Updated!")
            return redirect("main_service")
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors) 
    else:
        form = MainServicesEditForm(instance=ser)
    services = Main_Services.objects.all().order_by('-id')

    paginator = Paginator(services,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dep = Departments.objects.all()
    context = {'form': form, 'is_edit': True, 'service': ser, 'services': page_obj, 'dep': dep }
    return render(request, 'adwaitapp/main_service.html', context=context)

@login_required(login_url='login')
def main_service_delete(request, pk):
    ser = Main_Services.objects.get(id=pk)
    ser.delete()
    messages.success(request, "Record was Deleted!")
    return redirect("main_service")

# Sub Services____________
@login_required(login_url='login')
def sub_service(request):
   ser = Sub_Services.objects.all().order_by('-id')
   main = Main_Services.objects.all()
   paginator = Paginator(ser,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {'services': page_obj, 'is_edit': False, 'main': main, }
   return render(request, 'adwaitapp/sub_service.html', context=context)

@login_required(login_url='login')
def sub_service_add(request):
    form = SubServicesAddForm()
    if request.method == 'POST':
        form = SubServicesAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect('sub_service') 
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors)
    else:
        form = SubServicesAddForm()
        print("Form errors:", form.errors)
    main = Main_Services.objects.all()
    context = {'form': form, 'main': main, 'is_edit': False}
    return render(request, 'adwaitapp/sub_service.html', context=context)

@login_required(login_url='login')
def sub_service_edit(request, pk):
    
    ser = Sub_Services.objects.get(id=pk)
    form = SubServicesEditForm(instance=ser)
    if request.method == 'POST':
        form = SubServicesEditForm(request.POST, request.FILES, instance=ser)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was Updated!")
            return redirect("sub_service")
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors) 
    else:
        form = SubServicesEditForm(instance=ser)
    services = Sub_Services.objects.all().order_by('-id')

    paginator = Paginator(services,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    main = Main_Services.objects.all()
    context = {'form': form, 'is_edit': True, 'service': ser, 'services': page_obj, 'main': main }
    return render(request, 'adwaitapp/sub_service.html', context=context)

@login_required(login_url='login')
def sub_service_delete(request, pk):
    ser = Sub_Services.objects.get(id=pk)
    ser.delete()
    messages.success(request, "Record was Deleted!")
    return redirect("sub_service")


# Technologies____________
@login_required(login_url='login')
def technologies(request):
   tech = Technologies.objects.all().order_by('-id')
   main = Main_Services.objects.all()
   paginator = Paginator(tech,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {'technologies': page_obj, 'is_edit': False, 'main': main, }
   return render(request, 'adwaitapp/technologies.html', context=context)

@login_required(login_url='login')
def technologies_add(request):
    if request.method == 'POST':
        form = TechnologiesAddForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            icon = form.cleaned_data['icon']
            service_ids = form.cleaned_data['main_services']
            
            tech = Technologies.objects.create(
                name=name,
                icon=icon
            )
            for service_id in service_ids:
                Technologies_Service.objects.create(
                    technologies=tech,
                    main_services_id=service_id.id
                )

            tech.save()
            tech.icon.save(icon.name, icon)

            messages.success(request, "Your records were created!")  
            return redirect("technologies") 
        else:
            messages.error(request, "Something is wrong, Please try again!")
            print("Form errors:", form.errors)
            print("Icon errors:", form.errors.get('icon'))
    else:
        form = TechnologiesAddForm()
        print("Form errors:", form.errors)
    
    context = {'form': form, 'is_edit': False}
    return render(request, 'adwaitapp/technologies.html', context=context)

@login_required(login_url='login')
def technologies_edit(request, pk):
    technology = Technologies.objects.filter(id=pk).first()
    form = None
    existing_services = []
    all_services = []
    if technology:

        if request.method == 'POST':
                form = TechnologiesEditForm(request.POST, request.FILES, instance=technology)
                if form.is_valid():
                    technology = form.save(commit=False)

                    technology.save()

                    selected_services = form.cleaned_data.get('main_services', [])
                    Technologies_Service.objects.filter(technologies_id=technology).delete()

                    for service in selected_services:
                        Technologies_Service.objects.create(
                            technologies_id=technology.id,
                            main_services_id=service.id 
                        )
                
                    messages.success(request, "Your record was updated!")
                    return redirect("technologies")
                else:
                    messages.error(request, "Something is wrong, Please try again!")
                    print("Form errors:", form.errors)
        else:
            form = TechnologiesEditForm(instance=technology)
            existing_services = list(Technologies_Service.objects.filter(technologies_id=pk).values_list('main_services', flat=True))
            existing_services = [int(service_id) for service_id in existing_services]  # Convert to integers
            all_services = Main_Services.objects.all()

    tech = Technologies.objects.all().order_by('-id')
    main = Main_Services.objects.all()

    paginator = Paginator(tech,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'is_edit': True, 'technology': technology, 'technologies': page_obj, 'main': main, 'existing_services': existing_services, 'all_services': all_services }
    return render(request, 'adwaitapp/technologies.html', context=context)

@login_required(login_url='login')
def technologies_delete(request, pk):
    tech = Technologies.objects.get(id=pk)
    tech.delete()
    messages.success(request, "Record was Deleted!")
    return redirect("technologies")


#Blogs______________
@login_required(login_url='login')
def blogs(request):
   blog = Blogs.objects.filter(status=1).order_by('-id')
   dep = Departments.objects.all()
   main = Main_Services.objects.all()

   paginator = Paginator(blog,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {'blogs': page_obj, 'is_edit': False, 'dep': dep, 'main': main }
   return render(request, 'adwaitapp/blogs.html', context=context)

@login_required(login_url='login')
def blogs_add(request):
    form = BlogAddForm()
    if request.method == 'POST':
        form = BlogAddForm(request.POST, request.FILES)
        if form.is_valid():
            blog_form = form.save(commit=False)
            blog_form.status = 1
            blog_form.save()
            messages.success(request, "Your record was created!")
            return redirect('blogs')
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors)
    else:
        form = BlogAddForm()
        print("Form errors:", form.errors)
    dep = Departments.objects.all()
    main = Main_Services.objects.all()
    context = {'form': form, 'dep': dep, 'main': main , 'is_edit': False}
    return render(request, 'adwaitapp/blogs.html', context=context)

@login_required(login_url='login')
def blogs_edit(request, pk):
    
    blog = Blogs.objects.get(id=pk)
    form = BlogEditForm(instance=blog)
    if request.method == 'POST':
        form = BlogEditForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was Updated!")
            return redirect("blogs")
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors) 
    else:
        form = BlogEditForm(instance=blog)
    blogs = Blogs.objects.filter(status=1).order_by('-id')

    paginator = Paginator(blogs,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dep = Departments.objects.all()
    main = Main_Services.objects.all()
    context = {'form': form, 'is_edit': True, 'blog': blog, 'blogs': page_obj, 'dep': dep, 'main': main }
    return render(request, 'adwaitapp/blogs.html', context=context)

@login_required(login_url='login')
def blogs_delete(request, pk):
    emp = Blogs.objects.get(id=pk)
    emp.delete()
    messages.success(request, "Record was Deleted!")
    return redirect("blogs")

#Portfolio______________
@login_required(login_url='login')
def portfolio(request):
   portfolio = Portfolio.objects.filter(status=1).order_by('-id')
   dep = Departments.objects.all()

   paginator = Paginator(portfolio,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {'portfolios': page_obj, 'is_edit': False, 'dep': dep }
   return render(request, 'adwaitapp/portfolio.html', context=context)

@login_required(login_url='login')
def portfolio_add(request):
    form = PortfolioForm()
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_form = form.save(commit=False)
            portfolio_form.status = 1
            portfolio_form.save()

            for upload in request.FILES.getlist('files'):
                portfolio_upload = Portfolio_Uploads(portfolio=portfolio_form, user=request.user)
                portfolio_upload.files = upload  
                portfolio_upload.save()

            messages.success(request, "Your record was created!")
            return redirect('portfolio')
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors)
    else:
        form = PortfolioForm()
        print("Form errors:", form.errors)
    dep = Departments.objects.all()
    context = {'form': form, 'dep': dep, 'is_edit': False}
    return render(request, 'adwaitapp/portfolio.html', context=context)

@login_required(login_url='login')
def portfolio_edit(request, pk):
    
    portfolio = Portfolio.objects.get(id=pk)
    uploads = Portfolio_Uploads.objects.filter(portfolio_id=portfolio.id)
    form = PortfolioForm(instance=portfolio)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.status = 1
            portfolio.save()

            for upload in request.FILES.getlist('files'):
                Portfolio_Uploads.objects.create(
                    portfolio=portfolio,
                    files=upload,
                    user=request.user 
            )
            messages.success(request, "Your record was Updated!")
            return redirect("portfolio")
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors) 
    else:
        form = PortfolioForm(instance=portfolio)

    portfolios = Portfolio.objects.filter(status=1).order_by('-id')

    paginator = Paginator(portfolios,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dep = Departments.objects.all()
    context = {'form': form, 'is_edit': True, 'portfolio': portfolio, 'portfolios': page_obj, 'dep': dep , 'uploads': uploads }
    return render(request, 'adwaitapp/portfolio.html', context=context)

@login_required(login_url='login')
def portfolio_img_delete(request, pk):
    try:
        port = Portfolio_Uploads.objects.get(id=pk)
        port.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@login_required(login_url='login')
def portfolio_delete(request, pk):
    port = Portfolio.objects.get(id=pk)
    port.delete()
    messages.success(request, "Record was Deleted!")
    return redirect("portfolio")

@login_required(login_url='login')
def inquiry(request):
    inq = Inquiries.objects.all().order_by('-id')
    paginator = Paginator(inq,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'inquiries': page_obj, 'is_edit': False }
    return render(request, 'adwaitapp/inquiry.html', context=context)

@login_required(login_url='login')
def inquiry_edit(request, pk):
    inq = Inquiries.objects.get(id=pk)
    form = InquiriesEditForm(instance=inq)
    if request.method == 'POST':
        form = InquiriesEditForm(request.POST, instance=inq)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was Updated!")
            return redirect("inquiry")
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors) 
    else:
        form = InquiriesEditForm(instance=inq)
    inquiries = Inquiries.objects.all().order_by('-id')

    paginator = Paginator(inquiries,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'is_edit': True, 'inquiry': inq, 'inquiries': page_obj }
    return render(request, 'adwaitapp/inquiry.html', context=context)

#Customers______________
@login_required(login_url='login')
def customers(request):
   customers = Customers.objects.filter(status=1).order_by('-id')

   paginator = Paginator(customers,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {'customers': page_obj, 'is_edit': False }
   return render(request, 'adwaitapp/customers.html', context=context)

@login_required(login_url='login')
def customers_add(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            cust_form = form.save(commit=False)
            cust_form.status = 1
            cust_form.save()
            messages.success(request, "Your record was created!")
            return redirect('customers')
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors)
    else:
        form = CustomerForm()
        print("Form errors:", form.errors)
    context = {'form': form, 'is_edit': False}
    return render(request, 'adwaitapp/customers.html', context=context)

@login_required(login_url='login')
def customers_edit(request, pk):
    
    cust = Customers.objects.get(id=pk)
    form = CustomerForm(instance=cust)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=cust)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was Updated!")
            return redirect("customers")
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors) 
    else:
        form = CustomerForm(instance=cust)
    customers = Customers.objects.filter(status=1).order_by('-id')

    paginator = Paginator(customers,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'is_edit': True, 'customer': cust, 'customers': page_obj }
    return render(request, 'adwaitapp/customers.html', context=context)

#Developers______________
@login_required(login_url='login')
def developers(request):
   developers = Developers.objects.all().order_by('-id')

   paginator = Paginator(developers,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   dep = Departments.objects.all()

   context = {'developers': page_obj, 'is_edit': False, 'dep': dep, 'range': range(1, 6) }
   return render(request, 'adwaitapp/developers.html', context=context)

@login_required(login_url='login')
def developers_add(request):
    form = DeveloperForm()
    if request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect('developers')
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors)
    else:
        form = DeveloperForm()
        print("Form errors:", form.errors)

    dep = Departments.objects.all()
    context = {'form': form, 'is_edit': False, 'dep': dep}
    return render(request, 'adwaitapp/developers.html', context=context)

@login_required(login_url='login')
def developers_edit(request, pk):
    
    dev = Developers.objects.get(id=pk)
    form = DeveloperForm(instance=dev)
    if request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES, instance=dev)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was Updated!")
            return redirect("developers")
        else:
            messages.error(request, "Something is wrong, Please try again!!")
            print("Form errors:", form.errors) 
    else:
        form = DeveloperForm(instance=dev)
    developers = Developers.objects.all().order_by('-id')
    dep = Departments.objects.all()

    paginator = Paginator(developers,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'is_edit': True, 'developer': dev, 'developers': page_obj, 'dep': dep}
    return render(request, 'adwaitapp/developers.html', context=context)




# - Logout
def user_logout(request):
      auth.logout(request)
      return redirect("login")