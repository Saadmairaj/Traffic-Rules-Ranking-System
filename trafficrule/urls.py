"""trafficrule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    url(r'^register/$', views.signup, name='signup'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^myaccount/$', views.update_profile, name='profile'),
    url(r'^viewprofile/(?P<pk>[0-9]+)/$', views.view_profile, name='view-profile'),
    url(r'^password/$', views.change_password, name='account/change_password'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="account/loggedout.html"), name='logout'),
    url(r'^thanks/$', TemplateView.as_view(template_name='thank-you.html'), name='thanks'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact-us'),
    url(r'^complaint/$', views.ComplaintView.as_view(), name='complaint'),
    url(r'^complaint-list/$', views.ComplaintListView.as_view(), name='complaint-list'),
    url(r'^vehicles/$', views.VehiclesListView.as_view(), name='vehicles'),
    url(r'^update-complaint/(?P<pk>[0-9]+)/$', views.ComplaintUpdateView.as_view(), name='update-complaint'),
    url(r'^user-list/$', views.ProfilesListView.as_view(), name='user-list'),
    url(r'^payment/(?P<pk>[0-9]+)$', views.PaymentView.as_view(), name='payment'),
    # path('payments/', include('payments.urls'), name='payments'),   # Not working (app payments)
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
