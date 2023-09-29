from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                main_count += 1
        if main_count > 1:
            raise ValidationError('Основной раздел может быть только один')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = Article.scope.through
    formset = ArticleScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleScopeInline,
    ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [
        ArticleScopeInline,
    ]

