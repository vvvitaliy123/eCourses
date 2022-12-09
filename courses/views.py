from django.shortcuts import render
from .models import Category, Course

def courses(request):

    all_courses = Course.objects.all()

    return render(request, 'courses/courses.html', {
        'page_title': 'Всі курси',
        'all_courses': all_courses,
        'all_categorys': Category.objects.all(),
    })
