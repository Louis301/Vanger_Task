# slider/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    """Модель изображения для слайдера"""
    
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=255,
        help_text=_('Название изображения для отображения в админке')
    )
    image = FilerImageField(
        verbose_name=_('Изображение'),
        on_delete=models.CASCADE,
        related_name='slider_images',
        help_text=_('Загрузите изображение для слайдера через django-filer'),
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        blank=True,
        help_text=_('Дополнительное описание (опционально)')
    )
    order = models.PositiveIntegerField(
        verbose_name=_('Порядок'),
        default=0,
        help_text=_('Порядок сортировки (управляется drag&drop в админке)')
    )
    is_active = models.BooleanField(
        verbose_name=_('Активно'),
        default=True,
        help_text=_('Показывать изображение в слайдере')
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Изображение слайдера')
        verbose_name_plural = _('Изображения слайдера')
        ordering = ['order']

    def __str__(self):
        return self.title or f'Изображение #{self.id}'