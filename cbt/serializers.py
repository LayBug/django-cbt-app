from .models import Subject, QA
from rest_framework import serializers





class QASerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        fields = [
                'id',
                ]

class SubjectSerializer(serializers.ModelSerializer):
    qas = QASerializer(many=True, read_only = True)
    class Meta:
        model = Subject
        fields = (
                'course_name',
                'qas',
                )


