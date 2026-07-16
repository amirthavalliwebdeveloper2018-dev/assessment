from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # Home & Login

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "login/",
        views.login_page,
        name="login"
    ),


    # Dashboard

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),



    # ================= STUDENT =================

    path(
        "students/",
        views.student_list,
        name="student_list"
    ),

    path(
        "students/add/",
        views.add_student,
        name="add_student"
    ),

    path(
        "students/edit/<int:id>/",
        views.edit_student,
        name="edit_student"
    ),

    path(
        "students/delete/<int:id>/",
        views.delete_student,
        name="delete_student"
    ),

    path(
        "students/export/excel/",
        views.export_students_excel,
        name="export_students_excel"
    ),

    path(
        "students/export/pdf/",
        views.export_students_pdf,
        name="export_students_pdf"
    ),

    path(
        "students/import/csv/",
        views.import_students_csv,
        name="import_students_csv"
    ),



    # ================= COURSE =================

    path(
        "courses/",
        views.course_list,
        name="course_list"
    ),

    path(
        "courses/add/",
        views.add_course,
        name="add_course"
    ),

    path(
        "courses/edit/<int:id>/",
        views.edit_course,
        name="edit_course"
    ),

    path(
        "courses/delete/<int:id>/",
        views.delete_course,
        name="delete_course"
    ),



    # ================= FACULTY =================

    path(
        "faculty/",
        views.faculty_list,
        name="faculty_list"
    ),

    path(
        "faculty/add/",
        views.add_faculty,
        name="add_faculty"
    ),

    path(
        "faculty/edit/<int:id>/",
        views.edit_faculty,
        name="edit_faculty"
    ),

    path(
        "faculty/delete/<int:id>/",
        views.delete_faculty,
        name="delete_faculty"
    ),



    # ================= ATTENDANCE =================

    path(
        "attendance/",
        views.attendance_list,
        name="attendance_list"
    ),

    path(
        "attendance/add/",
        views.add_attendance,
        name="add_attendance"
    ),

    path(
        "attendance/edit/<int:id>/",
        views.edit_attendance,
        name="edit_attendance"
    ),

    path(
        "attendance/delete/<int:id>/",
        views.delete_attendance,
        name="delete_attendance"
    ),


    # ================= AUDIT LOG =================

    path(
        "audit-logs/",
        views.audit_log_list,
        name="audit_log_list"
    ),


    # ================= REPORTS =================

    path(
        "reports/",
        views.reports,
        name="reports"
    ),


    # ================= PROFILE =================

    path(
        "profile/",
        views.profile,
        name="profile"
    ),


    # ================= LOGOUT =================

    path(
        "logout/",
        views.logout_page,
        name="logout"
    ),



    # ================= FORGOT PASSWORD =================


    path(
        "forgot-password/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset.html"
        ),
        name="password_reset"
    ),


    path(
        "forgot-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done"
    ),


    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
        ),
        name="password_reset_confirm"
    ),


    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),
    
path(
    "change-password/",
    auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change.html"
    ),
    name="password_change",
),

path(
    "change-password/done/",
    auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/password_change_done.html"
    ),
    name="password_change_done",
),
]