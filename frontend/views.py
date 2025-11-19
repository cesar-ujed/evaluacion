from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from api.models import *
from django.views.generic.edit import FormView
from .forms import *
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse, Http404
import os
import zipfile
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import Count, Q
from django.views.generic import TemplateView
from django.db import IntegrityError



# ;;;;;;;;;;;;;;;;;; REGISTRO ;;;;;;;;;;;;;;;;;
def user_register(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1']
                )
                user.save()
                messages.success(request, 'Usuario creado correctamente.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'El usuario ya existe')
                return render(request, 'signup.html', {
                    'form': UserCreationForm()
                })
        messages.error(request, 'Las contraseñas no coinciden')
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    
    

# ;;;;;;;;;;;; LOGIN ;;;;;;;;;;;;;;;;
class LoginView(FormView):
    template_name = 'login.html'  # Ruta al archivo de plantilla
    form_class = BootstrapAuthenticationForm
    success_url = reverse_lazy('inicio')  # Redirigir después de iniciar sesión

    def dispatch(self, request, *args, **kwargs):
        """Cierra la sesión antes de procesar cualquier solicitud a esta vista"""
        logout(request)  # Cierra cualquier sesión activa
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Inicia sesión al validar el formulario"""
        user = form.get_user()  # Obtiene el usuario autenticado
        login(self.request, user)  # Inicia la sesión del usuario
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        """Maneja el caso en que el formulario no es válido (credenciales incorrectas)"""
        messages.error(self.request, "Usuario o contraseña incorrectos.")  # Envía un mensaje de error
        return super().form_invalid(form)  # Vuelve a mostrar el formulario con errores

    def get_success_url(self):
        """Redirigir después del login, con soporte para ?next="" en la URL"""
        return self.request.GET.get('next', self.success_url)
    

# ;;;;;;;;;;; CERRAR SESIÓN ;;;;;;;;;;;;;;
class LogoutView(View):
    def get(self, request):
        # Cierra la sesión del usuario
        logout(request)
        # Redirige a la página de inicio u otra página después de cerrar la sesión
        return redirect(reverse('login'))    
    

# ;;;;;;;;;;;;; INICIO USUARIO ;;;;;;;;;;;;
def inicio(request):
    hora_actual = timezone.now()

    return render(request, "inicio.html", {'hora_actual': hora_actual})


# ;;;;;;;;;;;;;; INICIO ADMIN ;;;;;;;;;;;;;;
# def inicio_admin(request):
#     return render(request, "inicio_admin.html")


class inicio_admin(TemplateView):
    template_name = "inicio_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Totales de evidencias por estatus
        resumen = Evidencia.objects.aggregate(
            total=Count("id"),
            pendientes=Count("id", filter=Q(status="pendiente")),
            en_revision=Count("id", filter=Q(status="en_revision")),
            aprobados=Count("id", filter=Q(status="aprobado")),
        )

        context["resumen"] = resumen
        return context


# ;;;;;;;;;;;;;; PERFIL ;;;;;;;;;;;;;;;;
class UserRecordsView(LoginRequiredMixin, ListView):
    template_name = 'perfil.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Evidencia.objects.filter(usuario=self.request.user).order_by('-id')
    

# ELIMINAR EVIDENCIA
class EliminarRecord(DeleteView):
    model = Evidencia
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('perfil')     


# ;;;;;;;;;;;; MODULO A ;;;;;;;;;;;;
class modulo_a(CreateView):
    model = Evidencia.objects.order_by('id')
    template_name = 'subir_a.html'
    form_class = Subir_a
    success_url = reverse_lazy('perfil')
    ordering = 'id'

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # ¡Clave aquí!
        response = super().form_valid(form)
        messages.success(self.request, "¡Evento guardado correctamente!")
        return response


# ;;;;;;;;;;;;;; MODULO B ;;;;;;;;;;;;;;
class modulo_b(CreateView):
    model = Evidencia
    template_name = 'subir_b.html'
    form_class = Subir_b
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # ¡Clave aquí!
        response = super().form_valid(form)
        messages.success(self.request, "¡Evento guardado correctamente!")
        return response    


# ;;;;;;;;;;;; MODULO C ;;;;;;;;;;;;;
class modulo_c(CreateView):
    model = Evidencia
    template_name = 'subir_c.html'
    form_class = Subir_c
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # ¡Clave aquí!
        response = super().form_valid(form)
        messages.success(self.request, "¡Evento guardado correctamente!")
        return response


# ;;;;;;;;;;;;; MODULO D ;;;;;;;;;;;;;
class modulo_d(CreateView):
    model = Evidencia
    template_name = 'subir_d.html'
    form_class = Subir_d
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # ¡Clave aquí!
        response = super().form_valid(form)
        messages.success(self.request, "¡Evento guardado correctamente!")
        return response     


# ;;;;;;;;;;;;; MODULO E ;;;;;;;;;;;;;;
class modulo_e(CreateView):
    model = Evidencia
    template_name = 'subir_e.html'
    form_class = Subir_e
    success_url = reverse_lazy('perfil') 

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # ¡Clave aquí!
        response = super().form_valid(form)
        messages.success(self.request, "¡Evento guardado correctamente!")
        return response    


# ;;;;;;;;;;;; MODULO F ;;;;;;;;;;;;;;;
class modulo_f(CreateView):
    model = Evidencia
    template_name = 'subir_f.html'
    form_class = Subir_f
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # ¡Clave aquí!
        response = super().form_valid(form)
        messages.success(self.request, "¡Evento guardado correctamente!")
        return response



# ;;;;;;;;;;;; MODULO A ADMIN ;;;;;;;;;;;
class AdminAListView(ListView):
    model = Evidencia
    template_name = 'admin_a.html'
    context_object_name = 'evidencias'

    def get_queryset(self):
        # Primero filtramos por Módulo A
        queryset = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=1
        ).select_related(
            'usuario', 'indicador', 'subindicador'
        ).order_by('id')
        
        # Luego aplicamos búsqueda si hay parámetro 'q'
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nombre_evidencia__icontains=search_query) |
                Q(indicador__nombre__icontains=search_query) |
                Q(usuario__username__icontains=search_query) 
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')
        context['search_query'] = search_query

        # Conteos por status
        evidencias_modulo = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=1
        )
        context['total_evidencias'] = evidencias_modulo.count()
        context['pendientes'] = evidencias_modulo.filter(status='pendiente').count()
        context['en_revision'] = evidencias_modulo.filter(status='en_revision').count()
        context['aprobados'] = evidencias_modulo.filter(status='aprobado').count()

        return context


def download_evidencias_zip(request, modulo_id):  # <- ¡Añade el parámetro aquí!
    # Filtra las evidencias por el módulo recibido en la URL
    evidencias = Evidencia.objects.filter(
        indicador__categoria__eje__modulo__id=modulo_id
    )
    
    search_query = request.GET.get('q')
    if search_query:
        evidencias = evidencias.filter(
            Q(nombre_evidencia__icontains=search_query) |
            Q(indicador__nombre__icontains=search_query) |
            Q(usuario__username__icontains=search_query)
        ).distinct()

    # Crear un archivo zip en memoria
    response = HttpResponse(content_type='application/zip')
    zip_filename = f"evidencias_modulo_{modulo_id}_{timezone.now().strftime('%Y-%m-%d_%H-%M')}.zip"
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'

    with zipfile.ZipFile(response, 'w') as zipf:
        for evidencia in evidencias:
            # Suponiendo que el modelo Evidencia tiene un campo "archivo" (FileField)
            if evidencia.archivo:
                file_path = evidencia.archivo.path
                if os.path.exists(file_path):
                    # Usamos el nombre del archivo original o uno basado en el nombre de la evidencia
                    arcname = slugify(evidencia.nombre_evidencia) + os.path.splitext(file_path)[1]
                    zipf.write(file_path, arcname)

    return response

# ELIMINAR EVIDENCIA
class EliminarEvidenciaView(DeleteView):
    model = Evidencia
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('admin_a') 

class EliminarEvidenciaB(DeleteView):
    model = Evidencia
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('admin_b')

class EliminarEvidenciaC(DeleteView):
    model = Evidencia
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('admin_c')

class EliminarEvidenciaD(DeleteView):
    model = Evidencia
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('admin_d')

class EliminarEvidenciaE(DeleteView):
    model = Evidencia
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('admin_e')

class EliminarEvidenciaF(DeleteView):
    model = Evidencia
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('admin_f')        


class RevisionView(UpdateView):
    model = Evidencia
    template_name = 'revision.html'
    form_class = RevisionForm

    # Redirección dinámica según módulo
    def get_success_url(self):
        evidencia = self.get_object()
        modulo_nombre = evidencia.indicador.categoria.eje.modulo.nombre.lower()  # "A", "B", etc.
        
        url_map = {
            "módulo a": "admin_a",
            "módulo b": "admin_b",
            "módulo c": "admin_c",
            "módulo d": "admin_d",
            "módulo e": "admin_e",
            "módulo f": "admin_f",
        }
        url_name = url_map.get(modulo_nombre, "admin_a")
        return reverse_lazy(url_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evidencia = self.get_object()
        context['archivo_url'] = evidencia.archivo.url if evidencia.archivo else None
        return context

# ;;;;;;;;;;;;; Editar en perfil ;;;;;;;;;;;;;;
class EditView(UpdateView):
    model = Evidencia
    template_name = 'editar.html'
    form_class = EditForm
    success_url = reverse_lazy('perfil')      


# ;;;;;;;;;;;;;;; Funciones ;;;;;;;;;;;;;;
def obtener_pdf(request, pdf_id):
    pdf = get_object_or_404(Evidencia, pk = pdf_id)
    response = FileResponse(pdf.archivo, content_type='application/pdf')
    return response


def descargar_evidencia(request, pk):
    try:
        evidencia = Evidencia.objects.get(pk=pk, usuario=request.user)
    except Evidencia.DoesNotExist:
        raise Http404("Evidencia no encontrada")

    if not evidencia.archivo:
        raise Http404("El archivo no existe")

    file_path = evidencia.archivo.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))


# ;;;;;;;;;;;; MODULO B ADMIN ;;;;;;;;;;;
class AdminBListView(ListView):
    model = Evidencia
    template_name = 'admin_b.html'
    context_object_name = 'evidencias'

    def get_queryset(self):
        # Primero filtramos por Módulo B
        queryset = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=2
        ).select_related(
            'usuario', 'indicador', 'subindicador'
        ).order_by('id')
        
        # Luego aplicamos búsqueda si hay parámetro 'q'
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nombre_evidencia__icontains=search_query) |
                Q(indicador__nombre__icontains=search_query) |
                Q(usuario__username__icontains=search_query) 

            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')
        context['search_query'] = search_query

        # Conteos por status para Módulo B
        evidencias_modulo = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=2
        )
        context['total_evidencias'] = evidencias_modulo.count()
        context['pendientes'] = evidencias_modulo.filter(status='pendiente').count()
        context['en_revision'] = evidencias_modulo.filter(status='en_revision').count()
        context['aprobados'] = evidencias_modulo.filter(status='aprobado').count()

        return context
    

# ;;;;;;;;;;;; MODULO C ADMIN ;;;;;;;;;;;
class EvidenciaModuloCListView(ListView):
    model = Evidencia
    template_name = 'admin_c.html'  # Template específico
    context_object_name = 'evidencias'

    def get_queryset(self):
        # Primero filtramos por Módulo C
        queryset = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=3
        ).select_related(
            'usuario', 'indicador', 'subindicador'
        ).order_by('id')
        
        # Luego aplicamos búsqueda si hay parámetro 'q'
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nombre_evidencia__icontains=search_query) |
                Q(indicador__nombre__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')
        context['search_query'] = search_query

        # Conteos por status para Módulo B
        evidencias_modulo = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=3
        )
        context['total_evidencias'] = evidencias_modulo.count()
        context['pendientes'] = evidencias_modulo.filter(status='pendiente').count()
        context['en_revision'] = evidencias_modulo.filter(status='en_revision').count()
        context['aprobados'] = evidencias_modulo.filter(status='aprobado').count()

        return context

# ;;;;;;;;;;;;;; MODULO D ;;;;;;;;;;;
class EvidenciaModuloDListView(ListView):
    model = Evidencia
    template_name = 'admin_d.html'  # Template específico
    context_object_name = 'evidencias'

    def get_queryset(self):
        # Primero filtramos por Módulo A
        queryset = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=4
        ).select_related(
            'usuario', 'indicador', 'subindicador'
        ).order_by('id')
        
        # Luego aplicamos búsqueda si hay parámetro 'q'
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nombre_evidencia__icontains=search_query) |
                Q(indicador__nombre__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')
        context['search_query'] = search_query

        # Conteos por status para Módulo B
        evidencias_modulo = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=4
        )
        context['total_evidencias'] = evidencias_modulo.count()
        context['pendientes'] = evidencias_modulo.filter(status='pendiente').count()
        context['en_revision'] = evidencias_modulo.filter(status='en_revision').count()
        context['aprobados'] = evidencias_modulo.filter(status='aprobado').count()

        return context
    

# ;;;;;;;;;;;;;; MODULO E ;;;;;;;;;;;
class EvidenciaModuloEListView(ListView):
    model = Evidencia
    template_name = 'admin_e.html'  # Template específico
    context_object_name = 'evidencias'

    def get_queryset(self):
        # Primero filtramos por Módulo E
        queryset = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=5
        ).select_related(
            'usuario', 'indicador', 'subindicador'
        ).order_by('id')
        
        # Luego aplicamos búsqueda si hay parámetro 'q'
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nombre_evidencia__icontains=search_query) |
                Q(indicador__nombre__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')
        context['search_query'] = search_query

        # Conteos por status para Módulo B
        evidencias_modulo = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=5
        )
        context['total_evidencias'] = evidencias_modulo.count()
        context['pendientes'] = evidencias_modulo.filter(status='pendiente').count()
        context['en_revision'] = evidencias_modulo.filter(status='en_revision').count()
        context['aprobados'] = evidencias_modulo.filter(status='aprobado').count()

        return context
    

# ;;;;;;;;;;;;;; MODULO F ;;;;;;;;;;;
class EvidenciaModuloFListView(ListView):
    model = Evidencia
    template_name = 'admin_f.html'  # Template específico
    context_object_name = 'evidencias'

    def get_queryset(self):
        # Primero filtramos por Módulo F
        queryset = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=6
        ).select_related(
            'usuario', 'indicador', 'subindicador'
        ).order_by('id')
        
        # Luego aplicamos búsqueda si hay parámetro 'q'
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(nombre_evidencia__icontains=search_query) |
                Q(indicador__nombre__icontains=search_query) |
                Q(usuario__username__icontains=search_query) 

            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')
        context['search_query'] = search_query

        # Conteos por status para Módulo B
        evidencias_modulo = Evidencia.objects.filter(
            indicador__categoria__eje__modulo__id=6
        )
        context['total_evidencias'] = evidencias_modulo.count()
        context['pendientes'] = evidencias_modulo.filter(status='pendiente').count()
        context['en_revision'] = evidencias_modulo.filter(status='en_revision').count()
        context['aprobados'] = evidencias_modulo.filter(status='aprobado').count()

        return context   
    

class NotificacionesView(ListView):
    model = Notificacion
    template_name = 'notificaciones.html'
    context_object_name = 'notificaciones'

    def get_queryset(self):
        # Solo mostrar notificaciones del usuario autenticado
        return Notificacion.objects.filter(usuario=self.request.user).order_by('-fecha')    
       

def eliminar_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    notificacion.delete()
    messages.success(request, "Notificación eliminada correctamente.")
    return redirect('notificaciones')  # o el nombre de tu vista/lista      



# CATEGORIAS

class CategoriasCreateView(CreateView):
    model = Categoria
    template_name = 'categoria_create.html'
    form_class = CategoriaEditForm
    success_url = reverse_lazy('categorias')

    def form_valid(self, form):
        # form.instance.usuario = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "¡Evento guardado correctamente!")
        return response


class CategoriasListView(ListView):
    model = Categoria
    template_name = 'categorias.html' 
    context_object_name = 'categorias'
    ordering = 'id'


class DeleteCategoria(DeleteView):
    model = Categoria
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('categorias')


class EditCategoriaView(UpdateView):
    model = Categoria
    template_name = 'categorias_edit.html'
    form_class = CategoriaEditForm
    success_url = reverse_lazy('categorias')   


# Indicador

class IndicadorCreateView(CreateView):
    model = Indicador
    template_name = 'indicador_create.html'
    form_class = IndicadorForm
    success_url = reverse_lazy('indicadores')

    def form_valid(self, form):
        # form.instance.usuario = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "¡Indicador guardado correctamente!")
        return response
    

class IndicadorListView(ListView):
    model = Indicador
    template_name = 'indicadores.html' 
    context_object_name = 'indicadores'
    ordering = 'id'


class DeleteIndicador(DeleteView):
    model = Indicador
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('indicadores')


class EditIndicadorView(UpdateView):
    model = Indicador
    template_name = 'indicadores_edit.html'
    form_class = IndicadorForm
    success_url = reverse_lazy('indicadores')   




