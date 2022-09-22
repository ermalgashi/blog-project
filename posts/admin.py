from django.contrib import admin
from .models import Posts, Category, Contact


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    readonly_fields = ("author",)

    def save_model(self, request, obj, form, change):
        if getattr(obj, "author", None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category)
admin.site.register(Contact)
