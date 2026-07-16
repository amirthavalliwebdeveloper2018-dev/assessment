import csv
from io import TextIOWrapper

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Student, Course, Faculty, Attendance, AuditLog
from .forms import StudentForm, CourseForm, FacultyForm, AttendanceForm, ProfileForm

from openpyxl import Workbook
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch



def home(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    return redirect("login")


def login_page(request):

    # Already logged in users should not see the login page
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password")

    return render(request, "login.html")


@login_required(login_url="login")
def dashboard(request):

    context = {
         "student_count": Student.objects.count(),
    "course_count": Course.objects.count(),
    "faculty_count": Faculty.objects.count(),
    "attendance_count": Attendance.objects.count(),
    "recent_logs": AuditLog.objects.select_related("user").order_by("-created_at")[:3],

    }

    return render(request, "dashboard.html", context)

@login_required(login_url="login")
def student_list(request):

    search = request.GET.get("search")

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all().order_by("-id")

    context = {
        "students": students
    }

    return render(request, "student_list.html", context)

@login_required(login_url="login")
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
               user=request.user,
    module="Student",
    action="CREATE",
    description=f"Created student '{form.instance.name}'"
            )

            messages.success(request, "Student added successfully.")

            return redirect("student_list")

        else:

            messages.error(request, form.errors.as_text())

    else:

        form = StudentForm()

    context = {
        "form": form
    }

    return render(request, "add_student.html", context)

@login_required(login_url="login")
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
              user=request.user,
    module="Student",
    action="UPDATE",
    description=f"Updated student '{student.name}'"
            )

            messages.success(request, "Student updated successfully.")

            return redirect("student_list")
        
        else:

            messages.error(request, form.errors.as_text())

    else:

        form = StudentForm(instance=student)

    context = {
        "form": form
    }

    return render(request, "add_student.html", context)

@login_required(login_url="login")
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student_name = student.name

    student.delete()

    AuditLog.objects.create(
    user=request.user,
    module="Student",
    action="DELETE",
    description=f"Deleted student '{student_name}'"
    )

    messages.success(request, "Student deleted successfully.")

    return redirect("student_list")

@login_required(login_url="login")
def course_list(request):

    courses = Course.objects.all().order_by("-id")

    context = {
        "courses": courses
    }

    return render(request, "course_list.html", context)

@login_required(login_url="login")
def add_course(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
                user=request.user,
    module="Course",
    action="CREATE",
    description=f"Created course '{form.instance.course_name}'"
            )

            messages.success(request, "Course added successfully.")

            return redirect("course_list")

        else:

            messages.error(request, form.errors.as_text())

    else:

        form = CourseForm()

    context = {
        "form": form
    }

    return render(request, "add_course.html", context)

@login_required(login_url="login")
def edit_course(request, id):

    course = get_object_or_404(Course, id=id)

    if request.method == "POST":

        form = CourseForm(request.POST, instance=course)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
                user=request.user,
    module="Course",
    action="UPDATE",
    description=f"Updated course '{course.course_name}'"
            )

            messages.success(request, "Course updated successfully.")

            return redirect("course_list")
        
        else:

            messages.error(request, form.errors.as_text())

    else:

        form = CourseForm(instance=course)

    context = {
        "form": form
    }

    return render(request, "add_course.html", context)

@login_required(login_url="login")
def delete_course(request, id):

    course = get_object_or_404(Course, id=id)

    course_name = course.course_name

    course.delete()

    AuditLog.objects.create(
    user=request.user,
    module="Course",
    action="DELETE",
    description=f"Deleted course '{course_name}'"

    )

    messages.success(request, "Course deleted successfully.")

    return redirect("course_list")


@login_required(login_url="login")
def faculty_list(request):

    faculties = Faculty.objects.all().order_by("-id")

    context = {
        "faculties": faculties
    }

    return render(request, "faculty_list.html", context)


@login_required(login_url="login")
def add_faculty(request):

    if request.method == "POST":

        form = FacultyForm(request.POST)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
               user=request.user,
    module="Faculty",
    action="CREATE",
    description=f"Created faculty '{form.instance.faculty_name}'"
            )

            messages.success(request, "Faculty added successfully.")

            return redirect("faculty_list")

        else:
            messages.error(request, form.errors.as_text())

    else:

        form = FacultyForm()

    context = {
        "form": form
    }

    return render(request, "add_faculty.html", context)


@login_required(login_url="login")
def edit_faculty(request, id):

    faculty = get_object_or_404(Faculty, id=id)

    if request.method == "POST":

        form = FacultyForm(request.POST, instance=faculty)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
              user=request.user,
    module="Faculty",
    action="UPDATE",
    description=f"Updated faculty '{faculty.faculty_name}'"
            )

            messages.success(request, "Faculty updated successfully.")

            return redirect("faculty_list")
        
        else:

            messages.error(request, form.errors.as_text())

    else:

        form = FacultyForm(instance=faculty)

    context = {
        "form": form
    }

    return render(request, "add_faculty.html", context)

@login_required(login_url="login")
def delete_faculty(request, id):

    faculty = get_object_or_404(Faculty, id=id)

    faculty_name = faculty.faculty_name

    faculty.delete()

    AuditLog.objects.create(
    user=request.user,
    module="Faculty",
    action="DELETE",
    description=f"Deleted faculty '{faculty_name}'"
    )

    messages.success(request, "Faculty deleted successfully.")

    return redirect("faculty_list")

@login_required(login_url="login")
def export_students_excel(request):

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Students"

    sheet.append([
        "ID",
        "Name",
        "Email",
        "Phone",
        "Gender",
        "Department",
        "Age",
        "Address"
    ])

    students = Student.objects.all().order_by("-id")

    for student in students:
        sheet.append([
            student.id,
            student.name,
            student.email,
            student.phone,
            student.gender,
            student.department,
            student.age,
            student.address,
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="students.xlsx"'

    workbook.save(response)

    return response

@login_required(login_url="login")
def export_students_pdf(request):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="students.pdf"'

    document = SimpleDocTemplate(response, pagesize=(11 * inch, 8.5 * inch))

    data = [[
        "ID",
        "Name",
        "Email",
        "Phone",
        "Gender",
        "Department",
        "Age",
        "Address"
    ]]

    students = Student.objects.all().order_by("-id")

    for student in students:
        data.append([
            student.id,
            student.name,
            student.email,
            student.phone,
            student.gender,
            student.department,
            student.age,
            student.address,
        ])

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]))

    document.build([table])

    return response

@login_required(login_url="login")
def import_students_csv(request):

    if request.method == "POST":

        csv_file = request.FILES.get("csv_file")

        if not csv_file:
            messages.error(request, "Please select a CSV file.")
            return redirect("student_list")

        file = TextIOWrapper(csv_file.file, encoding="utf-8")
        reader = csv.DictReader(file)

        imported = 0
        skipped = 0

        for row in reader:

            if Student.objects.filter(email=row["email"]).exists():
                skipped += 1
                continue

            Student.objects.create(
                name=row["name"],
                email=row["email"],
                phone=row["phone"],
                gender=row["gender"],
                department=row["department"],
                address=row["address"],
                age=int(row["age"]),
            )

            imported += 1

        AuditLog.objects.create(
    user=request.user,
    module="Student",
    action="IMPORT",
    description=f"Imported {imported} students ({skipped} duplicates skipped)"
        )

        messages.success(
            request,
            f"{imported} students imported successfully. {skipped} duplicate records skipped."
        )

    return redirect("student_list")

@login_required(login_url="login")
def attendance_list(request):

    attendances = Attendance.objects.all().order_by("-date")

    context = {
        "attendances": attendances
    }

    return render(request, "attendance_list.html", context)

@login_required(login_url="login")
def add_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
                user=request.user,
    module="Attendance",
    action="CREATE",
    description=f"Marked attendance for '{form.instance.student.name}'"
            )

            messages.success(request, "Attendance added successfully.")

            return redirect("attendance_list")

        else:

            messages.error(request, form.errors.as_text())

    else:

        form = AttendanceForm()

    context = {
        "form": form
    }

    return render(request, "add_attendance.html", context)

@login_required(login_url="login")
def edit_attendance(request, id):

    attendance = get_object_or_404(Attendance, id=id)

    if request.method == "POST":

        form = AttendanceForm(request.POST, instance=attendance)

        if form.is_valid():

            form.save()

            AuditLog.objects.create(
                user=request.user,
    module="Attendance",
    action="UPDATE",
    description=f"Updated attendance for '{attendance.student.name}'"
            )

            messages.success(request, "Attendance updated successfully.")

            return redirect("attendance_list")

        else:

            messages.error(request, form.errors.as_text())

    else:

        form = AttendanceForm(instance=attendance)

    context = {
        "form": form
    }

    return render(request, "add_attendance.html", context)

@login_required(login_url="login")
def delete_attendance(request, id):

    attendance = get_object_or_404(Attendance, id=id)

    student_name = attendance.student.name

    attendance.delete()

    AuditLog.objects.create(
    user=request.user,
    module="Attendance",
    action="DELETE",
    description=f"Deleted attendance of '{student_name}'"
    )

    messages.success(request, "Attendance deleted successfully.")

    return redirect("attendance_list")

@login_required(login_url="login")
def audit_log_list(request):

    logs = AuditLog.objects.all().order_by('-created_at')

    action = request.GET.get('action')

    if action:
        logs = logs.filter(action=action)

    search = request.GET.get("search")

    if search:
        logs = logs.filter(
            description__icontains=search
        )

    paginator = Paginator(logs, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "audit_log_list.html",
        {
            "page_obj": page_obj
        }
    )


# ================= REPORTS =================

@login_required(login_url="login")
def reports(request):

    recent_logs = AuditLog.objects.order_by("-created_at")[:5]

    context = {

        "student_count": Student.objects.count(),

        "course_count": Course.objects.count(),

        "faculty_count": Faculty.objects.count(),

        "attendance_count": Attendance.objects.count(),

        "present_count": Attendance.objects.filter(
            status="Present"
        ).count(),

        "absent_count": Attendance.objects.filter(
            status="Absent"
        ).count(),

        "audit_count": AuditLog.objects.count(),

        "recent_logs": recent_logs,

    }

    return render(
        request,
        "reports.html",
        context
    )

# ================= PROFILE =================

@login_required(login_url="login")
def profile(request):

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile")

    else:

        form = ProfileForm(
            instance=request.user
        )

    return render(
        request,
        "profile.html",
        {
            "form": form
        }
    )

# ================= LOGOUT =================

def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")

   