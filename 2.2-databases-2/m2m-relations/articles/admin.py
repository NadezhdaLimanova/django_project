from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
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

