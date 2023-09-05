from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    PROHIBITED_GOODS = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

    class Meta:
        model = Product
        fields = "__all__"

    def _clean(self, cleaned_data):

        cleaned_data = set(cleaned_data.lower().split(' '))

        if not self.PROHIBITED_GOODS.intersection(cleaned_data):
            raise forms.ValidationError("Вы пытаетесь добавить запрещенный товар. Попробуйте добавить другой товар.")

        return cleaned_data

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        self._clean(cleaned_data)

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        self._clean(cleaned_data)
