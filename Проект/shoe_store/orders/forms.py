from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('id',) 
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'min': 1}),
            'discount': forms.NumberInput(attrs={'min': 1, 'max': 99}),
            'stock': forms.NumberInput(attrs={'min': 0}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price
    
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError('Количество на складе не может быть отрицательным.')
        return stock
    
    def clean_discount(self):
        discount = self.cleaned_data.get('discount')
        if discount is not None and (discount < 0 or discount > 100):
            raise forms.ValidationError('Скидка должна быть от 0 до 100%.')
        return discount
