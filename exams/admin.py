from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Exam, Question, ExamResult

class ExamResultAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'exam', 'score']  # Make user, exam, and score read-only

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exam_results.csv"'

        writer = csv.writer(response)
        writer.writerow(['Username', 'Exam Title', 'Score', 'Grade'])

        for result in queryset:
            grade = self.calculate_grade(result.score)
            writer.writerow([result.user.username, result.exam.title, result.score, grade])

        return response

    def calculate_grade(self, score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    export_as_csv.short_description = "Export selected results as CSV"

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(ExamResult, ExamResultAdmin)
