from django.db import models
from cmn.etc import dbg

class AbsModel01(models.Model):
	field1 = models.CharField('f1', max_length=255,)
	class Meta:
		abstract = True

class AbsModel02(models.Model):
	field2 = models.CharField('f2', max_length=255,)
	class Meta:
		abstract = True
		
class Mixed1(AbsModel01, AbsModel02):
	field3 = models.CharField('f3', max_length=255,)
	#class Meta:
		#abstract = False
		
class Mixed2(AbsModel01, AbsModel02):
	#class Meta:
		#abstract = False
	pass
		
class AbsDecor01:
	def test1(self):
		dbg('test1')

class Mixed3(AbsModel01, AbsDecor01):
	field4 = models.CharField('f4', max_length=255,)
		