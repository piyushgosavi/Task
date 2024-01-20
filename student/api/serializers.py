from rest_framework import serializers
from .models import Section, Student


class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id','name']


class StudentSerializers(serializers.ModelSerializer):
    section = SectionSerializers(read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','section']