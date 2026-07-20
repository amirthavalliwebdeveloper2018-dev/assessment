from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api_views import (
    StudentViewSet,
    CourseViewSet,
    FacultyViewSet,
    AttendanceViewSet,
    AuditLogViewSet,
)

router = DefaultRouter()

router.register("students", StudentViewSet, basename="students")
router.register("courses", CourseViewSet, basename="courses")
router.register("faculty", FacultyViewSet, basename="faculty")
router.register("attendance", AttendanceViewSet, basename="attendance")
router.register("auditlogs", AuditLogViewSet, basename="auditlogs")

urlpatterns = [
    path("", include(router.urls)),
]