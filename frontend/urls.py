from django import views
from frontend import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('cerrar_sesion/', views.LogoutView.as_view(), name='logout'),
    path('registrarme/', views.user_register, name='registro'),
    path('inicio/', views.inicio, name='inicio'),
    path('inicio_admin/', views.inicio_admin.as_view(), name='inicio_admin'),
    path('mi_perfil/', views.UserRecordsView.as_view(), name="perfil"),

    # modulos
    path('modulo_a/', views.modulo_a.as_view(), name='modulo_a'),
    path('modulo_b/', views.modulo_b.as_view(), name='modulo_b'),
    path('modulo_c/', views.modulo_c.as_view(), name='modulo_c'),
    path('modulo_d/', views.modulo_d.as_view(), name='modulo_d'),
    path('modulo_e/', views.modulo_e.as_view(), name='modulo_e'),
    path('modulo_f/', views.modulo_f.as_view(), name='modulo_f'),

    # modulos admin
    path('admin_a/', views.AdminAListView.as_view(), name='admin_a'),
    path('admin_b/', views.AdminBListView.as_view(), name='admin_b'),
    path('admin_c/', views.EvidenciaModuloCListView.as_view(), name='admin_c'),
    path('admin_d/', views.EvidenciaModuloDListView.as_view(), name='admin_d'),
    path('admin_e/', views.EvidenciaModuloEListView.as_view(), name='admin_e'),
    path('admin_f/', views.EvidenciaModuloFListView.as_view(), name='admin_f'),

    path('editar/<int:pk>', views.EditView.as_view(), name='editar'),

    # ELIMINAR EVIDENCIA ADMIN
    path('eliminar/<int:pk>/', views.EliminarEvidenciaView.as_view(), name='eliminar_evidencia'),
    path('eliminar_b/<int:pk>/', views.EliminarEvidenciaB.as_view(), name='eliminar_b'),
    path('eliminar_c/<int:pk>/', views.EliminarEvidenciaC.as_view(), name='eliminar_c'),
    path('eliminar_d/<int:pk>/', views.EliminarEvidenciaD.as_view(), name='eliminar_d'),
    path('eliminar_e/<int:pk>/', views.EliminarEvidenciaE.as_view(), name='eliminar_e'),
    path('eliminar_f/<int:pk>/', views.EliminarEvidenciaF.as_view(), name='eliminar_f'),
    path('eliminar_record/<int:pk>/', views.EliminarRecord.as_view(), name='eliminar'),

    # REVISION EVIDENCIA
    path('revision/<int:pk>', views.RevisionView.as_view(), name='revision'),

    # obtener archivos
    path('obtener_evidencia/<int:pdf_id>/', views.obtener_pdf,    name='obtener_pdf'),
    path('download-evidencias/<int:modulo_id>/', views.download_evidencias_zip, name='download_evidencias_zip'),
    path("evidencia/<int:pk>/descargar/", views.descargar_evidencia, name="descargar_evidencia"),

    # notificaciones
    path('notificaciones/', views.NotificacionesView.as_view(), name='notificaciones'),
    path('notificacion/eliminar/<int:pk>/', views.eliminar_notificacion, name='eliminar_notificacion'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)