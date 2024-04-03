from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from app.forms import CourseModelForm, StudentModelForm, RegisterForm, LoginForm
from app.models import Student, Course, Region




def index_view(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    paginator = Paginator(object_list=students,
                          per_page=8)

    students_right = Student.objects.all()[:7]
    page_number = request.GET.get('page')
    students_list = paginator.get_page(number=page_number)
    query = request.GET.get('query', '')

    if query:
        students_list = Student.objects.filter(
            Q(course__title__icontains=query) |
            Q(fathers_job__icontains=query) |
            Q(mothers_job__icontains=query) |
            Q(address_line__icontains=query) |
            Q(region__name__icontains=query) |
            Q(study__icontains=query) |
            Q(name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(mothers_phone__icontains=query) |
            Q(mothers_name__icontains=query) |
            Q(fathers_name__icontains=query) |
            Q(course__title__icontains=query) |
            Q(age=query) |
            Q(level=query) |
            Q(fathers_phone__icontains=query) |  # Otaning telefon raqami (fathers_phone) ni qidirish
            Q(fathers_age__icontains=query) |
            Q(mothers_age__icontains=query)
        )
    return render(request=request,
                  template_name='app/index.html',
                  context={"students": students_list,
                           "students_right": students_right,
                           "courses": courses})


def add_view(request):
    if request.method == "POST":
        form = CourseModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = CourseModelForm()
    return render(request=request,
                  template_name='app/add.html',
                  context={"form": form})


def edit_student_view(request, student_id):
    student = Student.objects.select_related('course', 'region').filter(id=student_id).first()

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            if request.user.is_authenticated:
                student.user = request.user
            student.save(update_fields=['name', 'age', 'study', 'level', 'phone_number', 'address_line', 'region',
                                        'fathers_name', 'fathers_age', 'fathers_job', 'fathers_phone', 'mothers_name',
                                        'mothers_age', 'mothers_job', 'mothers_phone'])
            return redirect('student', student.id)

    form = StudentModelForm(instance=student)

    return render(request=request, template_name='app/edit.html',
                  context={"form": form, "courses": Course.objects.all(), "regions": Region.objects.all()})


def add_student_view(request):
    courses = Course.objects.all()
    regions = Region.objects.all()
    if request.method == "POST":
        form = StudentModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    form = StudentModelForm()
    return render(request=request,
                  template_name='app/add_student.html',
                  context={"form": form,
                           "courses": courses,
                           "regions": regions})


def detail_view(request, student_id):
    student = Student.objects.filter(id=student_id).first()

    return render(request=request,
                  template_name='app/detail.html',
                  context={"student": student})


def delete_view(request, student_id):
    student = Student.objects.filter(id=student_id).first()
    action = student.delete()
    if action:
        return redirect('index')
