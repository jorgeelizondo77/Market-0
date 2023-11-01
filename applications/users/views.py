from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    UpdateView,
    ListView,
    CreateView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    GroupForm,
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm
)
#
from django.contrib.auth.models import Group
from .models import User
# 
from .functions import code_generator


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        codigo = code_generator()

        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            codregistro=codigo
        )
        # enviar el codigo al email del user
        asunto = 'Confrimacion de email'
        mensaje = 'Código de verificacion: ' + codigo
        email_remitente = 'jorge.elizondo@gmail.com'
        #
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        # redirigir a pantalla de valdiacion

        return HttpResponseRedirect(
            reverse(
                'users:user-verification',
                kwargs={'pk': usuario.id}
            )
        )


class UserRegisterNew(LoginRequiredMixin, FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:users_list')

    def form_valid(self, form):
        codigo = code_generator()
        
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            group=form.cleaned_data['group'],
            codregistro=codigo
        )
        return super(UserRegisterNew, self).form_valid(form)
    

class UserRegisterUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/register_edit.html'
    context_object_name = "form"
    form_class = UserRegisterForm
    login_url ="users:login"
    success_url = reverse_lazy('users:users_list')

    def get_object(self):
        return User.objects.get(pk=self.kwargs.get("id"))

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        form.save()

        return super(UserRegisterUpdate, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('base:index')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users:login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users:login')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users:login')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        #
        User.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_active=True
        )
        return super(CodeVerificationView, self).form_valid(form)



class UsersView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "usuarios"
    login_url ="users:login"



def GroupListView(request):
    group_list = Group.objects.order_by('name')
    return render(request, 'users/auth/group_list.html', {'group_list': group_list})


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'users/auth/group_new.html'
    success_url = reverse_lazy('users:perfil_list')


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'users/auth/group_edit.html'
    context_object_name = "form"
    form_class = GroupForm
    login_url ="users:login"
    success_url = reverse_lazy('users:perfil_list')

    def get_object(self):
        return Group.objects.get(pk=self.kwargs.get("id"))

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        form.save()

        return super(GroupUpdateView, self).form_valid(form)