from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course, Bin

def home(request):
    return render(request, "grades/home.html")


def faq(request):
    return render(request, "grades/faq.html", {"title": "FAQ"})


def about(request):
    return render(request, "grades/about.html", {"title": "About"})

def courses(request):
    courses_list = Course.objects.order_by('-name')
    template = loader.get_template("grades/courses.html")
    context = {
        'courses_list': courses_list,
    }
    return HttpResponse(template.render(context, request))

def course(request, course_id):
    bins_list = Bin.objects.filter(course__pk=course_id)
    template = loader.get_template("grades/course.html")
    context = {
        'bins-list': bins_list,
    }
    return HttpResponse(template.render(context, request))

