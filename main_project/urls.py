
from django.contrib import admin
from django.urls import path,include
from . import views

#hendling media 
from django.conf import settings
from django.conf.urls.static import static
#handling media ends 
from django.contrib.auth.views import LogoutView
# from . views import user_logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homepage'),
    path('singup/', views.signup,name="singup_page"),

    # path('login/', views.user_login,name="login_page"),
    path('login/', views.user_login_view.as_view(),name="login_page"),

    path('profile/', views.profile_page,name="profile_page"),
    
    path('profile/update/', views.edit_profile,name="edit_profile"),

    # path('update_password/', views.update_password,name="update_password"),
    path('update_password/', views.update_passwordview.as_view(),name="update_password"),

    
    #catagory wise filter stars here ----------------

    path('brand_filter/<slug:car_brand_name_slug>/', views.home,name="brand_filter"),

    #category wise filter ends here ----------------------

    # post details handle starts here --------
    path('post/', include("posts.urls")),
    
    # post details handle ends here ------------
    
    path('logout/',views.user_logout,name="logout_page"),

    # path('experiment_pass/', views.experiment_pass,name="experiment_pass"),
]
#handling media files stars here------
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#handling media files ends here -------


