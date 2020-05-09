from django.db import models
import uuid
from django.urls import reverse

class Subject(models.Model):
    course_name = models.CharField(max_length = 60)
    fa_icon = models.CharField(max_length=20, blank = True)
    duration_in_minutes = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    
    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs = {'slug':self.slug})

class QA(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    subject = models.ForeignKey(Subject, related_name = "qas", on_delete = models.CASCADE)
    question = models.CharField(max_length=300)
    answer_1 = models.CharField(max_length=60)
    answer_2 = models.CharField(max_length=60)
    answer_3 = models.CharField(max_length=60)
    correct_answer = models.CharField(max_length=60)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('qa_detail', kwargs={'id': self.id},)

class Score(models.Model):
    session_id = models.CharField(max_length=60)
    subject = models.CharField(max_length = 20);
    point = models.IntegerField(blank=True)
    def __str__(self):
        return f'{self.session_id} => {self.point} point(s)'

    def get_absolute_url(self):
        return reverse('result', kwargs={"slug":self.subject})




