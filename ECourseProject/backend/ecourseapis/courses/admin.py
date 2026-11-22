from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Course, Lesson, Tag


class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tags.through
    extra = 3

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'course']
    list_filter = ['subject', 'created_date']
    search_fields = ['subject', 'course__subject']
    readonly_fields = ['image_view']
    inlines = [LessonTagInlineAdmin]

    exclude = ['tag']

    def image_view(self, lesson):
        return mark_safe(f'<img src="/static/{lesson.image.name}" />')


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
