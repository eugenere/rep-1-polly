from django.db import models

from django.utils import timezone
from datetime import datetime

class ModelMetaTools:
	def setVerbose_name(self, aFieldName, aVerboseName):
		self._meta.get_field(aFieldName).verbose_name = aVerboseName
	class Meta:
		abstract = True
		
class DateTracked(models.Model):
	created_at = models.DateTimeField('Дата создания', auto_now_add=True,)
	updated_at = models.DateTimeField('Дата изменения', auto_now=True,)
	class Meta:
		abstract = True
	
	
class PersInfo(models.Model):
	first_name = models.CharField('Имя', max_length=255,)
	family = models.CharField('Фимилия', max_length=255,)
	surname = models.CharField('Отчество', max_length=255,)
	passportCode = models.CharField('Паcпорт', max_length=255,)
	address = models.CharField('Место прописки', max_length=255,)
	class Meta:
		abstract = True		
	def __str__(self):
		return self.family + ' ' + self.name

		
class User(DateTracked):
	login = models.CharField(
		'Логин', max_length=255, unique=True, primary_key=True)
	key = models.CharField(
		'Ключ', max_length=255,)
	class Meta:
		ordering = ['login']		
	def __str__(self):
		return self.login
		
		
class Owner(User):
	class Meta:
		verbose_name = 'Владелец'
		verbose_name_plural = 'Владелецы'

		
class Cashier(User, PersInfo, ModelMetaTools):
	def __init__(self, *args, **kwargs):
		super(Cashier, self).__init__(*args, **kwargs)
		self.setVerbose_name("created_at", 'Дата приема')
	def __str__(self):
		return PersInfo.__str__(self)
	class Meta:
		verbose_name = 'Кассир'
		verbose_name_plural = 'Кассиры'
		ordering = ['family']
		
		
class Client(PersInfo, DateTracked, ModelMetaTools):
	def __init__(self, *args, **kwargs):
		super(Client, self).__init__(*args, **kwargs)
		self.setVerbose_name("created_at", 'Дата регистрации')
	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'

		
class Pledge(DateTracked, ModelMetaTools):
	pledger = models.ForeignKey(Client, verbose_name="Залогодатель")
	acceptor = models.ForeignKey(User, verbose_name="Приемщик")
	description = models.CharField('Описание', max_length=255)
	price = models.PositiveIntegerField('Стоимость')
	term = models.PositiveIntegerField('Срок залога')
	def __init__(self, *args, **kwargs):
		super(Pledge, self).__init__(*args, **kwargs)
		self.setVerbose_name("created_at", 'Дата приема')
	class Meta:
		verbose_name = 'Залог'
		verbose_name_plural = 'Залоги'
	