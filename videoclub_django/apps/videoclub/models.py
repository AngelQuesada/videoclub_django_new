from django.db import models

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField()
    foto = models.ImageField(upload_to = 'media/images/actores/', default = 'media/images/actores/sin_foto.jpg')

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField()
    foto = models.ImageField(upload_to = 'media/images/directores/', default = 'media/images/directores/sin_foto.jpg')

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    notas_posibles = (1, 2, 3, 4, 5)
    nota = models.IntegerField(default=0, choices=notas_posibles)
    caratula = models.ImageField(upload_to = 'media/images/peliculas/', default = 'media/images/peliculas/sin_caratula.jpg')
    genero = models.ManyToManyField(Genero, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete = models.SET_NULL) 
    actores = models.ForeignKey(Actor, on_delete=models.SET_NULL)

class Copia(models.Model):
    fecha_llegada = models.DateField()
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
