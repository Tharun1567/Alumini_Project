from django.urls import path
from module1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('more',views.more,name="more"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('login',views.loginView,name="loginPage"),
    path('profile',views.profile,name="profile"),
    path('alumi/<int:rid>',views.dedicated,name="alumi"),
    path('staff',views.staff,name="staff"),
    path('update/<int:rid>',views.update,name="update"),
    path('delete/<int:rid>',views.delete,name="delete"),
    path('register',views.register,name="register"),
    path('logout',views.logoutView,name="logout"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    