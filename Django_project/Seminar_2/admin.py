from django.contrib import admin
from .models import Author, Games


# Register your models here.
@admin.action(description='Обновляем биографию')
def update_name_bio(modeladmin, request, queryset):
    queryset.update(biography='Новая биография')
    queryset.update(name='Новое имя')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'email', 'birthday']
    ordering = ['-birthday']
    list_per_page = 5
    search_fields = ['name']
    actions = [update_name_bio]
    fieldsets = [
        (
            'Автор',
            {
                # 'classes': ['wide'],  # закомитить чтобы выводилось в одну строку
                'fields': [('name', 'lastname')],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['biography'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Дополнительная информация',
                'fields': ['birthday'],
            }
        ),
    ]


# admin.site.register(Author, AuthorAdmin)
admin.site.register(Games)
