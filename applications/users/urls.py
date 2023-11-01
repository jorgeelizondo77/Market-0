from django.urls import path

from applications.users.views import (UserRegisterNew, UserRegisterUpdate, LoginUser, LogoutView,
                    UpdatePasswordView, CodeVerificationView, UsersView,
                    GroupListView, GroupCreateView,GroupUpdateView
                    )

app_name = "users"

urlpatterns = [
    path('register/', UserRegisterNew.as_view(), name='register'),
    path('register/edit/<int:id>', UserRegisterUpdate.as_view(), name='register_edit'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', UpdatePasswordView.as_view(), name='user_update'),
    path('user-verification/<pk>/', CodeVerificationView.as_view(),name='user_verification'),
    path('usuarios/', UsersView.as_view(), name='users_list'),

    path('perfiles/',GroupListView, name='perfil_list'),
    path('perfil/new',GroupCreateView.as_view(), name='perfil_new'),
    path('perfil/edit/<int:id>', GroupUpdateView.as_view(), name='perfil_edit'),
]