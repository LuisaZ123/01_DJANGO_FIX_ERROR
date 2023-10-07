from django.db import models

# Create your models here.
class libros (models.Model):

    Tipo = models.CharField (max_length= 100, null= False, blank = False )
    Título = models.CharField (max_length= 400, null= False, blank = False)
    Fecha_de_publicación = models.CharField (max_length= 100, null= False, blank = False)
    Editorial = models.CharField (max_length= 100, null= False, blank = False)