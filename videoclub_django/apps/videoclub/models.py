from django.db import models

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(
        null=True,
        blank=True,
    )
    foto = models.ImageField(
        upload_to = 'media/images/actores/', 
        default = 'media/images/actores/sin_foto.jpg'
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Actores"

class Director(models.Model):
    nombre = models.CharField(
        max_length=100
    )
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField()
    foto = models.ImageField(
        upload_to = 'media/images/directores/',
        default = 'media/images/directores/sin_foto.jpg'
    )

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
        ("1", "1/5"),
        ("2", "2/5"),
        ("3", "3/5"),
        ("4", "4/5"),
        ("5", "5/5")
    )
    nota = models.IntegerField(
        default=0,
        choices=notas_posibles
    )
    caratula = models.ImageField(
        upload_to='media/images/peliculas/',
        default='media/images/peliculas/sin_caratula.jpg'
    )
    genero = models.ManyToManyField(
        Genero,
        blank=True
    )
    director = models.ForeignKey(
        Director,
        on_delete=models.SET('Sin Director')
    ) 
    actores = models.ForeignKey(
        Actor,
        on_delete=models.SET('Sin actor')
    )

    def __str__(self):
        return self.nombre

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
