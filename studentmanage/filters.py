import django_filters
from .models import*
from django_filters import ModelChoiceFilter

class StaffFilter(django_filters.FilterSet):
    staff_name = ModelChoiceFilter(queryset=Staffs.objects.all())
    class Meta:
        model=Staffs
        fields = ["staff_name"]

class CourseFilter(django_filters.FilterSet):
    course_name = ModelChoiceFilter(queryset=Courses.objects.all())
    class Meta:
        model = Courses  
        fields = ["course_name"]
        
class SubjectFilter(django_filters.FilterSet):
    subject_name = ModelChoiceFilter(queryset = Subjects.objects.all())
    class Meta:
        model = Subjects 
        fields = ["subject_name"]
        
class StudentFilter(django_filters.FilterSet):
    student_name = ModelChoiceFilter(queryset= Students.objects.all())
    class Meta:
        model= Students 
        fields = ["student_name"] 
        