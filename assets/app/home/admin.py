from django.contrib import admin
from app.home.models import Posts


class PostsAdmin(admin.ModelAdmin):
    search_fields = [
        'title', 'content',
    ]
    # list_editable = [
    #     'content'
    # ]
    list_display = [
        'title',
        # 'content',
        'date_posted',
        'active',
    ]


admin.site.register(Posts, PostsAdmin)
