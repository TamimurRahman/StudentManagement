from django.shortcuts import render,redirect,get_object_or_404
from .models import Student_Info
# Create your views here.

def create_student(request):
    if request.method=='POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        student_class = request.POST.get('student_class')
        dob = request.POST.get('dob')
        status = request.POST.get('status')
        father_name = request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        phone = request.POST.get('phone')
        adress = request.POST.get('adress')
        photo = request.FILES.get('photo')

        Student_Info.objects.create(
            name=name,roll=roll,student_class=student_class,dob=dob,status=status,father_name=father_name,
            mother_name=mother_name,phone=phone,adress=adress,photo=photo
        )

        return redirect('list')
    return render(request,'create_student.html')

def student_list(request):
    all_students = Student_Info.objects.all()
    return render(request,'student_list.html',{'all_students':all_students})

def student_profile_view(request,id):
    student = Student_Info.objects.get(id=id) # id capture korlam
    return render(request,'student_details.html',{'student':student})

def update_student(request,id):
    student = get_object_or_404(Student_Info,id=id)
    if request.method == 'POST':
        student.name = request.POST('name')
        student.roll = request.POST('roll')
        student.student_class = request.POST('student_class')
        student.dob = request.POST('dob')
        student.status = request.POST('status')
        student.father_name = request.POST('father_name')
        student.mother_name = request.POST('mother_name')
        student.phone = request.POST('phone')
        student.adress = request.POST('adress')
        student.photo = request.FILES.get('photo')

        student.save()
        return redirect('list')
    return render(request,'create_student.html',{'student':student})


