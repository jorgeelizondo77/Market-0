import json
from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# , permission_required

from django.views.generic import ListView, CreateView, UpdateView  

from applications.dom.forms import PaisForm, EntidadForm, EntidadDeleteForm, MunicipioForm, DomicilioForm, ZonaForm
from applications.dom.models import Pais, Entidad, Municipio, Zona
from applications.dom.models import Domicilio


class PaisView(LoginRequiredMixin, ListView):
    model = Pais
    template_name = "dom/pais_list.html"
    context_object_name = "paises"
    login_url ="users:login"

    def get_queryset(self):
        qs = Pais.objects.filter(ac=True)
        return qs


class PaisNew(LoginRequiredMixin, CreateView):
    model = Pais
    template_name = "dom/pais_new.html"
    context_object_name = "pais"
    form_class=PaisForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:pais_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class PaisEdit(LoginRequiredMixin, UpdateView):
    model=Pais
    template_name="dom/pais_edit.html"
    context_object_name = "pais"
    form_class=PaisForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:pais_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["pais"] = Pais.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(PaisEdit, self).form_valid(form)
    

@login_required(login_url='users:login')
def PaisDelete(request, id):
    pais = Pais.objects.filter(pk=id).first()
    contexto={}
    template_name="dom/pais_delete.html"

    if not pais:
        return redirect("dom:pais_list")
    
    if request.method=='GET':
        contexto={'pais':pais}

    if request.method=='POST':
        pais.ac=False
        pais.save()
        return redirect("dom:pais_list")

    return render(request,template_name,contexto)
    


class EntidadView(LoginRequiredMixin, ListView):
    model = Entidad
    template_name = "dom/entidad_list.html"
    context_object_name = "entidades"
    login_url ="users:login"

    def get_queryset(self):
        pais_seleccionado_id = self.request.GET.get('pais')
        
        if pais_seleccionado_id:
            qs = Entidad.objects.filter(ac=True,pais_id=pais_seleccionado_id)
        else:
            p = Pais.objects.filter(ac=True).first()
            qs = Entidad.objects.filter(ac=True, pais_id=p.id)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pais_seleccionado_id = self.request.GET.get('pais')
        context["paises"] = Pais.objects.filter(ac=True)
        if pais_seleccionado_id:
            context["pais_seleccionado_id"] = int(pais_seleccionado_id)
        else:
            p = Pais.objects.filter(ac=True).first()
            context["pais_seleccionado_id"] = p.id

        return context


class EntidadNew(LoginRequiredMixin, CreateView):
    model = Entidad
    template_name = "dom/entidad_new.html"
    context_object_name = "entidad"
    form_class=EntidadForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:entidad_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'].fields['pais'].queryset = Pais.objects.filter(ac=True) 
        # print(context['form'])   
        return context

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class EntidadEdit(LoginRequiredMixin, UpdateView):
    model=Entidad
    template_name="dom/entidad_edit.html"
    context_object_name = "entidad"
    form_class=EntidadForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:entidad_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["pais"] = Pais.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(EntidadEdit, self).form_valid(form)


@login_required(login_url='users:login')
def EntidadDelete(request, id):
    entidad = Entidad.objects.filter(pk=id).first()
    contexto={}
    template_name="dom/entidad_delete.html"

    if not entidad:
        return redirect("dom:entidad_list")
    
    if request.method=='GET':
        contexto={'entidad':entidad}

    if request.method=='POST':
        entidad.ac=False
        entidad.save()
        return redirect("dom:entidad_list")

    return render(request,template_name,contexto)
    



class MunicipioView(LoginRequiredMixin, ListView):
    model = Municipio
    template_name = "dom/municipio_list.html"
    context_object_name = "municipios"
    login_url ="users:login"

    def get_queryset(self):
        pais_seleccionado_id = self.request.GET.get('pais')
        entidad_seleccionada_id = self.request.GET.get('entidad')
        
        if pais_seleccionado_id:
            if entidad_seleccionada_id:
                qs = Municipio.objects.filter(ac=True,pais_id=pais_seleccionado_id, entidad_id=entidad_seleccionada_id)
            else:
                ent = Entidad.objects.filter(ac=True, pais_id=p.id).first()
                qs = Municipio.objects.filter(ac=True, pais_id=pais_seleccionado_id, entidad_id=ent.id)
        else:
            p = Pais.objects.filter(ac=True).first()
            ent = Entidad.objects.filter(ac=True, pais_id=p.id).first()
            qs = Municipio.objects.filter(ac=True, pais_id=p.id, entidad_id=ent.id)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pais_seleccionado_id = self.request.GET.get('pais')
        entidad_seleccionada_id = self.request.GET.get('entidad')

        context["paises"] = Pais.objects.filter(ac=True)

        if pais_seleccionado_id:
            context["pais_seleccionado_id"] = int(pais_seleccionado_id)
            context["entidades"] = Entidad.objects.filter(ac=True, pais_id=pais_seleccionado_id)
            
            if entidad_seleccionada_id:
                context["entidad_seleccionada_id"] = int(entidad_seleccionada_id)
            else:
                ent = context["entidades"].first()
                context["entidad_seleccionada_id"] = ent.id
        else:
            p = Pais.objects.filter(ac=True).first()
            context["pais_seleccionado_id"] = p.id
            context["entidades"] = Entidad.objects.filter(ac=True, pais_id=p.id)
            ent = context["entidades"].first()
            context["entidad_seleccionada_id"] = ent.id

        return context


class MunicipioNew(LoginRequiredMixin, CreateView):
    model = Municipio
    template_name = "dom/municipio_new.html"
    context_object_name = "entidad"
    form_class=MunicipioForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:municipio_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class MunicipioEdit(LoginRequiredMixin, UpdateView):
        model=Municipio
        template_name="dom/municipio_edit.html"
        context_object_name = "municipio"
        form_class=MunicipioForm
        login_url ="users:login"
        success_url = reverse_lazy("dom:municipio_list")
        # success_message="El registro ha sido editado satisfactoriamente"

        def get_context_data(self, **kwargs: Any):
            pk = self.kwargs.get('pk')
            context = super().get_context_data(**kwargs)
            # context["pais"] = Pais.objects.filter(pk=pk).first()
            # context["entidad"] = Entidad.objects.filter(pk=pk).first()
            return context

        def form_valid(self, form):
            form.instance.um = self.request.user.id
            return super(MunicipioEdit, self).form_valid(form)
                

@login_required(login_url='users:login')
def MunicipioDelete(request, id):
    municipio = Municipio.objects.filter(pk=id).first()
    contexto={}
    template_name="dom/municipio_delete.html"

    if not municipio:
        return redirect("dom:municipio_list")
    
    if request.method=='GET':
        contexto={'municipio':municipio}

    if request.method=='POST':
        municipio.ac=False
        municipio.save()
        return redirect("dom:municipio_list")

    return render(request,template_name,contexto)

    


def get_entidades(request):
    data = json.loads(request.body)
    pais_id = data["id"]
    entidades = Entidad.objects.filter(pais__id = pais_id).order_by('nombre')
    return JsonResponse(list(entidades.values("id", "nombre")), safe=False)


def get_municipios(request):
    data = json.loads(request.body)
    entidad_id = data["id"]
    municipios = Municipio.objects.filter(entidad__id = entidad_id).order_by('nombre')
    return JsonResponse(list(municipios.values("id", "nombre")), safe=False)



class DomicilioView(LoginRequiredMixin, ListView):
    model = Domicilio
    template_name = "dom/domicilio_list.html"
    context_object_name = "domicilios"
    login_url ="users:login"

    def get_queryset(self):
        qs = Domicilio.objects.filter(ac=True)
        return qs
    

class DomicilioNew(LoginRequiredMixin, CreateView):
    model = Domicilio
    template_name = "dom/domicilio_new.html"
    context_object_name = "domicilio"
    form_class=DomicilioForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:domicilio_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class DomicilioEdit(LoginRequiredMixin, UpdateView):
    model=Domicilio
    template_name="dom/domicilio_edit.html"
    context_object_name = "domicilio"
    form_class=DomicilioForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:domicilio_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["domicilio"] = Domicilio.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(DomicilioEdit, self).form_valid(form)
    

@login_required(login_url='users:login')
def DomicilioDelete(request, id):
    domicilio = Domicilio.objects.filter(pk=id).first()
    contexto={}
    template_name="dom/domicilio_delete.html"

    if not domicilio:
        return redirect("dom:domicilio_list")
    
    if request.method=='GET':
        contexto={'domicilio':domicilio}

    if request.method=='POST':
        domicilio.ac=False
        domicilio.save()
        return redirect("dom:domicilio_list")

    return render(request,template_name,contexto)
    


class ZonaView(LoginRequiredMixin, ListView):
    model = Zona
    template_name = "dom/zona_list.html"
    context_object_name = "zonas"
    login_url ="users:login"

    def get_queryset(self):
        qs = Zona.objects.filter(ac=True)
        return qs


class ZonaNew(LoginRequiredMixin, CreateView):
    model = Zona
    template_name = "dom/zona_new.html"
    context_object_name = "zona"
    form_class=ZonaForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:zona_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class ZonaEdit(LoginRequiredMixin, UpdateView):
    model=Zona
    template_name="dom/zona_edit.html"
    context_object_name = "zona"
    form_class=ZonaForm
    login_url ="users:login"
    success_url = reverse_lazy("dom:zona_list")
    # success_message="El registro ha sido editado satisfactoriamente"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["zona"] = Zona.objects.filter(pk=pk).first()
        return context

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(ZonaEdit, self).form_valid(form)
    

@login_required(login_url='users:login')
def ZonaDelete(request, id):
    zon = Zona.objects.filter(pk=id).first()
    contexto={}
    template_name="dom/zona_delete.html"

    if not zon:
        return redirect("dom:zona_list")
    
    if request.method=='GET':
        contexto={'zona':zon}

    if request.method=='POST':
        zon.ac=False
        zon.save()
        return redirect("dom:zona_list")

    return render(request,template_name,contexto)
