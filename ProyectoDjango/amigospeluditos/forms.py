from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Usuario

GENERO_CHOICES = [
    ('', 'Seleccionar'),
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Otro', 'Otro'),
]
DISPONIBILIDAD_CHOICES = [
    ('', 'Seleccionar'),
    ('En Stock', 'En Stock'),
    ('Sin Stock', 'Sin Stock'),
]

CATEGORIA_CHOICES = [
    ('', 'Selecionar'),
    ('Alimento', 'Alimento'),
    ('Prenda', 'Prenda'),
    ('Accesorio', 'Accesorio'),
]

class UsuarioForm(UserCreationForm):
    """ Formulario de registro de un usuario en la base de datos
    
    Variables:
        - password1: Contraseña
        - password2: Validación de contraseña

    """
    password1 = forms.CharField(label = 'Contraseña', min_length = 8, max_length = 20, widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label = 'Confirmación de contraseña', min_length = 8, max_length = 20, widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña nuevamente',
            'id': 'password2',
            'required': 'required',
        }
    ))

    mostrar_password1 = forms.BooleanField(label = 'Mostrar contraseña', required = False, widget = forms.CheckboxInput(
        attrs = {
            'class': 'form-check-input',
            'id': 'mostrarPassword1',
        }
    ))

    mostrar_password2 = forms.BooleanField(label = 'Mostrar confirmación de contraseña', required = False, widget = forms.CheckboxInput(
        attrs = {
            'class': 'form-check-input',
            'id': 'mostrarPassword2',
        }
    ))

    genero = forms.ChoiceField(label = 'Género', choices = GENERO_CHOICES, widget = forms.Select(
        attrs = {
            'class': 'form-control',
            'id': 'genero',
            'required': 'required',
        }
    ))

    rut = forms.CharField(min_length = 11, max_length = 12, validators = [RegexValidator(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$', 'Ingrese un RUT válido')], widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ej: 21.155.907-1',
            'id': 'rut',
            'required': 'required',
        }
    ))

    celular = forms.CharField(min_length = 9, max_length = 9, validators = [RegexValidator(r'^9[0-9]{8}$', 'Ingrese un número de celular válido, este siempre debe partir con 9')], widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su número de celular',
            'id': 'celular',
            'required': 'required',
        }
    ))
    
    email = forms.EmailField(widget = forms.EmailInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                    'id': 'email',
                    'required': 'required',
                }
        ),
        error_messages = {
            'invalid': 'Por favor, ingrese un correo electrónico válido.'
        }
    )

    nombre_de_usuario = forms.CharField(min_length = 5, max_length = 20, validators = [RegexValidator(r'^[a-zA-ZñÑ\s]+$', 'El nombre de solo puede contener letras y espacios.')], widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'nombre_de_usuario',
            'required': 'required',
        }
    ))

    nombre = forms.CharField(min_length = 1, max_length = 45, validators = [RegexValidator(r'^[a-zA-ZñÑ\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF\s]+$', 'El nombre solo puede contener letras con o sin tilde y espacios.')], widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre',
            'id': 'nombre',
            'required': 'required',
        }
    ))

    apellidos = forms.CharField(min_length = 4, max_length = 50, validators = [RegexValidator(r'^[a-zA-ZñÑ\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF\s]+$', 'Los apellidos solo puede contener letras con o sin tilde y espacios.')], widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese sus apellidos',
            'id': 'apellidos',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ['nombre_de_usuario', 'nombre', 'apellidos', 'celular', 'rut', 'email', 'genero', 'password1', 'mostrar_password1', 'password2']

    def clean_nombre_de_usuario(self):
        nombre_de_usuario = self.cleaned_data.get('nombre_de_usuario')
        if Usuario.objects.filter(nombre_de_usuario = nombre_de_usuario).exists():
            raise forms.ValidationError('¡Ya existe una cuenta con ese nombre de usuario!')
        return nombre_de_usuario

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if Usuario.objects.filter(rut = rut).exists():
            raise forms.ValidationError('¡Ya existe una cuenta con ese rut!')
        return rut

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email = email).exists():
            raise forms.ValidationError('¡Ya existe una cuenta con ese correo electrónico!')
        return email
    
    def clean_password2(self):
        """Validación de contraseña

        Válida que ambas contraseñas al momento de ingresarse en el formulario sean iguales. Retorna contraseña válida.

        Excepciones:
            - ValidationError = Cuando las contraseñas no son iguales, muestra mensaje de error.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('¡Contraseñas no coinciden!')
        return password2

class ProductoForm(forms.ModelForm):
    disponibilidad = forms.ChoiceField(choices = DISPONIBILIDAD_CHOICES, widget = forms.Select(
        attrs = {
            'class': 'form-control',
            'id': 'disponibilidad',
            'required': 'required',
        }
    ))

    categoria = forms.ChoiceField(label = 'Categoría', choices = CATEGORIA_CHOICES, widget = forms.Select(
        attrs = {
            'class': 'form-control',
            'id': 'disponibilidad',
            'required': 'requiered',
        }
    ))
    
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo_sku', 'descripcion', 'precio', 'disponibilidad', 'acerca_de', 'imagen', 'categoria']
        labels = {
            'codigo_sku': 'Código SKU',
            'descripcion': 'Descripción',
        }
        widgets = {
 
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese nombre del producto',
                    'id': 'nombre',
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'codigo_sku': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese el código SKU del producto',
                    'id': 'codigo_sku',
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'descripcion': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese una descripción para el producto',
                    'id': 'descripcion',
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'precio': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese el precio del producto',
                    'id': 'precio',
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'acerca_de': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese información del producto',
                    'id': 'acerca_de',
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'class':'form-control',
                    'id':'imagen',
                    'required': 'required',
                }
            )
        }