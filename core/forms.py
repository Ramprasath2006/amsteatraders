from django import forms
from .models import ContactInquiry, Review


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'you@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '+91 98765 43210'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Write your message here...',
                'rows': 5
            }),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Your Name', 'required': 'required'
            }),
            'rating': forms.Select(choices=[(i, f"{i} Stars") for i in range(5, 0, -1)], attrs={
                'class': 'form-control', 'required': 'required'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Write your review comments here...',
                'rows': 4, 'required': 'required'
            }),
        }

