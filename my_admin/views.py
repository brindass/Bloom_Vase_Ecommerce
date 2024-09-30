from django.shortcuts import render
from user.models import MyUser 
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from product.models import Category

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
    pass

def update_product(request):
    pass

def delete_product(request,pk):
    pass
    