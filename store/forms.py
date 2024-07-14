from django import forms
from .models import Product, Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# For creating and updating product instances in the 'Product' model.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category','description', 'image', 'user']


# For creating and updating order instances in the 'Order' model.
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []    # Empty list ([]) means all fields from the 'Order' model will be included by default.


# Form for user login. Inherits from Django's built-in AuthenticationForm that provides username and password fields.
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Customizing the widget attributes for better appearance.
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})


# Form for user registration. Inherits from Django's built-in UserCreationForm that needs to be imported.
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        # This is an additional field for specifying properties like email length, styling, etc.
        max_length=254,
        required=True,
        help_text='Required. Enter a valid email address.',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Customizing the widget attributes for better appearance and adds placeholders for input.
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email Address'})
