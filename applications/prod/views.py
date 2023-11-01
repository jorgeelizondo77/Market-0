import json
from typing import Any
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# , permission_required

from django.views.generic import ListView, CreateView, UpdateView  

from applications.prod.forms import (Unidad_CompraForm, CategoriaForm, ProductoForm,
                                    EtiquetaForm,MedidaForm)
from applications.prod.models import (Unidad_Compra, Categoria, Producto,
                                    Etiqueta,Medida)
from applications.prov.models import Proveedor


class Unidad_CompraView(LoginRequiredMixin, ListView):
    model = Unidad_Compra
    template_name = "prod/unidad_compra_list.html"
    context_object_name = "unidades_compra"
    login_url ="users:login"

    def get_queryset(self):
        qs = Unidad_Compra.objects.filter(ac=True)
        return qs


class Unidad_CompraNew(LoginRequiredMixin, CreateView):
    model = Unidad_Compra
    template_name = "prod/unidad_compra_new.html"
    context_object_name = "unidad_compra"
    form_class=Unidad_CompraForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:unidad_compra_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class Unidad_CompraEdit(LoginRequiredMixin, UpdateView):
    model=Unidad_Compra
    template_name="prod/unidad_compra_edit.html"
    context_object_name = "unidad_compra"
    form_class=Unidad_CompraForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:unidad_compra_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(Unidad_CompraEdit, self).form_valid(form)
        

@login_required(login_url='users:login')
def Unidad_CompraDelete(request, id):
    unidad_compra = Unidad_Compra.objects.filter(pk=id).first()
    contexto={}
    template_name="prod/unidad_compra_delete.html"

    if not unidad_compra:
        return redirect("prod:unidad_compra_list")
    
    if request.method=='GET':
        contexto={'unidad_compra':unidad_compra}

    if request.method=='POST':
        unidad_compra.ac=False
        unidad_compra.save()
        return redirect("prod:unidad_compra_list")

    return render(request,template_name,contexto)
    


class CategoriaView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "prod/categoria_list.html"
    context_object_name = "categorias"
    login_url ="users:login"

    def get_queryset(self):
        qs = Categoria.objects.filter(ac=True)
        return qs


class CategoriaNew(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = "prod/categoria_new.html"
    context_object_name = "categoria"
    form_class=CategoriaForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:categoria_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class CategoriaEdit(LoginRequiredMixin, UpdateView):
    model=Categoria
    template_name="prod/categoria_edit.html"
    context_object_name = "categoria"
    form_class=CategoriaForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:categoria_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(CategoriaEdit, self).form_valid(form)
        

@login_required(login_url='users:login')
def CategoriaDelete(request, id):
    categoria = Categoria.objects.filter(pk=id).first()
    contexto={}
    template_name="prod/categoria_delete.html"

    if not categoria:
        return redirect("prod:categoria_list")
    
    if request.method=='GET':
        contexto={'categoria':categoria}

    if request.method=='POST':
        categoria.ac=False
        categoria.save()
        return redirect("prod:categoria_list")

    return render(request,template_name,contexto)



class ProductoView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "prod/producto_list.html"
    context_object_name = "productos"
    login_url ="users:login"

    def get_queryset(self):
        qs = Producto.objects.filter(ac=True)
        return qs


class ProductoNew(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "prod/producto_new.html"
    context_object_name = "producto"
    form_class=ProductoForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:producto_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class ProductoEdit(LoginRequiredMixin, UpdateView):
    model=Producto
    template_name="prod/producto_edit.html"
    context_object_name = "producto"
    form_class=ProductoForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:producto_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(ProductoEdit, self).form_valid(form)
        

@login_required(login_url='users:login')
def ProductoDelete(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="prod/producto_delete.html"

    if not producto:
        return redirect("prod:producto_list")
    
    if request.method=='GET':
        contexto={'form':producto}

    if request.method=='POST':
        producto.ac=False
        producto.save()
        return redirect("prod:producto_list")

    return render(request,template_name,contexto)


def get_productos(request):
    data = json.loads(request.body)
    proveedor_id = data["id"]
    prov = Proveedor.objects.get(pk=proveedor_id)
    categorias_prov = prov.categorias.all()
    productos = Producto.objects.filter(ac=True, categoria__in = categorias_prov).order_by('nombre')
    return JsonResponse(list(productos.values("id", "nombre")), safe=False)



class EtiquetaView(LoginRequiredMixin, ListView):
    model = Etiqueta
    template_name = "prod/etiqueta_list.html"
    context_object_name = "etiquetas"
    login_url ="users:login"

    def get_queryset(self):
        qs = Etiqueta.objects.filter(ac=True)
        return qs


class EtiquetaNew(LoginRequiredMixin, CreateView):
    model = Etiqueta
    template_name = "prod/etiqueta_new.html"
    context_object_name = "etiqueta"
    form_class=EtiquetaForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:etiqueta_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class EtiquetaEdit(LoginRequiredMixin, UpdateView):
    model=Etiqueta
    template_name="prod/etiqueta_edit.html"
    context_object_name = "etiqueta"
    form_class=EtiquetaForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:etiqueta_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(EtiquetaEdit, self).form_valid(form)
        

@login_required(login_url='users:login')
def EtiquetaDelete(request, id):
    etiqueta = Etiqueta.objects.filter(pk=id).first()
    contexto={}
    template_name="prod/etiqueta_delete.html"

    if not etiqueta:
        return redirect("prod:etiqueta_list")
    
    if request.method=='GET':
        contexto={'etiqueta':etiqueta}

    if request.method=='POST':
        etiqueta.ac=False
        etiqueta.save()
        return redirect("prod:etiqueta_list")

    return render(request,template_name,contexto)




class MedidaView(LoginRequiredMixin, ListView):
    model = Medida
    template_name = "prod/medida_list.html"
    context_object_name = "medidas"
    login_url ="users:login"

    def get_queryset(self):
        qs = Medida.objects.filter(ac=True)
        return qs


class MedidaNew(LoginRequiredMixin, CreateView):
    model = Medida
    template_name = "prod/medida_new.html"
    context_object_name = "medida"
    form_class=MedidaForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:medida_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class MedidaEdit(LoginRequiredMixin, UpdateView):
    model=Medida
    template_name="prod/medida_edit.html"
    context_object_name = "medida"
    form_class=MedidaForm
    login_url ="users:login"
    success_url = reverse_lazy("prod:medida_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(MedidaEdit, self).form_valid(form)
        

@login_required(login_url='users:login')
def MedidaDelete(request, id):
    medida = Medida.objects.filter(pk=id).first()
    contexto={}
    template_name="prod/medida_delete.html"

    if not medida:
        return redirect("prod:medida_list")
    
    if request.method=='GET':
        contexto={'medida':medida}

    if request.method=='POST':
        medida.ac=False
        medida.save()
        return redirect("prod:medida_list")

    return render(request,template_name,contexto)