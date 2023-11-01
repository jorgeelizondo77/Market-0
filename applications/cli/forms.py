from django import forms
from applications.cli.models import Cliente, Regimen
from applications.dom.models import Entidad, Municipio, Pais, Zona


class RegimenForm(forms.ModelForm):
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Clave',
        max_length=3,
        required=True
    )
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Régimen fiscal',
        max_length=50,
        required=True
    )

    class Meta:
        model=Regimen
        fields = ['clave','nombre']

    def __init__(self, *args, **kwargs):
         super(RegimenForm, self).__init__(*args, **kwargs)



class ClienteForm(forms.ModelForm):
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
        widget = forms.Select(attrs={
        'class':'form-control'}),
        label='Régimen', required=False
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
        'class':'form-control'}), required=False
    )
    
    entidad = forms.ModelChoiceField(
        queryset = Entidad.objects.filter(ac=True),
        widget = forms.Select(attrs={
        'class':'form-control'}), required=False
    )
    
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

    contacto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Contacto',
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
    t_casa = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Tel. Casa',
        max_length=50, required=False
    )
    cuenta_contable = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Cuenta contable',
        max_length=20, required=False
    )

    plazo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Plazo', initial=0, required=False
    )
    comentario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Comentario',
        max_length=100, required=False
    )

    class Meta:
        model=Cliente
        fields = ['nombre','rfc','regimen','calle','numero_externo','numero_interno','pais','entidad','municipio',
                'colonia','cp','zona','contacto','correo','t_oficina','t_casa','cuenta_contable','plazo','comentario']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
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
            self.fields['entidad'].queryset = self.instance.pais.entidad_set.order_by('nombre')

        if 'entidad' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                entidad_id = int(self.data.get('entidad'))
                self.fields['municipio'].queryset = Municipio.objects.filter(ac=True, pais_id=pais_id, entidad_id=entidad_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['municipio'].queryset = self.instance.entidad.municipio_set.order_by('nombre')
