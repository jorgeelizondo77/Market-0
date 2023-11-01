from django import forms
from applications.prod.models import Categoria, Etiqueta, Medida, Producto, Unidad_Compra


class Unidad_CompraForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Unidad de Compra',
        max_length=50
    )

    class Meta:
        model=Unidad_Compra
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
         super(Unidad_CompraForm, self).__init__(*args, **kwargs)



class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Categoria',
        max_length=50
    )

    class Meta:
        model=Categoria
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
         super(CategoriaForm, self).__init__(*args, **kwargs)



class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombre',
        max_length=60
    )
    sku = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='SKU',
        max_length=20, required=False
    )
    upc = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='UPC',
        max_length=20, required=False
    )
    cuenta_contable = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Cuenta Contable',
        max_length=20, required=False
    )

    numero_sat = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Número SAT',
        max_length=20, required=False
    )
    unidad_sat = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Unidad SAT',
        max_length=20, required=False
    )
    qrcaja = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='QR Caja',
        max_length=20, required=False
    )
    qrpalet = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='QR Palet',
        max_length=20, required=False
    )

    unidad_compra = forms.ModelChoiceField(
        queryset = Unidad_Compra.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False)
    
    costo_promedio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Costo Promedio', 
        max_length=20, required=False, initial=0
    )
    unidad_venta = forms.ModelChoiceField(
        queryset = Unidad_Compra.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False)
    
    margen = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Margen',
        max_length=20, required=False, initial=0
    )
   
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False)
    
    comentario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Comentario',
        max_length=100, required=False
    )

    class Meta:
        model=Producto
        fields = ['nombre','sku','upc','cuenta_contable','numero_sat','unidad_sat',
                'qrcaja','qrpalet','unidad_compra','costo_promedio','unidad_venta','margen',
                'categoria','comentario']

    def __init__(self, *args, **kwargs):
         super(ProductoForm, self).__init__(*args, **kwargs)


class EtiquetaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombre',
        max_length=30
    )
    productos = forms.ModelMultipleChoiceField(
            queryset=Producto.objects.filter(ac=True),
            # widget=forms.CheckboxSelectMultiple(attrs={'oninvalid':"this.setCustomValidity('Favor de indicar su categoría')",'oninput':"setCustomValidity('')"}),
            widget=forms.CheckboxSelectMultiple,
            label='Productos'
            )
    
    class Meta:
        model=Etiqueta
        fields = ['nombre','productos']

    def __init__(self, *args, **kwargs):
         super(EtiquetaForm, self).__init__(*args, **kwargs)


class MedidaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombre',
        max_length=30
    )
    productos = forms.ModelMultipleChoiceField(
            queryset=Producto.objects.filter(ac=True),
            # widget=forms.CheckboxSelectMultiple(attrs={'oninvalid':"this.setCustomValidity('Favor de indicar su categoría')",'oninput':"setCustomValidity('')"}),
            widget=forms.CheckboxSelectMultiple,
            label='Productos'
            )
    
    class Meta:
        model=Medida
        fields = ['nombre','productos']

    def __init__(self, *args, **kwargs):
         super(MedidaForm, self).__init__(*args, **kwargs)


