from django.shortcuts import render
from user.models import MyUser 
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from product.models import Category, Product
from product.forms import ProductForm

# Create your views here.
def test(request):
    return render(request,'my_admin/category.html')
def list_users(request):
    users = MyUser.objects.all()
    paginator = Paginator(users,12)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'users':page}
    return render(request,'my_admin/users.html',context)

def block_or_unblock_user(request,pk):
    user = get_object_or_404(MyUser, id=pk)
    user.is_active = not user.is_active
    messages.success(request, f'User {user.email} status changed.')
    user.save()
    return redirect('list_users') 

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        if name:
            Category.objects.create(name=name)
    categories = Category.objects.all()
    context = {'categories':categories}
    print(context)
    return render(request,'my_admin/category.html',context)


def update_category(request,pk):
    if request.method == 'POST':
        category = Category.objects.get(id=pk)
        name = request.POST.get('name')
        category.name = name
        category.save()
        return redirect('add_category')
     

def delete_category(request,pk):
    category = Category.objects.get(id=pk)
    category.inactive = not category.inactive
    category.save()
    return redirect('add_category')


def create_product(request):
    form = ProductForm()  # Initialize an empty form
    if request.method == 'POST':
        print("Inside POST")
        print("Request Files:", request.FILES)  # Debugging line
        print("Request POST Data:", request.POST)
       
        form = ProductForm(request.POST, request.FILES)  # Pass both POST and FILES for image uploads
        
        if form.is_valid():
            print("The form is valid")
            form.save()  # Save the form data to the database
        else:
            print("Form errors:", form.errors)  # Print form errors if any

    products = Product.objects.all()  # Fetch all products
    context = {
        'form': form,   # Pass the form to the template
        'products': products  # Pass the products to the template
    }
    return render(request, 'my_admin/product_list.html', context)



def update_product(request):
    pass

def delete_product(request,pk):
    pass
    