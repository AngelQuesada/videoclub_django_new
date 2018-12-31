from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(
        'Fecha de nacimiento'
    )
    fecha_defuncion = models.DateField(
        'Fallecido',
        null=True,
        blank=True,
    )
    foto = models.ImageField(
        upload_to='images/actores/',
        default='images/actores/sin_foto.jpg'
    )

    def image_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.foto)))

    image_admin.short_description = 'Foto actual'

    def url_foto(self):
        return settings.MEDIA_URL+str(self.foto)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actores"

class Director(models.Model):
    nombre = models.CharField(
        max_length=100
    )
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(
        'Fallecido',
        null=True,
        blank=True,
    )
    foto = models.ImageField(
        upload_to='images/directores/',
        default='images/directores/sin_foto.jpg'
    )

    def image_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.foto)))

    image_admin.short_description = 'Foto actual'

    def url_foto(self):
        return settings.MEDIA_URL+str(self.foto)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Directores"

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
   
    class Meta:
        verbose_name_plural = "Géneros"

class Pelicula(models.Model):
    titulo = models.CharField(
        max_length=100
    )
    url_trailer = models.CharField(
        max_length=100
    )
    fecha = models.DateField()
    notas_posibles = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    nota = models.IntegerField(
        default=3,
        choices=notas_posibles
    )
    sinopsis = models.TextField(
        max_length=400,
        default="Sin sinopsis"
    )
    caratula = models.ImageField(
        upload_to='images/peliculas/caratulas',
        default='images/peliculas/caratulas/sin_caratula.jpg'
    )
    imagen_promocional = models.ImageField(
        upload_to='images/peliculas/imagenes_promocionales',
        default='images/peliculas/imagenes_promocionales/sin_imagen.jpg'
    )
    genero = models.ManyToManyField(
        Genero,
        blank=True
    )
    director = models.ForeignKey(
        Director,
        on_delete=models.SET('Sin Director')
    ) 
    actores = models.ManyToManyField(
        Actor,
        blank=True
    )

    def caratula_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.caratula)))

    caratula_admin.short_description = 'Carátula actual'

    def imagen_promocional_admin(self):
        return mark_safe("<img style='max-width:220px; max-height:300px' src=\"{}\" />".format(settings.MEDIA_URL+str(self.imagen_promocional)))

    imagen_promocional_admin.short_description = 'Imágen promocional actual'

    def url_imagen_promocional(self):
        return settings.MEDIA_URL+str(self.imagen_promocional)

    def __str__(self):
        return self.titulo

    class Meta():
        verbose_name_plural = "Películas"

class Copia(models.Model):
    fecha_llegada = models.DateField()
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "(ID: {}) {}".format(self.id, self.pelicula.titulo)
  
    class Meta:
        verbose_name_plural = "Copias"
