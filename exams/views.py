from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import ExamForm, QuestionForm
from .models import Exam, Question
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from django.utils import timezone


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'exams/create_exam.html', {'form': form})

def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'exams/create_question.html', {'form': form})
def take_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = Question.objects.filter(exam=exam)
    
    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_option:
                score += 1
        return render(request, 'exams/result.html', {'score': score, 'total': total})

    return render(request, 'exams/take_exam.html', {'exam': exam, 'questions': questions})
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exams/exam_list.html', {'exams': exams})

def logout_view(request):
    auth_logout(request)
    return render(request, 'registration/logged_out.html')


# Create your views here.
