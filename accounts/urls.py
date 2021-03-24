from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$',views.AboutView.as_view(),name='about'),
    url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.register, name="signup"),
    url(r"update/$", views.update_profile, name='update'),
    url(r"request/$", views.contactView, name='request'),
    url(r"success/$", views.successView.as_view(),name="success")
]
