from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name="post_edit"),
    path('post/new', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('register/', SignUpView.as_view(template_name='registration/register.html'), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
     name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]