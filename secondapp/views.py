from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Student
from .forms import TeacherForm, StudentForm


# CREATE operations
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # redirect to a list of teachers after creation
    else:
        form = TeacherForm()
    return render(request, 'create_teacher_two.html', {'form': form})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # redirect to a list of students after creation
    else:
        form = StudentForm()
    return render(request, 'create_student_two.html', {'form': form})


# READ operations
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list_two.html', {'teachers': teachers})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list_two.html', {'students': students})


# UPDATE operations
def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'update_teacher_two.html', {'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student_two.html', {'form': form})


# DELETE operations
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'delete_teacher_two.html', {'teacher': teacher})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student_two.html', {'student': student})
