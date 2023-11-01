from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# , permission_required

from django.urls import reverse_lazy
from applications.prov.forms import BancoForm, Forma_PagoForm, ProveedorForm

from applications.prov.models import Banco, Forma_Pago, Proveedor
from django.views.generic import ListView, CreateView, UpdateView  


class BancoView(LoginRequiredMixin, ListView):
    model = Banco
    template_name = "prov/banco_list.html"
    context_object_name = "bancos"
    login_url ="users:login"

    def get_queryset(self):
        qs = Banco.objects.filter(ac=True)
        return qs
    

class BancoNew(LoginRequiredMixin, CreateView):
    model = Banco
    template_name = "prov/banco_new.html"
    context_object_name = "banco"
    form_class=BancoForm
    login_url ="users:login"
    success_url = reverse_lazy("prov:banco_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class BancoEdit(LoginRequiredMixin, UpdateView):
    model=Banco
    template_name="prov/banco_edit.html"
    context_object_name = "banco"
    form_class=BancoForm
    login_url ="users:login"
    success_url = reverse_lazy("prov:banco_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["banco"] = Banco.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(BancoEdit, self).form_valid(form)
    

@login_required(login_url='users:login')
def BancoDelete(request, id):
    banco = Banco.objects.filter(pk=id).first()
    contexto={}
    template_name="prov/banco_delete.html"

    if not banco:
        return redirect("prov:banco_list")
    
    if request.method=='GET':
        contexto={'banco':banco}

    if request.method=='POST':
        banco.ac=False
        banco.save()
        return redirect("prov:banco_list")

    return render(request,template_name,contexto)


    
class Forma_PagoView(LoginRequiredMixin, ListView):
    model = Forma_Pago
    template_name = "prov/forma_pago_list.html"
    context_object_name = "formas_pago"
    login_url ="users:login"

    def get_queryset(self):
        qs = Forma_Pago.objects.filter(ac=True)
        return qs


class Forma_PagoNew(LoginRequiredMixin, CreateView):
    model = Forma_Pago
    template_name = "prov/forma_pago_new.html"
    context_object_name = "forma_pago"
    form_class=Forma_PagoForm
    login_url ="users:login"
    success_url = reverse_lazy("prov:forma_pago_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class Forma_PagoEdit(LoginRequiredMixin, UpdateView):
    model=Forma_Pago
    template_name="prov/forma_pago_edit.html"
    context_object_name = "forma_pago"
    form_class=Forma_PagoForm
    login_url ="users:login"
    success_url = reverse_lazy("prov:forma_pago_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["forma_pago"] = Forma_Pago.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(Forma_PagoEdit, self).form_valid(form)
    

@login_required(login_url='users:login')
def Forma_PagoDelete(request, id):
    forma_pago = Forma_Pago.objects.filter(pk=id).first()
    contexto={}
    template_name="prov/forma_pago_delete.html"

    if not forma_pago:
        return redirect("prov:forma_pago_list")
    
    if request.method=='GET':
        contexto={'forma_pago':forma_pago}

    if request.method=='POST':
        forma_pago.ac=False
        forma_pago.save()
        return redirect("prov:forma_pago_list")

    return render(request,template_name,contexto)    



class ProveedorView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = "prov/proveedor_list.html"
    context_object_name = "proveedores"
    login_url ="users:login"

    def get_queryset(self):
        qs = Proveedor.objects.filter(ac=True)
        return qs


class ProveedorNew(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = "prov/proveedor_new.html"
    context_object_name = "proveedores"
    form_class=ProveedorForm
    login_url ="users:login"
    success_url = reverse_lazy("prov:proveedor_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form: ProveedorForm) -> HttpResponse:
        print(form)
        return super().form_invalid(form)
    
    
    

class ProveedorEdit(LoginRequiredMixin, UpdateView):
    model=Proveedor
    template_name="prov/proveedor_edit.html"
    context_object_name = "proveedor"
    form_class=ProveedorForm
    login_url ="users:login"
    success_url = reverse_lazy("prov:proveedor_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["proveedor"] = Proveedor.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(ProveedorEdit, self).form_valid(form)
    

@login_required(login_url='users:login')
def ProveedorDelete(request, id):
    proveedor = Proveedor.objects.filter(pk=id).first()
    contexto={}
    template_name="prov/proveedor_delete.html"

    if not proveedor:
        return redirect("prov:proveedor_list")
    
    if request.method=='GET':
        contexto={'proveedor':proveedor}

    if request.method=='POST':
        proveedor.ac=False
        proveedor.save()
        return redirect("prov:proveedor_list")

    return render(request,template_name,contexto)    

