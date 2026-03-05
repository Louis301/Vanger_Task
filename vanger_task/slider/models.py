# slider/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    """Модель изображения для слайдера"""
    
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
        help_text=_('Название изображения для отображения в админке')
    )
    image = FilerImageField(
        _('Изображение'),
        on_delete=models.CASCADE,
        related_name='slider_images',
        help_text=_('Загрузите изображение для слайдера через django-filer')
    )
    description = models.TextField(
        _('Описание'),
        blank=True,
        help_text=_('Дополнительное описание (опционально)')
    )
    order = models.PositiveIntegerField(
        _('Порядок'),
        default=0,
        help_text=_('Порядок сортировки (управляется drag&drop в админке)')
    )
    is_active = models.BooleanField(
        _('Активно'),
        default=True,
        help_text=_('Показывать изображение в слайдере')
    )
    created_at = models.DateTimeField(
        _('Дата создания'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Изображение слайдера')
        verbose_name_plural = _('Изображения слайдера')
        ordering = ['order']

    def __str__(self):
        return self.title or f'Изображение #{self.id}'

    def thumbnail(self):
        """Метод для отображения превью в админке"""
        if self.image and self.image.thumbnails:
            return self.image.thumbnails['admin_thumb']
        return None
    thumbnail.short_description = _('Превью')