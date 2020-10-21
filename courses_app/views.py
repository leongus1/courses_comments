from django.shortcuts import render, HttpResponse, redirect
from .models import Courses, Descriptions, Comments
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'header': "Add a New Course",
        'courses': Courses.objects.all(),
        'button': "  Add  ",
        'to_edit': False,
    }
    return render(request, 'index.html', context)

def add_course(request):
    errors = Courses.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        Courses.objects.create(name=request.POST['course_name'],description=Descriptions.objects.create(description=request.POST['description']))
        
        return redirect ('/')
    
    
def remove_course_page(request, course_id):
    context = {
        'course': Courses.objects.get(description_id=course_id),    
    }
    
    return render(request, 'remove_confirm.html', context)

def confirm_remove(request, course_id):
    Courses.objects.get(description_id=course_id).delete()
    return redirect('/')

def edit(request, course_id):
    context = {
        'header': "Edit Course Information",
        'courses': Courses.objects.all(),
        'button': " Update ",
        'to_edit': True,
        'this_course': Courses.objects.get(description_id=course_id),
        'this_id': course_id,
    }
    return render(request, 'index.html', context)

def update(request, course_id):
    c1 = Courses.objects.get(description_id=course_id)
    d1 = Descriptions.objects.get(id=course_id)
    c1.name = request.POST['course_name']
    d1.description=request.POST['description']
    c1.save()
    d1.save()
    return redirect('/')

def course_comments(request, course_id):
    context = {
        'this_course': Courses.objects.get(description_id=course_id),
    }
    return render(request, 'comments.html', context)
    
def update_comment(request, course_id):
    this_course = Courses.objects.get(description_id=course_id)
    Comments.objects.create(topic = request.POST['topic'], comment = request.POST['comment'], course = this_course)
    return redirect(f'/courses/{course_id}/comments')
    
    
    
    