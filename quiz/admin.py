from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(QuizCategory)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display= ['question', 'level']
admin.site.register(QuizQuestion, QuizQuestionAdmin)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display= ['id', 'question', 'user', 'right_answer']
admin.site.register(UserSubmittedAnswer, UserSubmittedAnswerAdmin)    


class UserCategoryAttemptsAdmin(admin.ModelAdmin):
    list_display= ['category', 'user', 'attempt_time']
admin.site.register(UserCategoryAttempts, UserCategoryAttemptsAdmin)    