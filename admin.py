from django.contrib import admin
from polls.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
	    ('Question',               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	
admin.site.register(Question, QuestionAdmin)
