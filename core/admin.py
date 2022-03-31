from django.contrib import admin
from core.models import Article, Author, ArticleImage, Carousel, HeadingArticle

# Register your models here.

admin.site.register(ArticleImage)

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ('title', 'is_active', 'updated_at', 'heading')
    list_editable = ('is_active', 'heading')
    ordering = ['-created_at']
    list_filter = ['is_active', 'updated_at', 'main_article', 'center_article', 'right_panel_article', 'text_article', 'margin_article_text', 'slug', 'pagination_article', 'carousel_block']
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ("title",)}
    fields = ('title', 'text', 'picture', 'created_at', 'updated_at', 'main_article', 'center_article', 'right_panel_article', 'margin_article_text', 'text_article',  'pagination_article', 'carousel_block', 'heading', 'slug', 'metades')
    readonly_fields = ('created_at', 'updated_at')




class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author

    list_display = ('user', 'nik')
    list_editable = ('nik',)
    ordering = ['nik']
    prepopulated_fields = {'slug': ("user",)}
    list_filter = ['nik', 'slug',]
    search_fields = ['nik',]

    fields = ('nik', 'user', 'photo', 'slug',)
    readonly_fields = ('nik',)



admin.site.register(Article, ArticleAdmin)
admin.site.register(HeadingArticle)
admin.site.register(Carousel)
admin.site.register(Author, AuthorAdmin)

# Register your models here.
