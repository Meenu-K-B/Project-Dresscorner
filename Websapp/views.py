from django.shortcuts import render,redirect

from Kidapp.models import ProductDb,CategoryDb
from Websapp.models import ContactDb
from Websapp.models import RegisterDb
from Websapp.models import CartDb,OrderDb
from django.contrib import messages
import razorpay

# Create your views here.
def index(request):
    Categories = CategoryDb.objects.all
    Cartitem = CartDb.objects.filter(Username=request.session['Name'])
    x = Cartitem.count()
    return render(request,"Windex.html",{'Categories':Categories,'x':x})
def Productpage(request):
    Products = ProductDb.objects.all()
    return render(request,"Products.html",{'Products':Products})
def Productfilteredproducts(request,Ca_name):
    data = ProductDb.objects.filter(Product_Category=Ca_name)
    return render(request, "filteredproduct.html",{'data':data})
def Contact(request):
    return render(request, "Contact.html")
def Save_Contact(request):
    if request.method == "POST":
        d = request.POST.get('Name')
        a = request.POST.get('Email')
        b = request.POST.get('Contact')
        c = request.POST.get('Message')
        obj = ContactDb(Email=a,Contact=b,Message=c,Name=d)
        obj.save()
        return redirect(Contact)
def About_page(request):
    return render(request, "About.html")
def Blog_page(request):
    return render(request, "Blog.html")
def Singleproductpage(request,pro_id):
    data = ProductDb.objects.get(id=pro_id)
    return render(request,"Singleproduct.html",{'data':data})
def Login_pages(request):
    return render(request,"Login.html")
def Signup_page(request):
    return render(request,"Signup.html")
def Save_Signup(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('mobile')
        c = request.POST.get('email')
        d = request.POST.get('pass')
        e = request.POST.get('re_pass')

        obj = RegisterDb(Name=a,Mobile=b,Email=c,Password=d,CPassword=e)
        if RegisterDb.objects.filter(Username=a).exists():
            messages.warning(request,"User already exists...!")
            return redirect(Signup_page)
        elif RegisterDb.objects.filter(Email=c).exists():
            messages.warning(request,"Email address already exist..")
            return redirect(Signup_page)
        obj.save()
        messages.success(request, "User registered Successfully")
        return redirect(Signup_page)
def User_login(request):
    if request.method=="POST":
        un = request.POST.get('your_name')
        pswd = request.POST.get('your_pass')
        if RegisterDb.objects.filter(Name=un,Password=pswd).exists():
            request.session['Name'] = un
            request.session['Password'] = pswd
            messages.success(request, "Welcome..!")
            return redirect(index)
        else:
            messages.error(request,"Invalid username or Password...!")
            return redirect(Login_pages)
    else:
        messages.success(request,".Successfully.logged out...!")
        return redirect(Login_pages)
def User_logout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(User_login)
def Save_Cart(request):
    if request.method == "POST":
        a = request.POST.get('Username')
        b = request.POST.get('Productname')
        c = request.POST.get('Quantity')
        d = request.POST.get('Totalprice')
        e = request.POST.get('price')
        try:
            Product_img = ProductDb.objects.get(Product_Name=b)
            img = Product_img.Image1
        except ProductDb.DoesNotExist:
            img = None
        obj = CartDb(Username=a,ProductName=b,Quantity=c,TotalPrice=d,Price=e,Prod_Image=img)
        obj.save()
        return redirect(index)
def Cartpage(request):
    Cartitem = CartDb.objects.filter(Username=request.session['Name'])
    subtotal = 0
    shipping_amount = 0
    total_amount = 0
    for i in Cartitem:
        subtotal = subtotal + i.TotalPrice
        if subtotal > 50000:
            shipping_amount = 100
        else:
            shipping_amount = 250
        total_amount = shipping_amount + subtotal

    return render(request, "Cart.html", {'Cartitem': Cartitem, 'subtotal': subtotal, 'shipping_amount': shipping_amount,
                                         'total_amount': total_amount})
def Removecart(request,Cart_id):
    s = CartDb.objects.filter(id=Cart_id)
    s.delete()
    return redirect(Cartpage)
def Checkoutpage(request):
    Carts = CartDb.objects.filter(Username=request.session['Name'])
    subtotal = 0
    shipping_amount = 0
    total_amount = 0
    for t in Carts:
        subtotal = subtotal + t.TotalPrice
        if subtotal > 50000:
            shipping_amount = 100
        else:
            shipping_amount = 250
        total_amount = shipping_amount+subtotal
    return render(request,"Checkout.html",{'Carts':Carts,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount})

def Save_BillingDetails(request):
    if request.method == "POST":
        M = request.POST.get('name')
        i = request.POST.get('email')
        a = request.POST.get('place')
        s = request.POST.get('contact')
        r = request.POST.get('address')
        v = request.POST.get('total')
        d = request.POST.get('state')
        t = request.POST.get('pin')
        h = request.POST.get('messages')

        obj = OrderDb(Name=M, Email=i, Place=a, Address=r, Mobile=s,State=d,Pin=t,TotalPrice=v,Messages=h)
        obj.save()
        return redirect(Checkoutpage)
def Paymentpage(request):
    customer =OrderDb.objects.order_by('-id').first()
    pay = customer.TotalPrice
    amount = int(pay*100)
    pay_str = str(amount)
    for i in pay_str:
        print(i)
    if request.method == "POST":
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_jRkTOp2nyDmNrX','tORMhtYiNKIeQaKzfxBiBLnO'))
            payment = client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"Payment.html",{'customer':customer,'pay_str':pay_str})