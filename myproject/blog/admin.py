from django.contrib import admin
from .models import Article, Category

# Admin site change header
admin.site.site_header = "مدیریت وبلاگ دکتر مریم امیری"

# Register your models here.
def make_published(modeladmin, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
             message_bit = "منتشر شد."
        else:
             message_bit = "منتشر شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated,  message_bit))
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_drafted(modeladmin, request, queryset):
        rows_updated = queryset.update(status='d')
        if rows_updated == 1:
             message_bit = "پیش نویس شد."
        else:
             message_bit = "پیش نویس شدند."
        modeladmin.message_user(request, "{} مقاله {}".format(rows_updated,  message_bit))
make_drafted.short_description = "پیش نویس کردن مقالات انتخاب شده"

def make_category_published(modeladmin, request, queryset):
        rows_updated = queryset.update(status=True)
        if rows_updated == 1:
             message_bit = "منتشر شد."
        else:
             message_bit = "منتشر شدند."
        modeladmin.message_user(request, "{} دسته {}".format(rows_updated,  message_bit))
make_category_published.short_description = "انتشار دسته های انتخاب شده"

def make_category_drafted(modeladmin, request, queryset):
        rows_updated = queryset.update(status=False)
        if rows_updated == 1:
             message_bit = "غیرفعال شد."
        else:
             message_bit = "غیرفعال شدند."
        modeladmin.message_user(request, "{} دسته {}".format(rows_updated,  message_bit))
make_category_drafted.short_description = "غیرفعال کردن دسته های انتخاب شده"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','parent', 'status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_category_published, make_category_drafted]

admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','author','jpublish','status','category_to_str')
    list_filter = ('publish','status', 'author')
    search_fields = ('title','description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']
    actions = [make_published, make_drafted]

admin.site.register(Article, ArticleAdmin)