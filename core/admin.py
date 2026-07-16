from django.contrib import admin
from .models import Student, Course, Faculty, Attendance, AuditLog


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Attendance)


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("user", "module", "action", "created_at")
    list_filter = ("module", "action")
    search_fields = ("module", "action", "description")