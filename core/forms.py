from django import forms
from django.contrib.auth.models import User
from .models import Student, Course, Faculty, Attendance


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter full name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number"
            }),

            "gender": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Male / Female"
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter department"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Enter address"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter age"
            }),

        }

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = "__all__"

        widgets = {

            "course_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course name"
            }),

            "duration": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: 6 Months"
            }),

            "fees": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course fees"
            }),

        }

class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = "__all__"

        widgets = {

            "faculty_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter faculty name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number"
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter subject"
            }),

            "assigned_courses": forms.SelectMultiple(attrs={
                "class": "form-select"
            }),
        }

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = "__all__"

        widgets = {

            "student": forms.Select(attrs={
                "class": "form-select"
            }),

            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

        }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter First Name"
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Last Name"
                }
            ),

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Username"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Email Address"
                }
            ),

        }