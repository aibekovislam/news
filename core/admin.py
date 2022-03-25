from django.contrib import admin
from core.models import Article, Author, ArticleImage, Carousel, HeadingArticle

# Register your models here.

admin.site.register(Author)
admin.site.register(ArticleImage)

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ('title', 'is_active', 'updated_at', 'heading')
    list_editable = ('is_active', 'heading')
    ordering = ['-created_at']
    list_filter = ['is_active', 'updated_at', 'main_article', 'center_article', 'right_panel_article', 'text_article', 'margin_article_text', 'slug', 'pagination_article', 'carousel_block', 'article_page_main']
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ("title",)}
    fields = ('title', 'text', 'picture', 'created_at', 'updated_at', 'main_article', 'center_article', 'right_panel_article', 'margin_article_text', 'text_article',  'pagination_article', 'carousel_block', 'article_page_main', 'heading', 'slug',)
    readonly_fields = ('created_at', 'updated_at')








admin.site.register(Article, ArticleAdmin)
admin.site.register(HeadingArticle)
admin.site.register(Carousel)

# Register your models here.
