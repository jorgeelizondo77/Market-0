from django import forms
from django.core.exceptions import ValidationError
from applications.cli.models import Regimen
from applications.dom.models import Entidad, Municipio, Pais, Zona
from applications.prod.models import Categoria
from applications.prov.models import Banco, Forma_Pago, Proveedor


class BancoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Banco',
        max_length=50
    )

    class Meta:
        model=Banco
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
         super(BancoForm, self).__init__(*args, **kwargs)


class Forma_PagoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Banco',
        max_length=50
    )

    class Meta:
        model=Forma_Pago
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
         super(Forma_PagoForm, self).__init__(*args, **kwargs)



class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombre',
        max_length=100
    )
    rfc = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='RFC',
        max_length=13, required=False
    )
    regimen = forms.ModelChoiceField(
        queryset = Regimen.objects.filter(ac=True),
        widget = forms.Select(attrs={'class':'form-control'}),
        label='Régimen', required=False
    )
    contacto_embarque = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Contacto Embarque',
        max_length=100, required=False
    )
    correo = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Correo', required=False
    )
    t_celular = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Tel. Celular',
        max_length=50, required=False
    )
    t_oficina = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Tel. Oficina',
        max_length=50, required=False
    )
    calle = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Calle', max_length=50, required=False
    )
    numero_externo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Número externo',
        max_length=10, required=False
    )
    numero_interno = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Número interno',
        max_length=10, required=False
    )

    pais = forms.ModelChoiceField(
        queryset = Pais.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False)
    
    entidad = forms.ModelChoiceField(
        queryset = Entidad.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False)
    
    municipio = forms.ModelChoiceField(
        queryset = Municipio.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False
    )
    
    colonia = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Colonia',
        max_length=60, required=False
    )
    cp = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Código Postal',
        max_length=10, required=False
    )
    zona = forms.ModelChoiceField(
        queryset = Zona.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False
    )

    categorias = forms.ModelMultipleChoiceField(
            queryset=Categoria.objects.filter(ac=True),
            # widget=forms.CheckboxSelectMultiple(attrs={'oninvalid':"this.setCustomValidity('Favor de indicar su categoría')",'oninput':"setCustomValidity('')"}),
            widget=forms.CheckboxSelectMultiple
            )

    contacto_venta = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Contacto Ventas',
        max_length=100, required=False
    )
    correo_venta = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Correo Ventas', required=False
    )
    t_celular_venta = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Tel. Celular',
        max_length=50, required=False
    )
    
    t_oficina_venta = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Tel. Oficina',
        max_length=50, required=False
    )

    forma_pago = forms.ModelChoiceField(
        queryset = Forma_Pago.objects.filter(ac=True),
        widget = forms.Select(attrs={'class':'form-control'}), 
        required=False
    )
    # plazo = models.PositiveIntegerField(default=0, blank=True, null=True)
    # descuento = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    # limite_credito = models.PositiveIntegerField(default=0, blank=True, null=True)

    banco = forms.ModelChoiceField(
        queryset = Banco.objects.filter(ac=True),
        widget = forms.Select(attrs={'class':'form-control'}), 
        required=False
    )
    cuenta_banco = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Cuenta Banco',
        max_length=20, required=False
    )
    clabe = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='CLABE',
        max_length=20, required=False
    )

    comentario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Comentario',
        max_length=100, required=False
    )

    class Meta:
        model=Proveedor
        fields = ['nombre','rfc','regimen','contacto_embarque','correo','t_celular','t_oficina',
                'calle','numero_externo','numero_interno','pais','entidad','municipio','colonia',
                'cp','zona','categorias','contacto_venta','correo_venta','t_celular_venta','t_oficina_venta',
                'forma_pago','plazo','descuento','limite_credito','banco','cuenta_banco','clabe',
                'comentario']
        
    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['categorias'].required = True
        self.fields['pais'].queryset = Pais.objects.filter(ac=True)
        self.fields['entidad'].queryset = Entidad.objects.none()
        self.fields['municipio'].queryset = Municipio.objects.none()

        if 'pais' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                entidades = Entidad.objects.filter(ac=True, pais_id=pais_id).order_by('nombre')
                self.fields['entidad'].queryset = entidades
                entidad_id = entidades.first()
                self.fields['municipio'].queryset = Municipio.objects.filter(ac=True, pais_id=pais_id, entidad_id=entidad_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # pass
            # try:
            self.fields['entidad'].queryset = self.instance.pais.entidad_set.order_by('nombre')
            # except (ValueError, TypeError):
                # pass

        if 'entidad' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                entidad_id = int(self.data.get('entidad'))
                self.fields['municipio'].queryset = Municipio.objects.filter(ac=True, pais_id=pais_id, entidad_id=entidad_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # pass
            self.fields['municipio'].queryset = self.instance.entidad.municipio_set.order_by('nombre')

        def clean_categorias(self):
            if not self.cleaned_data['categorias']:
                self.add_error('categorias', 'Debe seleccionar al menos una categoría.')
                raise forms.ValidationError({'categorias':'Debe seleccionar al menos una categoría.'})
            return self.cleaned_data['categorias']


