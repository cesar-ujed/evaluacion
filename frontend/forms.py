from django import forms
from api.models import *
from django.contrib.auth.forms import AuthenticationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'contraseña'}))


class Subir_a(forms.ModelForm):
    # Filtramos los indicadores por una categoría específica (ejemplo: categoría ID=1)
    indicador = forms.ModelChoiceField(
        queryset=Indicador.objects.filter(categoria__eje__modulo__id=1),  # Cambia el filtro según necesites
        empty_label="Selecciona un indicador",
        # label="Indicador"
        widget=forms.Select(attrs={"class": "form-control"})
    )

    subindicador = forms.ModelChoiceField(
        queryset=Subindicador.objects.all(),  # Cambia el filtro según necesites
        empty_label="Selecciona un subindicador",
        widget=forms.Select(attrs={"class": "form-control"})

    )


    class Meta:
        model = Evidencia
        fields = [
            'indicador', 
            'subindicador', 
            'nombre_evidencia',
            'archivo', 
            'comentarios',
            'juicio_valor',
        ]
        widgets = {
            'indicador': forms.Select(attrs={'class': 'form-control'}),
            'subindicador': forms.Select(attrs={'class': 'form-control'}),
            'nombre_evidencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la evidencia...'
                }),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enlace(URL) de evidencia o algun comentario...'
                }),
            'juicio_valor': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Porcentaje de avances y descripcion del proceso...'
                }),
        }
        exclude = ['usuario']



class Subir_b(forms.ModelForm):
    # Filtramos los indicadores por una categoría específica (ejemplo: categoría ID=1)
    indicador = forms.ModelChoiceField(
        queryset=Indicador.objects.filter(categoria__eje__modulo__id=2),  # Cambia el filtro según necesites
        empty_label="Selecciona un indicador",
        # label="Indicador"
        widget=forms.Select(attrs={"class": "form-control"})
    )

    subindicador = forms.ModelChoiceField(
        queryset=Subindicador.objects.all(),  # Cambia el filtro según necesites
        empty_label="Selecciona un subindicador",
        widget=forms.Select(attrs={"class": "form-control"})
    )


    class Meta:
        model = Evidencia
        fields = [
            'indicador', 
            'subindicador', 
            'nombre_evidencia',
            'archivo', 
            'comentarios',
            'juicio_valor',
        ]
        widgets = {
            'indicador': forms.Select(attrs={'class': 'form-control'}),
            'subindicador': forms.Select(attrs={'class': 'form-control'}),
            'nombre_evidencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la evidencia...'
                }),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enlace(URL) de evidencia o algun comentario...'
                }),
            'juicio_valor': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Porcentaje de avances y descripcion del proceso...'
                }),
        }
        exclude = ['usuario']


class Subir_c(forms.ModelForm):
    # Filtramos los indicadores por una categoría específica (ejemplo: categoría ID=1)
    indicador = forms.ModelChoiceField(
        queryset=Indicador.objects.filter(categoria__eje__modulo__id=3),  # Cambia el filtro según necesites
        empty_label="Selecciona un indicador",
        # label="Indicador"
        widget=forms.Select(attrs={"class": "form-control"})
    )

    subindicador = forms.ModelChoiceField(
        queryset=Subindicador.objects.all(),  # Cambia el filtro según necesites
        empty_label="Selecciona un subindicador",
        widget=forms.Select(attrs={"class": "form-control"})
    )


    class Meta:
        model = Evidencia
        fields = [
            'indicador', 
            'subindicador', 
            'nombre_evidencia',
            'archivo', 
            'comentarios',
            'juicio_valor',
        ]
        widgets = {
            'indicador': forms.Select(attrs={'class': 'form-control'}),
            'subindicador': forms.Select(attrs={'class': 'form-control'}),
            'nombre_evidencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la evidencia...'
                }),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enlace(URL) de evidencia o algun comentario...'
                }),
            'juicio_valor': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Porcentaje de avances y descripcion del proceso...'
                }),
        }
        exclude = ['usuario']      


class Subir_d(forms.ModelForm):
    # Filtramos los indicadores por una categoría específica (ejemplo: categoría ID=1)
    indicador = forms.ModelChoiceField(
        queryset=Indicador.objects.filter(categoria__eje__modulo__id=4),  # Cambia el filtro según necesites
        empty_label="Selecciona un indicador",
        # label="Indicador"
        widget=forms.Select(attrs={"class": "form-control"})
    )
    subindicador = forms.ModelChoiceField(
        queryset=Subindicador.objects.all(),  # Cambia el filtro según necesites
        empty_label="Selecciona un subindicador",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Evidencia
        fields = [
            'indicador', 
            'subindicador', 
            'nombre_evidencia',
            'archivo', 
            'comentarios',
            'juicio_valor',
        ]
        widgets = {
            'indicador': forms.Select(attrs={'class': 'form-control'}),
            'subindicador': forms.Select(attrs={'class': 'form-control'}),
            'nombre_evidencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la evidencia...'
                }),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enlace(URL) de evidencia o algun comentario...'
                }),
            'juicio_valor': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Porcentaje de avances y descripcion del proceso...'
                }),
        }
        exclude = ['usuario']


class Subir_e(forms.ModelForm):
    # Filtramos los indicadores por una categoría específica (ejemplo: categoría ID=1)
    indicador = forms.ModelChoiceField(
        queryset=Indicador.objects.filter(categoria__eje__modulo__id=5),  # Cambia el filtro según necesites
        empty_label="Selecciona un indicador",
        # label="Indicador"
        widget=forms.Select(attrs={"class": "form-control"})
    )
    subindicador = forms.ModelChoiceField(
        queryset=Subindicador.objects.all(),  # Cambia el filtro según necesites
        empty_label="Selecciona un subindicador",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Evidencia
        fields = [
            'indicador', 
            'subindicador', 
            'nombre_evidencia',
            'archivo', 
            'comentarios',
            'juicio_valor',
        ]
        widgets = {
            'indicador': forms.Select(attrs={'class': 'form-control'}),
            'subindicador': forms.Select(attrs={'class': 'form-control'}),
            'nombre_evidencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la evidencia...'
                }),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enlace(URL) de evidencia o algun comentario...'
                }),
            'juicio_valor': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Porcentaje de avances y descripcion del proceso...'
                }),
        }   
        exclude = ['usuario']


class Subir_f(forms.ModelForm):
    # Filtramos los indicadores por una categoría específica (ejemplo: categoría ID=1)
    indicador = forms.ModelChoiceField(
        queryset=Indicador.objects.filter(categoria__eje__modulo__id=6),  # Cambia el filtro según necesites
        empty_label="Selecciona un indicador",
        # label="Indicador"
        widget=forms.Select(attrs={"class": "form-control"})
    )
    subindicador = forms.ModelChoiceField(
        queryset=Subindicador.objects.all(),  # Cambia el filtro según necesites
        empty_label="Selecciona un subindicador",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Evidencia
        fields = [
            'indicador', 
            'subindicador', 
            'nombre_evidencia',
            'archivo', 
            'comentarios',
            'juicio_valor',
        ]
        widgets = {
            'indicador': forms.Select(attrs={'class': 'form-control'}),
            'subindicador': forms.Select(attrs={'class': 'form-control'}),
            'nombre_evidencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la evidencia...'
                }),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enlace(URL) de evidencia o algun comentario...'
                }),
            'juicio_valor': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Porcentaje de avances y descripcion del proceso...'
                }),
        }            
        exclude = ['usuario']
       

class RevisionForm(forms.ModelForm):
    class Meta:
        model = Evidencia
        fields = [
            'comentarios',
            'juicio_valor',
            'feedback', 
            'status', 
        ]
        widgets = {
            'comentarios': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'juicio_valor' : forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }          


class EditForm(forms.ModelForm):
    class Meta:
        model = Evidencia
        fields = [
            'archivo', 
            'comentarios',
            'juicio_valor',
        ]
        widgets = {
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={'class': 'form-control'}),
            'juicio_valor': forms.Textarea(attrs={'class': 'form-control'}),
        }
        exclude = ['usuario']        