from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    PROHIBITED_GOODS = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

    class Meta:
        model = Product
        fields = "__all__"

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


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"
