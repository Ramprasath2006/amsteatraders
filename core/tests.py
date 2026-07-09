from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models import Category, Product


class CategoryImageTestCase(TestCase):
    def setUp(self):
        # Create a small dummy image for testing uploads
        self.dummy_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x05\x05\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
            content_type='image/jpeg'
        )

    def test_no_image_no_products(self):
        """If there is no category image and no product image, it should return None."""
        category = Category.objects.create(name="Green Tea")
        self.assertIsNone(category.get_image_url)

    def test_fallback_to_product_image(self):
        """If there is no category image, it should fall back to the first product's image."""
        category = Category.objects.create(name="Black Tea")
        product = Product.objects.create(
            category=category,
            name="Assam Black Tea",
            image=self.dummy_image
        )
        # Refresh from DB
        category.refresh_from_db()
        self.assertIsNotNone(category.get_image_url)
        self.assertEqual(category.get_image_url, product.image.url)

    def test_use_category_image(self):
        """If a category image is provided, it should be used instead of the product image."""
        category = Category.objects.create(
            name="Herbal Tea",
            image=self.dummy_image
        )
        self.assertIsNotNone(category.get_image_url)
        self.assertEqual(category.get_image_url, category.image.url)

