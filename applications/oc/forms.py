from django import forms
from applications.cli.models import Cliente
from applications.dom.models import Domicilio
from applications.prod.models import Producto
from applications.prov.models import Proveedor
from applications.users.models import User
from applications.oc.models import Orden_Compra


SINO_CHOICES = (
        ('', 'Seleccione'),
        ('S', 'SI'),
        ('N', 'NO'), 
)
DIVISA_CHOICES = (
        ('', 'Seleccione'),
        ('P', 'Pesos (MXN)'),
        ('D', 'Dólares (USD)'), 
)
LAB_CHOICES = (
        ('', 'Seleccione'),
        ('E', 'Empaque'),
        ('P', 'Puesto en Bodega'), 
)

class Orden_CompraForm(forms.ModelForm):
    proveedor = forms.ModelChoiceField(
        queryset = Proveedor.objects.filter(ac=True),
        widget = forms.Select(attrs={'class':'form-control'}),
        label='Proveedor', required=True
    )
    # libre_abordo = forms.CharField(
    #      label='Libre a Bordo', 
    #      widget=forms.Select(
    #          choices=LAB_CHOICES,
    #          attrs={
    #             'class': 'form-control'
    #             }
    #          )
    # )
    entregar_en = forms.ModelChoiceField(
        queryset = Domicilio.objects.filter(ac=True),
        widget = forms.Select(attrs={'class':'form-control'}),
        label='Entregar en', required=True
    )
    fecha_entrega = forms.DateField(
        widget=forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date','class': 'form-control'}),
        required = False,
        label='Fecha de Entrega'
        )
    comentario_oc = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Comentario orden de Compra',
        max_length=100,required=False
    )
    cliente = forms.ModelChoiceField(
        queryset = Cliente.objects.filter(ac=True),
        widget = forms.Select(attrs={'class':'form-control'}),
        label='Cliente', required=False
    )
    divisa = forms.CharField(
         label='Divisa', 
         widget=forms.Select(
             choices=DIVISA_CHOICES,
             attrs={
                'class': 'form-control'
                }
             ),required=False
    )
    tipo_cambio = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'})
    )
    comentario_pedido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Comentario sobre el Pedido',
        max_length=100,required=False
    )
    embarcador = forms.ModelChoiceField(
        queryset = User.objects.all(),
        widget = forms.Select(attrs={'class':'form-control'}),
        label='Embarcador', required=True
    )
    comision = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    tarimas = forms.IntegerField(initial=0,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    cajas_tarimas = forms.IntegerField(initial=0,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    total_cajas = forms.IntegerField(initial=0,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    flete1 = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    flete2 = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    aduana_mx = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    sobrepeso_mx = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    aduana_us = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    sobrepeso_us = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    logistica = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    otros = forms.DecimalField(initial=0, max_digits=12, decimal_places=2,required=False,
                                widget = forms.NumberInput(attrs={'class':'form-control2'}))
    
    producto = forms.ModelChoiceField(
        queryset = Producto.objects.all(),
        widget = forms.Select(attrs={'class':'form-control'}),
        label='Producto', required=True
    )
    total_gasto = forms.DecimalField(
        widget=forms.HiddenInput(),
        required=False
    )
    tipoUpdate = forms.CharField(
        widget=forms.HiddenInput(),
        empty_value="1"
    )

    class Meta:
        model=Orden_Compra
        fields = ['proveedor','entregar_en','fecha_entrega','comentario_oc','cliente','divisa',
                'tipo_cambio','comentario_pedido','embarcador','comision','tarimas','cajas_tarimas',
                'total_cajas','flete1','flete2','aduana_mx','sobrepeso_mx','aduana_us',
                'sobrepeso_us','logistica','otros','producto','total_gasto']

    def __init__(self, *args, **kwargs):
        super(Orden_CompraForm, self).__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.none()

        if 'proveedor' in self.data:
            try:
                proveedor_id = int(self.data.get('proveedor'))
                prov = Proveedor.objects.get(pk=proveedor_id)
                categorias_prov = prov.categorias.all()
                self.fields['producto'].queryset = Producto.objects.filter(ac=True, categoria__in = categorias_prov).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['proveedor'].disabled=True
            proveedor_id = int(self.instance.proveedor.id)
            prov = Proveedor.objects.get(pk=proveedor_id)
            categorias_prov = prov.categorias.all()
            self.fields['producto'].queryset = Producto.objects.filter(ac=True, categoria__in = categorias_prov).order_by('nombre')
           