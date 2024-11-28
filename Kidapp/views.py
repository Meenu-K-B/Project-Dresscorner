from django.shortcuts import render,redirect
from Kidapp.models import CategoryDb
from Kidapp.models import ProductDb
from Websapp.models import ContactDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django import views
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import datetime
from django.contrib import messages
def indexpage(request):
    date = datetime.datetime.now()
    return render(request,"index.html",{'date':date})
def AddCategory(req):
    return render(req,"AddCategory.html")
def Save_Category(req):
    if req.method == "POST":
        a = req.POST.get('Cname')
        b = req.FILES['image']
        c = req.POST.get('Description')
        obj = CategoryDb(Catname=a,Image=b,Description=c)
        obj.save()
        return redirect(AddCategory)
def DisplayCat(req):
    data = CategoryDb.objects.all()
    return render(req,"DisplayCat.html",{'data':data})
def EditCat(req,cat_id):
    dat = CategoryDb.objects.get(id=cat_id)
    return render(req,"EditCategory.html",
    {'dat':dat})
def deleteCat(request,cat_id):
    x= CategoryDb.objects.filter(id=cat_id)
    x.delete()
    return redirect(DisplayCat)
def Update_Category(request,cat_id):
    if request.method == "POST":
        cat = request.POST.get('Cname')
        desc = request.POST.get('Description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=cat_id).Image
        CategoryDb.objects.filter(id=cat_id).update(Catname=cat,Description=desc,Image=file)
        return redirect(DisplayCat)
def Addproduct(req):
    cat = CategoryDb.objects.all()
    return render(req,"Addproduct.html",{'cat':cat})
def Saveproduct(request):
    if request.method == "POST":
        aa = request.POST.get('Cname')
        ba = request.POST.get('Pname')
        ca = request.POST.get('Quantity')
        da = request.POST.get('Price')
        ea = request.POST.get('Description')
        fa = request.POST.get('Country')
        ga = request.POST.get('Manufacture')
        ha = request.FILES['image1']
        ia = request.FILES['image2']
        ja = request.FILES['image3']
        obj = ProductDb(Product_Category=aa,Product_Name=ba,Quantity=ca,MRP=da,Description=ea,Country=fa,Manufactured=ga,Image1=ha,Image2=ia,Image3=ja)
        obj.save()
        return redirect(Addproduct)
def display_Product(req):
    datas = ProductDb.objects.all()
    return render(req,"DisplayProduct.html",
                  {'datas':datas})
def EditProduct(req,dat_id):
    dataa = ProductDb.objects.get(id=dat_id)
    return render(req,"Edit_Product.html",
    {'dataa':dataa})
def deleteProduct(request,pro_id):
    y= ProductDb.objects.filter(id=pro_id)
    y.delete()
    return redirect(display_Product)
def Update_Product(request,P_id):
    if request.method == "POST":
        ab = request.POST.get('Cname')
        bb = request.POST.get('Pname')
        cb = request.POST.get('Quantity')
        db = request.POST.get('Price')
        eb = request.POST.get('Description')
        fb = request.POST.get('Country')
        gb = request.POST.get('Manufacture')
        try:
            img = request.FILES['image1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file1 = ProductDb.objects.get(id=P_id).Image1
        try:
            imgs = request.FILES['image2']
            fci = FileSystemStorage()
            file2 = fci.save(imgs.name, imgs)
        except MultiValueDictKeyError:
            file2 = ProductDb.objects.get(id=P_id).Image2
        try:
            imggs = request.FILES['image3']
            ffc = FileSystemStorage()
            file3 = ffc.save(imgs.name, imggs)
        except MultiValueDictKeyError:
            file3 = ProductDb.objects.get(id=P_id).Image3
        ProductDb.objects.filter(id=P_id).update(Product_Category=ab,Product_Name=bb,Quantity=cb,MRP=db,Description=eb,Country=fb,Manufactured=gb,Image1=file1,Image2=file2,Image3=file3)
        return redirect(display_Product)
def loginpage(request):
    return render(request,"login_index.html")
def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pswd)
            if user is not None:
                login(request, user)
                request.session['username']=un
                request.session['password']=pswd
                messages.success(request, "Welcome..!")
                return redirect(indexpage)
            else:
                messages.error(request, "Incorrect Password..")
                return redirect(loginpage)
        else:
            messages.warning(request, "Invalid username")
            return redirect(loginpage)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def Display_contact(req):
    data = ContactDb.objects.all()
    return render(req,"Displaycontact.html",
                  {'data':data})
def DeleteContact(req,Con_id):
    x = ContactDb.objects.filter(id=Con_id)
    x.delete()
    return redirect(Display_contact)