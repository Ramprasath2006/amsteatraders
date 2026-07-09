from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Product, Review
from .forms import ContactForm, ReviewForm


def home(request):
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:6]
    categories = Category.objects.all()[:5]
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'page_title': 'Home',
    }
    return render(request, 'core/home.html', context)


def products(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your review has been submitted successfully.")
            return redirect('products')
    else:
        form = ReviewForm()

    category_slug = request.GET.get('category')
    sort_by = request.GET.get('sort')
    all_products = Product.objects.filter(is_active=True).exclude(is_featured=True)
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:4]
    user_reviews = Review.objects.filter(is_approved=True)

    if category_slug:
        all_products = all_products.filter(category__slug=category_slug)

    if sort_by == 'name':
        all_products = all_products.order_by('name')
    else:
        all_products = all_products.order_by('category__order', 'name')

    context = {
        'products': all_products,
        'categories': categories,
        'featured_products': featured_products,
        'selected_category': category_slug,
        'selected_sort': sort_by,
        'user_reviews': user_reviews,
        'review_form': form,
        'page_title': 'Product & Review',
    }
    return render(request, 'core/products.html', context)


def about(request):
    context = {'page_title': 'About Us'}
    return render(request, 'core/about.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for reaching out! Your message has been received. "
                "Our team will get back to you shortly."
            )
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below and try again.")
    else:
        form = ContactForm()

    context = {
        'form': form,
        'page_title': 'Contact Us',
    }
    return render(request, 'core/contact.html', context)
