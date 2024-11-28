from django.urls import path
from Kidapp import views
urlpatterns = [
    path('index/',views.indexpage,name="index"),
    path('Categories/',views.AddCategory,name="Categories"),
    path('SaveCategories/',views.Save_Category,name="SaveCategories"),
    path('DisplayCat/',views.DisplayCat,name="DisplayCat"),
    path('Edit_Cat/<int:cat_id>/',views.EditCat,name="Edit_Cat"),
    path('Delete_Cat/<int:cat_id>/',views.deleteCat,name="Delete_Cat"),
    path('Update_Cat/<int:cat_id>/',views.Update_Category,name="Update_Cat"),
    path('AddProduct/',views.Addproduct,name="AddProduct"),
    path('Saveproduct/',views.Saveproduct,name="Saveproduct"),
    path('Displayproduct/',views.display_Product,name="Displayproduct"),
    path('Edit_Product/<int:dat_id>/', views.EditProduct, name="Edit_Product"),
    path('Delete_Product/<int:pro_id>/', views.deleteProduct, name="Delete_Product"),
    path('Update_Product/<int:P_id>/',views.Update_Product,name="Update_Product"),
    path('login_index/',views.loginpage,name="login_index"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('adminlogout/',views.admin_logout,name="adminlogout"),
    path('ContactDisplay/',views.Display_contact,name="ContactDisplay"),
    path('Contact_Delete/<int:Con_id>/',views.DeleteContact,name="Contact_Delete"),


]