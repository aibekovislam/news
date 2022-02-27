from django.contrib import admin
from core.models import Article, Author, ArticleImage, HeadingArticle

# Register your models here.

admin.site.register(Author)
admin.site.register(ArticleImage)

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ('title', 'is_active', 'updated_at', 'heading')
    list_editable = ('is_active', 'heading')
    ordering = ['-created_at']
    list_filter = ['is_active', 'updated_at', 'main_article', 'center_article', 'right_panel_article', 'text_article', 'margin_article_text']
    search_fields = ['title', 'text']

    fields = ('title', 'text', 'picture', 'created_at', 'updated_at', 'main_article', 'center_article', 'right_panel_article', 'margin_article_text', 'text_article', 'heading')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(HeadingArticle)
# Register your models here.
