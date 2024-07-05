from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import ExamForm, QuestionForm
from .models import Exam, Question, ExamResult
from django.contrib.auth import logout as auth_logout
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.utils import timezone


# signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # Automatically log the user in after successful signup
                login(request, user)
                return redirect('login')  # Redirect to exam list or any other page after login
            except ValidationError as e:
                form.add_error(None, e)
                print(f"Validation Error: {e}")
        else:
            print(f"Form Errors: {form.errors}")  # Print form errors for debugging
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
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.question_set.all()

    if request.method == 'POST':
        user = request.user
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_option = request.POST.get(f'{question.id}')
            if selected_option == question.correct_option:
                score += 1

        percentage_score = (score / total_questions) * 100

        # Save the result
        ExamResult.objects.create(user=user, exam=exam, score=percentage_score)

        return redirect('exam_list')  # Redirect to exam list after submission

    return render(request, 'exams/take_exam.html', {'exam': exam, 'questions': questions})
@login_required
def exam_list(request):
    user = request.user
    # Get all exams
    all_exams = Exam.objects.all()
    # Get exams the user has taken
    taken_exams = ExamResult.objects.filter(user=user).values_list('exam_id', flat=True)
    # Filter exams that the user hasn't taken yet
    available_exams = all_exams.exclude(id__in=taken_exams)
    return render(request, 'exams/exam_list.html', {'exams': available_exams})

def logout_view(request):
    auth_logout(request)
    return render(request, 'registration/logged_out.html')


# Create your views here.
