from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django.utils.html import format_html

class PostAdminForm(forms.ModelForm):
    

    class Meta:
        model = Person
        fields = '__all__'

class FirmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'count_person', 'get_productions', 'get_place', 'location')
    list_display_links = ['id', 'title']
    search_fields = ('title',)
    list_filter = ('productions', 'place', 'count_person')
    readonly_fields = ('count_person', )
    fields = ('title', 'slug', 'productions', 'place', 'count_person', 'main_inf', 'photo', 'location')

    def get_productions(self, obj):
        return format_html(', '.join(productions.title for productions in obj.productions.all()))
   
    get_productions.short_description = 'productions'

    def get_place(self, obj):
        return format_html(', '.join(place.place for place in obj.place.all()))
   
    get_place.short_description = 'place'

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    form = PostAdminForm    
    save_as = True
    save_on_top = True
    list_display = ['id', 'name', 'profession', 'current_place']
    list_display_links = ['id', 'name']
    search_fields = ('name',)
    list_filter = ('current_place', )
    fields = ('name', 'slug', 'profession', 'current_place', 'main_inf', 'photo', 'age', 'gender', 'adress', 'nationality', 'family_status', 'education', 'experience', 'telegram', 'viber', 'skype', 'mail', 'phone')

admin.site.register(Production)
admin.site.register(Place)
admin.site.register(Firm, FirmAdmin)
admin.site.register(Person, PersonAdmin)