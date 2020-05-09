from .serializers import SubjectSerializer
from rest_framework import viewsets, permissions
from django.shortcuts import render, get_object_or_404 
from . import models
from django.db.models import Q
from random import randint
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

alphabets_list = list(map(chr, range(97, 123)))

def generate_session_id():
    suffix_list = []
    for i in range(7):
        x = randint(1,7)
        suffix_list.append(alphabets_list[x])
    suffix = ''.join(suffix_list)
    return suffix



def validate_quiz(request, id):
    QA = models.QA.objects.get(id=id)
    answer = QA.correct_answer
    if request.method == "POST":
        subject = request.POST["subject"]
        if request.session.get("user_session_id"):
            score = models.Score.objects.get(Q(subject=subject) & Q(session_id = request.session.get("user_session_id")))
            if answer == request.POST["answer"]:
                score.point += 1
                score.save()
                request.session["has_taken_test"] = True
            elif answer != request.POST["answer"]:
                score.point += 0
                score.save()
                request.session["has_taken_test"] = True
        elif not request.session.get("user_session_id"):
            request.session["user_session_id"] = generate_session_id()
            session_id = request.session["user_session_id"]
            if answer == request.POST["answer"]:
                score = models.Score.objects.create(session_id = session_id, subject = subject, point = 1)
                score.save()
                request.session["has_taken_test"] = True
            elif answer != request.POST["answer"]:
                score = models.Score.objects.create(session_id = session_id, subject=subject, point = 0)
                score.save()
                request.session["has_taken_test"] = True
    return render(request, 'quiz.html', {"QA":QA})


def test_page(request):
    Subjects = models.Subject.objects.all()
    return render(request, "test.html", {"Subjects":Subjects})



def load_subject(request, slug):
    subject = slug
    if request.session.get(f"{subject}_done") == True:
        expires_at = request.session.get_expiry_age()
        return render(request, "taken.html", {"expires_at":expires_at})
    subject = models.Subject.objects.get(slug=slug)
    qas = subject.qas.all()
    return render(request, "subject.html", {"Subject":subject,"qas":qas})


def result_page(request, slug):
    if not request.session.get("user_session_id"):
        return HttpResponseRedirect("/test/")
    session_id = request.session["user_session_id"]
    subject = slug
    subject_name= subject.lower()
    request.session[f"{subject_name}_done"] = True
    request.session.set_expiry(120)
    score = models.Score.objects.get(Q(session_id = session_id)&Q(subject=subject))
    total_no_qas = len(models.Subject.objects.get(course_name=subject).qas.all())
    del request.session["user_session_id"]
    return render(request, 'result.html',{ "score":score, "total_no_qas":total_no_qas})


class PhysicsViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.filter(course_name="Physics")
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ChemistryViewSet(viewsets.ModelViewSet):
    queryset= models.Subject.objects.filter(course_name="Chemistry")
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
       


class MathematicsViewSet(viewsets.ModelViewSet):
        queryset = models.Subject.objects.filter(course_name="Mathematics")
        serializer_class = SubjectSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

       
