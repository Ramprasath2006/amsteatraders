from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Tea product category, e.g. Black Tea, Green Tea, Herbal Tea."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def get_image_url(self):
        product_with_image = self.products.filter(is_featured=False, image__isnull=False).exclude(image='').first()
        if product_with_image and product_with_image.image:
            return product_with_image.image.url
        return None


class Product(models.Model):
    """A tea product or service offered by A M S Tea Traders."""
    category = models.ForeignKey(
        Category, related_name='products',
        on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=50, default='per kg', blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products') + f'#{self.slug}'


class ContactInquiry(models.Model):
    """Message submitted via the Contact Us form."""
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject or 'Inquiry'} ({self.created_at:%Y-%m-%d})"


class Review(models.Model):
    """Customer review submitted via the website."""
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating} stars ({self.created_at:%Y-%m-%d})"

