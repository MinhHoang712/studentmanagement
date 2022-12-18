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