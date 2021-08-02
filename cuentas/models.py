from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage

#from typing_extensions import TypeVarTuple

# Create your models here.

class Meta:
    model = User
    fields = ("username",)

class Perfiles(models.Model):
    """
        Creamos un modelo para el manejo de perfiles(tabla)
    """
    GENERO = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )
    ESTADO_CIVIL = (
        ('s', 'Soltero'),
        ('c', 'Casado'),
        ('d', 'Divorciado'),
        ('v', 'Viudo'),
    )
    ROL = (
        ('a','Administrador'),
        ('u','Usuario'),
        ('e','Especialista'),
    )
    ESTATUS = (
        ('f','Usuario destacado'),
        ('c','Creador de contenido'),
        ('u','Usuario nuevo'),
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usu')
    foto = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='media/', default='media/anonimo.png')
    genero = models.CharField('Genero', max_length=1, choices=GENERO, blank=True, null=True)
    biografia = models.TextField('Descripcion de bigrafia', blank=True, null=True)
    fecNacimiento = models.DateField('Fecha de nacimiento', blank=True, null=True)
    rol = models.CharField('Rol', max_length=1, choices=ROL, default='u')
    estatus = models.CharField('Estatus', max_length=1, default='u',choices=ESTATUS)
    direccion = models.TextField('Direccion',blank=True, null=True)
    url_website = models.CharField('Web Site', max_length=255, blank=True, null=True)
    url_twitter = models.CharField('Twitter', max_length=255, blank=True, null=True)
    url_instagram = models.CharField('Instagram', max_length=255, blank=True, null=True)
    url_facebook = models.CharField('Facebook', max_length=255, blank=True, null=True)
    data_modificada = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.username

class Categorias(models.Model):
    """
        Se crea un modelo de categorias para que las publicaciones puedan separarse por categorias(tabla)
    """
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


"""class Publicaciones(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfiles, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=255)
    publicacion = RichTextField()
    #imagen = models.ImageField(upload_to='')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    #borrador = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True, default='admin')
    vistas = models.PositiveIntegerField(default=0)
    categoria = models.ManyToManyField(Categorias)

    class Meta:
        ordering = ('titulo',)
    
    def __str__(self):
        return '{} by @{}'.format(self.titulo, self.usuario.username)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Publicaciones, self).save(*args, **kwargs)    """

class Articulos(models.Model):

    HOME_MAIN = "HM"
    BUTTOM_MAIN = "BM"
    TOP_MAIN = "TM"
    POSICION = [(HOME_MAIN, "HOME_MAIN"),(BUTTOM_MAIN, "BOTTOM_MAIN"),(TOP_MAIN, "TOP_MAIN"),]
    id = models.PositiveIntegerField(primary_key=True)
    titulo = models.CharField(max_length=100, unique=False , null = True)
    autor = models.CharField(max_length=100, unique=False  , null = True)
    palabras_clave = models.CharField(max_length=200, unique=False, null = True)
    pub_fecha = models.DateField(null = True)
    resumen = models.TextField(null= True)
    contenido = models.TextField(null=True)
    art_archivo = models.FileField(upload_to='documents/', blank=True, null = True)
    imagen = models.ImageField('Imagen', default='',upload_to='articulos/', height_field=None, width_field=None,blank=True, null=True)
    #posicion = models.CharField(max_length=50, choices=POSICION, default = TOP_MAIN)
    categoria = models.ForeignKey(Categorias, on_delete=(models.RESTRICT), null = True)

    def __str__(self):
        return self.titulo


class Comentarios_publicacion(models.Model):
    """
        Se crea un modelo para que un usuario pueda realizar comentarios(tabla)
    """
    perfil = models.ForeignKey(Perfiles, on_delete=models.PROTECT)
    articulo = models.ForeignKey(Articulos, on_delete=models.PROTECT)
    comentario = models.TextField(null=True)
    fecha_publicacion = models.DateField(auto_now=True)
    def __str__(self):
        return self.comentario


"""class Comentarios_articulo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfiles, on_delete=models.PROTECT)
    articulo = models.ForeignKey(Articulos, on_delete=models.PROTECT)
    comentario = models.TextField(null=True)
    reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')"""
    