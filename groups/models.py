from django.db import models
from django.urls import reverse

class Group(models.Model):
	parent_group = models.ForeignKey('self', null=True, blank=True, related_name='Parent', verbose_name="Родительская группа", on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	description = models.TextField(max_length=512, blank=True, null=True)
	icon = models.ImageField(upload_to="groups/%Y/%m/%d/", blank=True, verbose_name="Иконка")
	child_groups = models.PositiveIntegerField(verbose_name="Дочерние группы", default=0)
	child_elems = models.PositiveIntegerField(verbose_name="Дочерние элементы", default=0)

	class Meta:
		ordering = ['name']
		verbose_name = 'Группа'
		verbose_name_plural = 'Группы'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('groups:GroupDetail', args=[self.pk])

	def get_add_url(self):
		return reverse('groups:ElemCreate', args=[self.pk])

class Elem(models.Model):
	elem_parent_group = models.ForeignKey(Group, related_name='Elem_parent_group', verbose_name="Родительская группа элемента", on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	description = models.TextField(max_length=512, blank=True, null=True)
	icon = models.ImageField(upload_to="elems/%Y/%m/%d/", blank=True, verbose_name="Элемент")
	date = models.DateField(auto_now_add=True)
	checked = models.NullBooleanField(null=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'Элемент'
		verbose_name_plural = 'Элементы'

	def __str__(self):
		return self.name