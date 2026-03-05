# slider/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Админка для управления изображениями слайдера"""
    
    list_display = ('thumbnail_preview', 'title', 'description_short', 'is_active', 'order')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'image_preview')
    
    fieldsets = (
        (_('Основная информация'), {
            'fields': ('title', 'description', 'image')
        }),
        (_('Настройки отображения'), {
            'fields': ('is_active', 'order')
        }),
        (_('Дополнительно'), {
            'fields': ('image_preview', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def thumbnail_preview(self, obj):
        """Отображение превью изображения в списке"""
        if obj.image and obj.image.thumbnails:
            thumb = obj.image.thumbnails['admin_thumb']
            return format_html(
                '<img src="{}" style="max-width: 80px; max-height: 60px; border-radius: 4px;" />',
                thumb.url
            )
        return _('Нет изображения')
    thumbnail_preview.short_description = _('Превью')
    
    def description_short(self, obj):
        """Краткое описание в списке"""
        if obj.description:
            return obj.description[:50] + ('...' if len(obj.description) > 50 else '')
        return '—'
    description_short.short_description = _('Описание')
    
    def image_preview(self, obj):
        """Полноразмерное превью в форме редактирования"""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px;" />',
                obj.image.url
            )
        return _('Изображение не загружено')
    image_preview.short_description = _('Просмотр изображения')