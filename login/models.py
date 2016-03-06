from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



def fotos_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'skill_{0}/{1}'.format(instance.pk, filename)


def validate_even(value):
    if value < 1 or value > 5:
        raise ValidationError(
            _('%(value)s Puntuacion de 1 a 5'),
            params={'value': value},
        )

# Create your models here.
class Chofer(models.Model):
	class Meta:
		verbose_name='Chofer'
		verbose_name_plural='Choferes'

	#Attributs
	usr = models.OneToOneField(User)
	img = models.ImageField(upload_to = fotos_directory_path, blank=False)
	nombre = models.CharField(max_length=50,blank=False)
	apellido_paterno = models.CharField(max_length=50,blank=False)
	apellido_materno = models.CharField(max_length=50,blank=False)
	placa = models.CharField(max_length=50,blank=False)
	vehiculo = models.CharField(max_length=50,blank=False)
	salida = models.CharField(max_length=50,blank=False)
	destino = models.CharField(max_length=50,blank=False)

	def __str__(self):
		return (self.nombre)


class Usuario(models.Model):
	class Meta:
		verbose_name='Usuario'
		verbose_name_plural='Usuarios'

	#Attributs
	usr = models.OneToOneField(User)
	puntuacion = models.IntegerField(validators=[validate_even])
	comentario = models.TextField(max_length= 300)

	def __str__(self):
		return (self.usr.username)



class Rankin(models.Model):
	class Meta:
		verbose_name='Rankin'
		verbose_name_plural='Rankins'

	rankin_usuario = models.ForeignKey(Usuario)
	rankin_global = models.ForeignKey(Chofer)

	def __str__(self):
		return (self.rankin_usuario.usr , self.rankin_global.usr )



	



