from django.contrib import admin
from django.contrib import auth
from django.urls import path
from django.urls.conf import include
from dashboard import views as dash_views
from  django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/',dash_views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="dashboard/login.html"),name="login"),
    path('profile/', dash_views.profile, name="profile"),
    path('update-avatar/', dash_views.updateUserAvatar, name="update-avatar"),
    path('logout/',auth_views.LogoutView.as_view(template_name="dashboard/logout.html"),name="logout"),
]
