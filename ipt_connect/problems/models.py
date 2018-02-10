from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Problem(models.Model):
	"""
	Problem suggestion for the IPT. A model has:
	 	- A name
	 	- An author
	 	- A description
	 	- Labels (from a predefined list ?)
	 	- Flags 
	 	- A grade
	 	- Comments
	 	- Versioning
	"""

	name = models.CharField(max_length=100, default=None)
	author = models.CharField(max_length=100, default=None)
	description = models.TextField(max_length=1500, default=None)

	points = models.FloatField(default=0.0, editable=False)

	def __unicode__(self):
		return self.name

