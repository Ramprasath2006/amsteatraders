# A M S Tea Traders — Django Website

A full-stack business website built with Django (backend) and HTML/CSS/JavaScript (frontend).

## Features
- 5 pages: Home, Products & Services, About Us, Gallery, Contact Us
- Shared `base.html` layout with common header and **identical footer on every page**
- `Category` and `Product` models — products are pulled live from the database, filterable by category
- `ContactInquiry` model — the Contact form saves every submission to the database
- Fully responsive green & white design (mobile nav toggle, responsive grid/footer)
- Django admin panel for managing categories, products, and viewing contact inquiries

## Setup Instructions

```bash
# 1. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create an admin user (or use the seeded one below)
python manage.py createsuperuser

# 5. (Optional) Load sample tea categories & products
python seed_data.py

# 6. Run the development server
python manage.py runserver
```

Visit:
- Website: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Seeded Admin Login (from seed_data.py)
- Username: `admin`
- Password: `admin123`

**Change this password before deploying to production.**

## Project Structure
```
amstea/            Project settings, root urls.py
core/               App: models, views, forms, admin, urls
templates/          base.html, partials/(header, footer), core/(5 pages)
static/core/        css/style.css, js/script.js
media/products/     Uploaded product images (via admin)
```

## Adding Real Content
1. Go to `/admin/`, log in.
2. Add **Categories** (e.g. Black Tea, Green Tea, Herbal Tea, Masala Chai).
3. Add **Products** — assign a category, upload an image, set price/unit, mark as Featured to show on Home.
4. Uploaded product images automatically appear in the **Gallery** page too.
5. Messages submitted via **Contact Us** appear under **Contact Inquiries** in the admin.
