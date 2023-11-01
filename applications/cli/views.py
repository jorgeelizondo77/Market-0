from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# , permission_required

from django.views.generic import ListView, CreateView, UpdateView
from applications.cli.forms import ClienteForm, RegimenForm  

from applications.cli.models import Cliente, Regimen


class RegimenView(LoginRequiredMixin, ListView):
    model = Regimen
    template_name = "cli/regimen_list.html"
    context_object_name = "regimenes"
    login_url ="users:login"

    def get_queryset(self):
        qs = Regimen.objects.filter(ac=True)
        return qs


class RegimenNew(LoginRequiredMixin, CreateView):
    model = Regimen
    template_name = "cli/regimen_new.html"
    context_object_name = "regimen"
    form_class=RegimenForm
    login_url ="users:login"
    success_url = reverse_lazy("cli:regimen_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class RegimenEdit(LoginRequiredMixin, UpdateView):
    model=Regimen
    template_name="cli/regimen_edit.html"
    context_object_name = "regimen"
    form_class=RegimenForm
    login_url ="users:login"
    success_url = reverse_lazy("cli:regimen_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["regimen"] = Regimen.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(RegimenEdit, self).form_valid(form)
    

@login_required(login_url='users:login')
def RegimenDelete(request, id):
    regimen = Regimen.objects.filter(pk=id).first()
    contexto={}
    template_name="cli/regimen_delete.html"

    if not regimen:
        return redirect("cli:regimen_list")
    
    if request.method=='GET':
        contexto={'regimen':regimen}

    if request.method=='POST':
        regimen.ac=False
        regimen.save()
        return redirect("cli:regimen_list")

    return render(request,template_name,contexto)




class ClienteView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cli/cliente_list.html"
    context_object_name = "clientes"
    login_url ="users:login"

    def get_queryset(self):
        qs = Cliente.objects.filter(ac=True)
        return qs


class ClienteNew(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "cli/cliente_new.html"
    context_object_name = "cliente"
    form_class=ClienteForm
    login_url ="users:login"
    success_url = reverse_lazy("cli:cliente_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class ClienteEdit(LoginRequiredMixin, UpdateView):
    model=Cliente
    template_name="cli/cliente_edit.html"
    context_object_name = "form"
    form_class=ClienteForm
    login_url ="users:login"
    success_url = reverse_lazy("cli:cliente_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(ClienteEdit, self).form_valid(form)
        

@login_required(login_url='users:login')
def ClienteDelete(request, id):
    cliente = Cliente.objects.filter(pk=id).first()
    contexto={}
    template_name="cli/cliente_delete.html"

    if not cliente:
        return redirect("cli:cliente_list")
    
    if request.method=='GET':
        contexto={'cliente':cliente}

    if request.method=='POST':
        cliente.ac=False
        cliente.save()
        return redirect("cli:cliente_list")

    return render(request,template_name,contexto)
