from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin,\
     PermissionRequiredMixin
from django.views.generic import TemplateView



class MixinFormInvalid:
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

# class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
class SinPrivilegios(LoginRequiredMixin, MixinFormInvalid):
    login_url = 'base:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='base:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base.html'
    # login_url='base:login'

class Base(TemplateView):
    template_name = 'index.html'
    # login_url='base:login'


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "base:login"
    template_name="base/sin_privilegios.html"


