from django.contrib import admin


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bdate', 'country', 'city', 'photo_200')
    list_display_links = ('first_name', 'last_name', 'bdate', 'country', 'city')
    search_fields = ('first_name', 'last_name', 'bdate', 'country', 'city')
