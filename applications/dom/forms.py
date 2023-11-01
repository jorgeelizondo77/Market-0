from django import forms
from applications.dom.models import Pais, Entidad, Municipio, Domicilio, Zona


class PaisForm(forms.ModelForm):
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Clave',
        max_length=3
    )
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Pais',
        max_length=50
    )

    class Meta:
        model=Pais
        fields = ['clave','nombre']

    def __init__(self, *args, **kwargs):
        super(PaisForm, self).__init__(*args, **kwargs)



class EntidadForm(forms.ModelForm):
    pais = forms.ModelChoiceField(
    queryset = Pais.objects.filter(ac=True),
    widget = forms.Select(attrs={
         'class':'form-control'}))
    
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Clave',
        max_length=3
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Entidad',
        max_length=50
    )

    class Meta:
        model=Entidad
        fields = ['pais','clave','nombre']

    def __init__(self, *args, **kwargs):
        super(EntidadForm, self).__init__(*args, **kwargs)


class EntidadDeleteForm(forms.ModelForm):
    pais = forms.ModelChoiceField(
    queryset = Pais.objects.filter(ac=True),
    widget = forms.Select(attrs={
         'class':'form-control',
         'disabled':'disabled'
         }))
    
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
         'readonly':'readonly'}),
        label='Clave',
        max_length=3
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
         'readonly':'readonly'}),
        label='Entidad',
        max_length=50
    )

    class Meta:
        model=Entidad
        fields = ['pais','clave','nombre']

    def __init__(self, *args, **kwargs):
        super(EntidadDeleteForm, self).__init__(*args, **kwargs)


class MunicipioForm(forms.ModelForm):
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Clave',
        max_length=3
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Municipio',
        max_length=60
    )

    class Meta:
        model=Municipio
        fields = ['pais','entidad','clave','nombre']


    def __init__(self, *args, **kwargs):
        super(MunicipioForm, self).__init__(*args, **kwargs)
        self.fields['pais'].queryset = Pais.objects.filter(ac=True)
        self.fields['entidad'].queryset = Entidad.objects.none()

        if 'pais' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                entidades = Entidad.objects.filter(ac=True, pais_id=pais_id).order_by('nombre')
                self.fields['entidad'].queryset = entidades
                entidad_id = entidades.first()
                # self.fields['municipio'].queryset = Municipio.objects.filter(ac=True, pais_id=pais_id, entidad_id=entidad_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['entidad'].queryset = self.instance.pais.entidad_set.order_by('nombre')

        if 'entidad' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                entidad_id = int(self.data.get('entidad'))
                # self.fields['municipio'].queryset = Entidad.objects.filter(ac=True, pais_id=pais_id, entidad_id=entidad_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            pass
            # self.fields['municipio'].queryset = self.instance.pais.entidad.municipio_set.order_by('nombre')



class DomicilioForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Domicilio',
        max_length=50
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

    class Meta:
        model=Domicilio
        fields = ['nombre','calle','numero_externo','numero_interno','pais',
                  'entidad','municipio','colonia','cp']

    def __init__(self, *args, **kwargs):
        super(DomicilioForm, self).__init__(*args, **kwargs)
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

            



class ZonaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Zona',
        max_length=50
    )

    class Meta:
        model=Zona
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(ZonaForm, self).__init__(*args, **kwargs)
