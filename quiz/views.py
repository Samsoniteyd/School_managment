from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from . import models


def all_category(request):
    catData= models.QuizCategory.objects.all()
    context={
        'brin':catData
    }
    return render(request, 'quizs/all_category.html', context)


@login_required(login_url=('login'))
def category_question(request, cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question=models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    context={
        'question':question,
        'category': category
    }
    return render(request, 'quizs/category_question.html', context)



def submit_answer(request, cat_id, quest_id):
    if request.method== 'POST':
        category = models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestion.objects.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
            if question:
                quest= models.QuizQuestion.objects.get(id=quest_id)
                user=request.user
                answer='Not Submitted'
                models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
                context={
                    'question': question,
                    'category': category
                }
                return render(request, 'quizs/category_question.html', context ) 
            else:
                quest=models.QuizQuestion.objects.get(id=quest_id)
                user=request.user
                answer=request.POST['answer'] 
                models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)

            # return HttpResponse('skip is clicked!!')
             
        # category = models.QuizCategory.objects.get(id=cat_id)
        # question=models.QuizQuestion.objects.filter(category=category, id__gt=quest_id).exclude(id=quest_id).order_by('id').first()

        if question:
             
            context={
                'question':question,
                'category': category
            }
            return render(request, 'quizs/category_question.html', context)
        else:
            return HttpResponse('No more question!')

    else:
         return HttpResponse('method not allowed!')




# @login_required(login_url=('login'))
# def submit_answer(request, cat_id, quest_id):
#     if request.method =='POST': 
#         category = models.QuizCategory.objects.get(id=cat_id)
#         question=models.QuizQuestion.objects.filter(category=category, id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        
#         if 'skip' in request.POST:
#             if question:
#                 quest= models.QuizQuestion.objects.get(id=quest_id)
#                 user= request.user
#                 answer = 'Not Submitted'
#                 models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
#                 context={
#                     'question':question,
#                     'category': category
#                 }
#                 return render(request, 'quizs/category_question.html', context)
#         else:
#             quest=models.QuizQuestion.objects.get(id=quest_id)
#             user = request.user
#             answer= request.POST['answer']
#             models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
#         if question:
#             context={
#                 'question':question,
#                 'category': category
#             }
#             return render(request, 'quizs/category_question.html', context)
#         else:
#             result = models.UserSubmittedAnswer.objects.filter(user=request.user)
#             skipped = models.UserSubmittedAnswer.objects.filter(user=request.user,  right_answer= "not submitted" ).count()
#             attempted  = models.UserSubmittedAnswer.objects.filter(user=request.user).exclude(right_answer= "not submitted").count()
            
#             rightAns=0
#             percentage= 0
#             for row in result:
#                 if row.question.right_opt  == row.right_answer:
#                     rightAns +=1
#             percentage= (rightAns*100)/result.count()       

#             context={
#                 'result':result,
#                 'total_skipped':skipped,
#                 'attempted':attempted,
#                 'rightAns': rightAns,
#                 'percentage':percentage

#             }
#             return render(request, 'quizs/result.html', context)

#     else:
#         return HttpResponse('method not allowed!')
    

@login_required(login_url=('login'))
def attempt_limit(request):
        return render(request, 'attempt_limit.html' )

@login_required(login_url=('login'))
def final(request):
    result = models.UserSubmittedAnswer.objects.filter(user=request.user)
    skipped = models.UserSubmittedAnswer.objects.filter(user=request.user,  right_answer= "not submitted" ).count()
    attempted  = models.UserSubmittedAnswer.objects.filter(user=request.user).exclude(right_answer= "not submitted").count()
            
    rightAns=0
    percentage= 0
    for row in result:
        if row.question.right_opt  == row.right_answer:
            rightAns +=1
    percentage= (rightAns*100)/result.count() 
    context={
                'result':result,
                'total_skipped':skipped,
                'attempted':attempted,
                'rightAns': rightAns,
                'percentage':percentage

            }
    return render(request, 'quizs/final.html', context)
