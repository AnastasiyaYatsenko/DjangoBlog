from django.contrib import admin
import posts.models


class PostCategoriesInline(admin.TabularInline):
    model = posts.models.Post.categories.through


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [PostCategoriesInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')


admin.site.register(posts.models.Post, PostAdmin)
admin.site.register(posts.models.Category, CategoryAdmin)
