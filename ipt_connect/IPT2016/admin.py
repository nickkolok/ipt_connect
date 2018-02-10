# coding: utf8
from django.contrib import admin
from django.contrib.auth.models import User
from models import *
from django import forms
from django.forms import widgets

class JuryGradeInline(admin.TabularInline):
	model = JuryGrade
	extra = 0

class TacticalRejectionInline(admin.TabularInline):
	model = TacticalRejection
	extra = 0

class EternalRejectionInline(admin.TabularInline):
	model = EternalRejection
	extra = 0

class Roundadmin(admin.ModelAdmin):

	list_display = ('pf_number','round_number','room')
	list_filter = ('pf_number','round_number','room')
	fieldsets = [
	('General Information', {'fields': [('pf_number', "round_number", "room"), ("reporter_team", "opponent_team", "reviewer_team")]}),
	(None, {'fields': [("reporter"), ('opponent'), ('reviewer'), 'problem_presented']})
	]
	inlines = [TacticalRejectionInline, EternalRejectionInline, JuryGradeInline]
	
	class Media:
		js = ('admin/js/jquery.js','admin/js/participant_fill.js',)
	#TODO: Display the full name+surname of the reporter, opponent and reviewer in the admin view


class TeamAdmin(admin.ModelAdmin):

	list_display = ('name','IOC')
	search_fields = ('name','IOC')


class ParticipantAdmin(admin.ModelAdmin):

	list_display = ('surname','name','team','email','role','gender','birthdate','passport_number','affiliation','veteran','diet','tourism','shirt_size','remark','hotel_room','mixed_dormitory','check_in')
	search_fields = ('surname','name','hotel_room')
	list_filter = ('team','gender','role','diet','tourism','veteran','shirt_size','hotel_room','check_in')

	def save_model(self, request, obj, form, change):
		if not(request.user.is_superuser):
			u = User.objects.get(username = request.user.username)
			obj.team = u.Team_IPT2016
			obj.save()
		obj.save()

	def get_queryset(self,request):
		qs = super(ParticipantAdmin,self).get_queryset(request)
		u = User.objects.get(username = request.user.username)
		if request.user.is_superuser:
			return qs
		return qs.filter(team = u.Team_IPT2016)

class JuryAdmin(admin.ModelAdmin):

	list_display = ('name',)


# Register your models here.
admin.site.register(Team,TeamAdmin)
admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Round, Roundadmin)
admin.site.register(Problem)
admin.site.register(Room)
admin.site.register(Jury,JuryAdmin)
