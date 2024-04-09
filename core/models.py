from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# MODELO CATEGORÍA


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['name']

    def __str__(self):
        return self.name


# MODELO DE ETIQUETAS
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        db_table = 'etiqueta'
        ordering = ['name']

    def __str__(self):
        return self.name


# MODELO DE AUTOR = USUARIOS REGISTRADOS EN LA APLICACION => importando la tabla de usuarios


# MODELO DE LOS POSTS
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    excerpt = models.TextField(verbose_name='Bajada')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(
        upload_to='posts', null=True, blank=True, verbose_name='Imagen')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    # Campos con relaciones
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoria')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')

    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        db_table = 'Post'
        ordering = ['-created']

    def __str__(self):
        return self.title


##########################################################

# MODELO ABOUT


# MODELO LINK = REDES SOCIALES
