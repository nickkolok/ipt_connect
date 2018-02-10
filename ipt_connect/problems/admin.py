from django.contrib import admin
from django.contrib.auth.models import User
from models import *

# Register your models here.


class ProblemAdmin(admin.ModelAdmin):

	list_display = ('name', 'author', 'points')
	search_fields = ('name', 'author', 'points')



admin.site.register(Problem, ProblemAdmin)