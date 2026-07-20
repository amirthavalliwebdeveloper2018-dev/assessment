from rest_framework import viewsets

from .models import Student, Course, Faculty, Attendance, AuditLog
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    FacultySerializer,
    AttendanceSerializer,
    AuditLogSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("-id")
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("-id")
    serializer_class = CourseSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all().order_by("-id")
    serializer_class = FacultySerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by("-id")
    serializer_class = AttendanceSerializer


class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all().order_by("-created_at")
    serializer_class = AuditLogSerializer