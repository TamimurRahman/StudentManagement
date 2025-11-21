from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from .models import Student_Info
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

def create_student(request):
    try:
        # ====== Check if form is submitted ======
        if request.method == 'POST':
            # ====== Get form data ======
            name = request.POST.get('name')
            roll = request.POST.get('roll')
            student_class = request.POST.get('student_class')
            dob = request.POST.get('dob')
            status = request.POST.get('status')
            father_name = request.POST.get('father_name')
            mother_name = request.POST.get('mother_name')
            phone = request.POST.get('phone')
            adress = request.POST.get('adress')
            
            # ====== Get uploaded photo ======
            photo = request.FILES.get('photo')

            # ====== Create new student record ======
            Student_Info.objects.create(
                name=name,
                roll=roll,
                student_class=student_class,
                dob=dob,
                status=status,
                father_name=father_name,
                mother_name=mother_name,
                phone=phone,
                adress=adress,
                photo=photo
            )

            # ====== Success message & redirect ======
            messages.add_message(request, messages.SUCCESS, 'Student created successfully!')
            return redirect('list')

    # ====== Handle duplicate roll number in the same class ======
    except IntegrityError:
        messages.add_message(request, messages.SUCCESS, 'This roll already exists in this class!')
        return redirect('create')

    # ====== Render the create student page ======
    return render(request, 'create_student.html')



def student_list(request):
    all_students = Student_Info.objects.all()
    class_filter = request.GET.get('student_class','all')#for filtering
    query = request.GET.get('name_query','').strip()
    # search_result = None
    if class_filter != 'all':
        all_students = all_students.filter(student_class=class_filter)
    
    if query:
        all_students = all_students.filter(Q(name__icontains=query))
        
    return render(request,'student_list.html',{'all_students':all_students,'class_filter':class_filter,'query':query})

def student_profile_view(request,id):
    student = Student_Info.objects.get(id=id) # id capture korlam
    return render(request,'student_details.html',{'student':student})

def update_student(request, id):
    # ====== Get the student object or return 404 if not found ======
    student = get_object_or_404(Student_Info, id=id)

    # ====== Check if form is submitted ======
    if request.method == 'POST':
        # ====== Update student fields from form ======
        student.name = request.POST.get('name')
        student.roll = request.POST.get('roll')
        student.student_class = request.POST.get('student_class')
        student.dob = request.POST.get('dob')
        student.status = request.POST.get('status')
        student.father_name = request.POST.get('father_name')
        student.mother_name = request.POST.get('mother_name')
        student.phone = request.POST.get('phone')
        student.adress = request.POST.get('adress')

        # ====== Update photo if new image uploaded ======
        if request.FILES.get('photo'):  # Only update if new image uploaded
            student.photo = request.FILES.get('photo')

        # ====== Save the updated student object ======
        student.save()

        # ====== Redirect to student list after update ======
        return redirect('list')

    # ====== Render the create/update student form with existing data ======
    return render(request, 'create_student.html', {'student': student})



def delete_student(request, id):
    student = get_object_or_404(Student_Info, id=id)
    student.delete()
    return redirect('list')


