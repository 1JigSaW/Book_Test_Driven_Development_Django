from django.db import models

class Item(models.Model):
	'''list item'''
	text = models.TextField(default='')
