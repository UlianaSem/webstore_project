from django import forms
from django.forms import BaseInlineFormSet

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    PROHIBITED_GOODS = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

    class Meta:
        model = Product
        exclude = ('owner', )

    def _clean(self, cleaned_data):

        cleaned_data_list = set(cleaned_data.lower().split(' '))

        if self.PROHIBITED_GOODS.intersection(cleaned_data_list):
            raise forms.ValidationError("Вы пытаетесь добавить запрещенный товар. Попробуйте добавить другой товар.")

        return cleaned_data

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        return self._clean(cleaned_data)

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        return self._clean(cleaned_data)


class ProductModeratorForm(forms.ModelForm):

    PROHIBITED_GOODS = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

    class Meta:
        model = Product
        fields = ['description', 'category_id', 'is_published']

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        cleaned_data_list = set(cleaned_data.lower().split(' '))

        if self.PROHIBITED_GOODS.intersection(cleaned_data_list):
            raise forms.ValidationError("Вы пытаетесь добавить запрещенный товар. Попробуйте добавить другой товар.")

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"


class CustomInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        is_active_count = len([form for form in self.forms if form.instance.is_active])

        if is_active_count > 1:
            raise forms.ValidationError('Может быть только одна активная версия. Прежде чем создать новую, '
                                        'деактивируйте предыдущую')
