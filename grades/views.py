from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Course, Bin, Assessment
from .forms import Courseform, Binform



def home(request):
    return render(request, "grades/home.html")


def faq(request):
    return render(request, "grades/faq.html", {"title": "FAQ"})


def about(request):
    return render(request, "grades/about.html", {"title": "About"})


@login_required
def courses(request):
    courses_list = Course.objects.filter(user__user=request.user)
    template = loader.get_template("grades/courses.html")
    context = {
        'courses_list': courses_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def course(request, course_id):
    bins_list = Bin.objects.filter(course__pk=course_id)
    template = loader.get_template("grades/course.html")
    context = {
        'bins_list': bins_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def assessment(request, course_id, bin_id):
    assessments_list = Assessment.objects.filter(bin__pk=bin_id)
    template = loader.get_template("grades/assessment.html")
    context = {
        'assessments_list': assessments_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def newCourse(request):
    if request.method == 'POST':
        form = Courseform(request.POST)

        if form.is_valid():
            new_course = Course.objects.create(name=form.instance.name,
                                               credits=form.instance.credits,
                                               user=request.user.profile)
            new_course.save()
        #    new_Course = form.save(commit=False)
        #    new_Course.user = request.user
        #    new_Course.save()
        #    form.save()
            return HttpResponseRedirect("/courses/")
    else:
        form = Courseform()

    return render(request, "grades/newcourse.html", {'form': form})

@login_required
def newBin(request, course_id):
    if request.method == 'POST':
        form = Binform(request.POST)
        if form.is_valid():
            new_bin = form.save(commit=False)
            new_bin.course = course_id
            new_bin.save()
            return HttpResponseRedirect("/courses/" + course_id)
    else:
        form = Binform()

    return render(request, "grades/newbin.html", {'form': form})
