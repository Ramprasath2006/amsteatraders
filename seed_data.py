import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amstea.settings')
django.setup()

from core.models import Category, Product
from django.contrib.auth.models import User

# Superuser (username: admin / password: admin123) for local testing
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@amsteatraders.com', 'admin123')
    print("Superuser created: admin / admin123")

# Clear existing categories and products to avoid duplication or stale data
Product.objects.all().delete()
Category.objects.all().delete()

categories_data = [
    {"name": "Dust Tea", "description": "Finely ground tea leaves offering a strong, robust, and quick brew.", "order": 1},
    {"name": "Hotel Blend", "description": "Specially formulated tea blend perfect for hotels, restaurants, and catering.", "order": 2},
    {"name": "Premium Tea Dust", "description": "High-grade fine tea dust for a rich, quick-brewing cup of tea.", "order": 3},
    {"name": "BOP", "description": "Broken Orange Pekoe, offering a well-balanced flavor and medium strength.", "order": 4},
    {"name": "Leaf Tea", "description": "Whole or large broken tea leaves for a smooth, aromatic, and flavorful cup.", "order": 5},
]

categories = {}
for c in categories_data:
    obj, _ = Category.objects.get_or_create(name=c["name"], defaults={"description": c["description"], "order": c["order"]})
    categories[c["name"]] = obj

products_data = [
    {"name": "Assam Tea", "category": "Leaf Tea",
     "short_description": "A strong, rich, and malty whole leaf black tea directly from the estates of Assam.",
     "price": 420, "unit": "per kg", "is_featured": True},
    {"name": "Darjeeling Classic Tea", "category": "Leaf Tea",
     "short_description": "A delicate whole leaf black tea with a refined floral aroma and complex flavor.",
     "price": 650, "unit": "per kg", "is_featured": True},
    {"name": "Herbal Tea", "category": "Leaf Tea",
     "short_description": "A soothing, caffeine-free infusion of pure chamomile, herbs, and flowers.",
     "price": 380, "unit": "per kg", "is_featured": True},
    {"name": "Masala Tea", "category": "Hotel Blend",
     "short_description": "A warm and spicy blend of robust black tea infused with premium Indian spices.",
     "price": 400, "unit": "per kg", "is_featured": True},

    # Other products (not featured)
    {"name": "Dust Tea", "category": "Dust Tea",
     "short_description": "Finely ground tea leaves offering a strong, robust, and quick-brewing cup.",
     "price": 320, "unit": "per kg", "is_featured": False},
    {"name": "Hotel Blend", "category": "Hotel Blend",
     "short_description": "Specially formulated tea blend perfect for hotels, restaurants, and catering.",
     "price": 350, "unit": "per kg", "is_featured": False},
    {"name": "Premium Tea Dust", "category": "Premium Tea Dust",
     "short_description": "High-grade fine tea dust for a rich, quick-brewing cup of tea.",
     "price": 420, "unit": "per kg", "is_featured": False},
    {"name": "BOP", "category": "BOP",
     "short_description": "Broken Orange Pekoe, offering a well-balanced flavor and medium strength.",
     "price": 450, "unit": "per kg", "is_featured": False},
    {"name": "Leaf Tea", "category": "Leaf Tea",
     "short_description": "Whole or large broken tea leaves for a smooth, aromatic, and flavorful cup.",
     "price": 600, "unit": "per kg", "is_featured": False},
]

for p in products_data:
    Product.objects.create(
        name=p["name"],
        category=categories[p["category"]],
        short_description=p["short_description"],
        price=p["price"],
        unit=p["unit"],
        is_featured=p["is_featured"],
        is_active=True,
    )

print(f"Seeded {Category.objects.count()} categories and {Product.objects.count()} products.")
