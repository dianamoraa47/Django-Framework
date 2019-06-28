from django.contrib import admin


from.models import Course

class CourseAdmin(admin.ModelAdmin):
	list_displays = ("Name", "Durations","Startdate","Enddate","Months")
	search_fields = ("Name", "Durations","Startdate","Enddate","Months")


admin.site.register(Course)


# Register your models here.
