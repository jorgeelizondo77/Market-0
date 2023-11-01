import decimal
import json
from typing import Any

import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db.models import Sum
from applications.oc.forms import Orden_CompraForm

from applications.oc.models import Orden_Compra, Orden_Compra_Estatus
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView,UpdateView,ListView,View

from applications.oc.models import Orden_Compra_Detalle
from applications.prod.models import Etiqueta, Medida, Producto
from applications.users.models import User


class Orden_CompraNew(LoginRequiredMixin, CreateView):
    model = Orden_Compra
    template_name = "oc/oc_consigna_new.html"
    context_object_name = "oc"
    form_class=Orden_CompraForm
    login_url ="users:login"

    def get_success_url(self):
        return reverse_lazy('oc:occ_edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        estatus = Orden_Compra_Estatus.objects.get(pk=1)
        form.instance.estatus = estatus
        form.instance.uc = self.request.user
        form.instance.consignacion = True
        producto = form.cleaned_data['producto']
        if(form.is_valid):
            orden_compra = form.save(commit=False)
            orden_compra.save()
            oc_det = Orden_Compra_Detalle()
            oc_det.orden_compra = orden_compra
            oc_det.producto_id = int(producto.id)
            oc_det.uc = self.request.user
            oc_det.save()
        return super(Orden_CompraNew, self).form_valid(form)    


class Orden_CompraEdit(LoginRequiredMixin, UpdateView):
    model=Orden_Compra
    template_name="oc/oc_consigna_edit.html"
    context_object_name = "oc"
    form_class=Orden_CompraForm
    login_url ="users:login"

    def get_context_data(self, **kwargs: Any):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        oc_det = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra__id=pk).order_by('-fc')
        context["detalle"] = oc_det
        return context
    
    def get_success_url(self):
        return reverse_lazy('oc:occ_edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        estatus = Orden_Compra_Estatus.objects.get(pk=1)
        form.instance.estatus = estatus
        form.instance.um = self.request.user.id
        form.instance.consignacion = True
        producto = form.cleaned_data['producto']
        actualizar = form.cleaned_data['tipoUpdate']
        if(form.is_valid):
            orden_compra = form.save(commit=False)
            orden_compra.save()
            if int(actualizar) == 1:
                oc_det = Orden_Compra_Detalle()
                oc_det.orden_compra = orden_compra
                oc_det.producto_id = int(producto.id)
                oc_det.uc = self.request.user
                oc_det.save()
        return super(Orden_CompraEdit, self).form_valid(form)
    

def guarda_oc_detalle(request):
    data = json.loads(request.body)
    id = data["id"]
    orden_compra_id = data["orden_compra_id"]
    etiquetaId = data["etiquetaId"]
    medidaId = data["medidaId"]
    precio_ventaId = decimal.Decimal(data["precio_ventaId"])
    precio_reportarId = decimal.Decimal(data["precio_reportarId"])
    cantidadId = decimal.Decimal(data["cantidadId"])
    subtotalId = decimal.Decimal(data["subtotalId"])

    oc = Orden_Compra.objects.get(pk=orden_compra_id)

    prc_com = oc.comision/100
    comision = precio_ventaId * prc_com

    gasto = oc.total_gasto

    precio = precio_ventaId - comision - gasto
    importe = precio * cantidadId
    # subtotal = precio_ventaId * cantidadId

    oc_det = Orden_Compra_Detalle.objects.get(pk=id)
    oc_det.etiqueta_id = int(etiquetaId)
    oc_det.medida_id = int(medidaId)
    oc_det.precio_venta = precio_ventaId
    oc_det.precio_reportar = precio_reportarId
    oc_det.comision = comision
    oc_det.gasto = gasto
    oc_det.precio = precio
    oc_det.cantidad = cantidadId
    oc_det.importe = importe
    oc_det.subtotal = subtotalId
    oc_det.uc = request.user
    oc_det.save()
    
    oc.total_precio_venta = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('precio_venta'))['precio_venta__sum']
    oc.total_comision = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('comision'))['comision__sum']
    oc.total_precio = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('precio'))['precio__sum']
    oc.total_cantidad = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('cantidad'))['cantidad__sum']
    oc.total_importe = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('importe'))['importe__sum']
    oc.subtotal = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('subtotal'))['subtotal__sum']
    oc.save()
    
    return JsonResponse({'message':"",
                         'total_cantidad':oc.total_cantidad,
                         'subtotal':oc.subtotal
                         }, status=200, safe=False)
    


def elimina_oc_detalle(request):
    data = json.loads(request.body)
    id = data["id"]
    orden_compra_id = data["orden_compra_id"]
    oc = Orden_Compra.objects.get(pk=orden_compra_id)

    oc_det = Orden_Compra_Detalle.objects.get(pk=id)
    oc_det.ac = False
    oc_det.uc = request.user
    oc_det.save()
    
    oc.total_precio_venta = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('precio_venta'))['precio_venta__sum']
    oc.total_comision = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('comision'))['comision__sum']
    oc.total_precio = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('precio'))['precio__sum']
    oc.total_cantidad = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('cantidad'))['cantidad__sum']
    oc.total_importe = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('importe'))['importe__sum']
    oc.subtotal = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra_id=orden_compra_id).aggregate(Sum('subtotal'))['subtotal__sum']
    oc.save()
    
    return JsonResponse({'message':"",
                         'total_cantidad':oc.total_cantidad,
                         'subtotal':oc.subtotal
                         }, status=200, safe=False)
   


class Orden_CompraView(LoginRequiredMixin, ListView):
    model = Orden_Compra
    template_name = "oc/oc_consigna_list.html"
    context_object_name = "orders"
    login_url ="users:login"

    def get_queryset(self):
        qs = Orden_Compra.objects.filter(ac=True).order_by('-fc')
        return qs
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     # Obtener todos los IDs de usuario de las órdenes
    #     id_usuarios = Orden_Compra.objects.filter(ac=True).values_list('uc', flat=True)
        
    #     # Obtener los nombres de los usuarios para los IDs encontrados
    #     usuarios = User.objects.filter(id__in=id_usuarios)
        
    #     # Crear un diccionario que mapea los IDs de usuario a los nombres de usuario
    #     usuario_dict = {usuario.id: usuario.nombre for usuario in usuarios}
        
    #     # Agregar el diccionario al contexto para acceder en la plantilla
    #     context['usuarios'] = usuario_dict
        
    #     return context
    

class Orden_CompraPdfView(View):
    def link_callback(self, uri, rel):
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise RuntimeError(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path
    
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('oc/oc_consigna_report.html')

            pk = self.kwargs.get('pk')
            oc = Orden_Compra.objects.get(pk=pk)
            oc_det = Orden_Compra_Detalle.objects.filter(ac=True, orden_compra__id=pk)

            context = {
                'logo': '{}{}'.format(settings.STATIC_URL, 'img/logo_bonita.png'),
                'title':'Mi primer PDF',
                'oc': oc,
                'oc_det': oc_det
                }
            
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'atachment; filename="report.pdf"'

            pisaStatus = pisa.CreatePDF(
                html, dest=response, link_callback=self.link_callback)
            
            # if pisaStatus.err:
            #         return HttpResponse('Se encontraron algunos errores' + html + '</pre>')
            return response
        except:
             pass
        return HttpResponseRedirect(reverse_lazy('oc:occ_list'))