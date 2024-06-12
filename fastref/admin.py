from django.contrib import admin
from .models import Category, Language, Feedback

# Custom admin class for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'language_name', 'is_deleted')

# Custom admin class for Language model
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'description', 'is_deleted', 'bg_color')
    # list_display = ('id', 'name', 'logo', 'category_id', 'description', 'is_deleted', 'bg_color', 'html')

# Custom admin class for Feedback model
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email_id', 'feedback')

# Register your models with the custom admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Feedback, FeedbackAdmin)
