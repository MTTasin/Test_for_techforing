from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(User)
class UserAccountAdmin(admin.ModelAdmin):
    model = User
    list_display = ["id", "username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined"]
    list_display_links = ["id", "username", "email"]
    list_filter = ["id", "username", "email", "first_name", "last_name", "is_staff", "is_active"]
    search_fields = ["id", "username", "email", "first_name", "last_name"]
    fieldsets = (
        (
            _("Login Credentials"), {
                "fields": ("email", "password",)
            }, 
        ),
        (
            _("Personal Information"),
            {
                "fields": ('username', 'first_name', 'last_name',)
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login",)
            },
        ),
    )
    add_fieldsets = (
            (None, {
                "classes": ("wide",),
                "fields": ("username", "email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active", "date_joined"),
            },),
        )
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["id", "name", "description", "owner", "created_at"]
    list_display_links = ["id", "name"]
    list_filter = ["id", "name", "description", "owner", "created_at"]
    search_fields = ["id", "name", "description", "owner", "created_at"]



@admin.register(Project_member)
class ProjectMemberAdmin(admin.ModelAdmin):
    model = Project_member
    list_display = ["id", "project", "user", "role"]
    list_display_links = ["id", "project", "user"]
    list_filter = ["id", "project", "user", "role"]
    search_fields = ["id", "project", "user", "role"]



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ["id", "title", "description", "status", "priority", "assigned_to", "project", "created_at", "due_date"]
    list_display_links = ["id", "title"]
    list_filter = ["id", "title", "description", "status", "priority", "assigned_to", "project", "created_at", "due_date"]
    search_fields = ["id", "title", "description", "status", "priority", "assigned_to", "project", "created_at", "due_date"]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ["id", "content", "user", "task", "created_at"]
    list_display_links = ["id", "content"]
    list_filter = ["id", "content", "user", "task", "created_at"]
    search_fields = ["id", "content", "user", "task", "created_at"]
