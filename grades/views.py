from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Course, Bin, Assessment
from .forms import Courseform

def home(request):
    return render(request, "grades/home.html")


def faq(request):
    return render(request, "grades/faq.html", {"title": "FAQ"})


def about(request):
    return render(request, "grades/about.html", {"title": "About"})

def courses(request, user_id):
    courses_list = Course.objects.filter(user__pk=user_id)
    template = loader.get_template("grades/courses.html")
    context = {
        'courses_list': courses_list,
    }
    return HttpResponse(template.render(context, request))

def course(request, user_id, course_id):
    bins_list = Bin.objects.filter(course__pk=course_id)
    template = loader.get_template("grades/course.html")
    context = {
        'bins_list': bins_list,
    }
    return HttpResponse(template.render(context, request))

def assessment(request, user_id, course_id, bin_id):
    assessments_list = Assessment.objects.filter(bin__pk=bin_id)
    template = loader.get_template("grades/assessment.html")
    context = {
        'assessments_list': assessments_list,
    }
    return HttpResponse(template.render(context, request))

def newCourse(request, user_id):
    if request.method == 'POST':
        form = Courseform(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/courses/")
    else:
        form = Courseform()

    return render(request, "grades/newcourse.html", {'form': form})