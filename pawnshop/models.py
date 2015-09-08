from django.db import models

# Create your models here.

from django.utils.translation import ugettext as _

class Soul(models.Model):
	SOUL_KINDS = (
		('OW', _('Master')),
		('PM', _('Slave')),
		('CL', _('Cadger')),
	)
	
	name = models.CharField(verbose_name=_("name"), max_length=200, unique=True, null=False)
	key = models.CharField(verbose_name=_("key"), max_length=200, blank=True)
	kind = models.CharField(max_length=2, choices=SOUL_KINDS)
	reg_data = models.DateTimeField(verbose_name=_('date registered'), auto_now_add=True, editable=False)

	def __str__(self):
		return self.name
		
class Swag(models.Model):
	owner = models.ForeignKey(Soul)
	name = models.CharField(verbose_name=_("name"), max_length=200, unique=True, null=False)
	cost = models.IntegerField(default=0, verbose_name=_("cost"))
	take_data = models.DateTimeField(_('date came'), auto_now_add=True)

	def __str__(self):
		return self.name
