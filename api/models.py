from django.db import models
from django.contrib.auth.models import User


class Ures(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    ures        = models.ForeignKey(Ures, on_delete=models.CASCADE)
    matricula   = models.CharField(max_length=10, null=True, blank=True)
    nombre      = models.CharField(max_length=90, null=True, blank=True)
    apellido    = models.CharField(max_length=90, null=True, blank=True)

    @property
    def notificaciones_no_leidas(self):
        return self.user.notificaciones.filter(leida=False).count()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.matricula}) - {self.user.username}"



# Modulo
class Modulo(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

# Eje
class Eje(models.Model):
    modulo      = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='ejes')
    nombre      = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


# Categoria
class Categoria(models.Model):
    eje         = models.ForeignKey(Eje, on_delete=models.CASCADE, related_name="categorias")
    nombre      = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.eje} - {self.nombre}"
    

# Indicador
class Indicador(models.Model):
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='indicadores')
    nombre      = models.CharField(max_length=255)
    estandar    = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.estandar}"
    

# Subindicador
class Subindicador(models.Model):
    letra = models.CharField(max_length=5)
    
    def __str__(self):
        return self.letra 


class Evidencia(models.Model):
    ESTADO = [
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En revisión'),
        ('aprobado', 'Aprobado'),
    ]

    indicador       = models.ForeignKey(Indicador,      on_delete=models.CASCADE, related_name='evidencias')
    subindicador    = models.ForeignKey(Subindicador,   on_delete=models.CASCADE, related_name='evidencias')
    usuario         = models.ForeignKey(User,           on_delete=models.CASCADE, related_name='evidencias')
    nombre_evidencia = models.CharField(max_length=255)
    archivo         = models.FileField(upload_to="evidencias/", blank=True, null=True)
    comentarios     = models.TextField(null=True, blank=True)
    juicio_valor    = models.TextField(null=True, blank=True)  
    feedback        = models.TextField(null=True, blank=True)
    status          = models.CharField(max_length=20, choices=ESTADO, default='pendiente')

    def save(self, *args, **kwargs):
        # Solo crear notificación si la evidencia ya existía
        if self.pk:
            old_status = Evidencia.objects.get(pk=self.pk).status
            if old_status != self.status:
                from .models import Notificacion

                if self.status == 'en_revision':
                    mensaje = f"Tu evidencia '{self.nombre_evidencia}' ha pasado a revisión."
                elif self.status == 'aprobado':
                    mensaje = f"🎉 Tu evidencia '{self.nombre_evidencia}' ha sido aprobada."
                else:
                    mensaje = f"El estado de tu evidencia '{self.nombre_evidencia}' cambió a {self.status}."

                # Crear la notificación
                Notificacion.objects.create(usuario=self.usuario, mensaje=mensaje)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_evidencia} - {self.usuario}"


class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación para {self.usuario.username} - {self.mensaje[:40]}"


# Para poder usar user.notificaciones_no_leidas directamente en templates
User.add_to_class('notificaciones_no_leidas', Profile.notificaciones_no_leidas)
