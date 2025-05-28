from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category, Product
from decimal import Decimal
from datetime import datetime

class Command(BaseCommand):
    help = 'Add sample gaming products to the database'

    def handle(self, *args, **kwargs):
        # Create categories
        categories = {
            'Gaming Consoles': 'Latest gaming consoles and bundles',
            'Gaming Peripherals': 'High-performance gaming mice, keyboards, and controllers',
            'Gaming Chairs': 'Ergonomic gaming chairs for long gaming sessions',
            'Gaming Monitors': 'High refresh rate gaming monitors'
        }

        # Create categories first
        created_categories = {}
        for cat_name, cat_desc in categories.items():
            category, created = Category.objects.get_or_create(
                name=cat_name,
                slug=slugify(cat_name)
            )
            created_categories[cat_name] = category
            if created:
                self.stdout.write(f'Created category: {cat_name}')

        # Product data
        products = [
            {
                'category': 'Gaming Consoles',
                'name': 'PlayStation 5 Digital Edition',
                'description': 'Next-gen gaming console with 825GB SSD, 4K support, and ray tracing',
                'price': Decimal('399.99'),
                'image': 'products/ps5-digital.jpg',
                'stock': 10,
                'available': True
            },
            {
                'category': 'Gaming Consoles',
                'name': 'Xbox Series X',
                'description': '4K gaming at 60 FPS, 1TB SSD, backward compatibility with Xbox games',
                'price': Decimal('499.99'),
                'image': 'products/xbox-series-x.jpg',
                'stock': 15,
                'available': True
            },
            {
                'category': 'Gaming Peripherals',
                'name': 'Razer DeathAdder V3 Pro',
                'description': 'Ultra-lightweight wireless gaming mouse with 30K DPI optical sensor',
                'price': Decimal('149.99'),
                'image': 'products/razer-deathadder.jpg',
                'stock': 25,
                'available': True
            },
            {
                'category': 'Gaming Peripherals',
                'name': 'SteelSeries Apex Pro TKL',
                'description': 'Mechanical gaming keyboard with adjustable actuation and OLED display',
                'price': Decimal('189.99'),
                'image': 'products/apex-pro.jpg',
                'stock': 20,
                'available': True
            },
            {
                'category': 'Gaming Monitors',
                'name': 'ASUS ROG Swift PG279QM',
                'description': '27" 1440p IPS gaming monitor with 240Hz refresh rate and G-Sync',
                'price': Decimal('799.99'),
                'image': 'products/rog-swift.jpg',
                'stock': 8,
                'available': True
            },
            {
                'category': 'Gaming Monitors',
                'name': 'Samsung Odyssey G7',
                'description': '32" curved gaming monitor with 240Hz refresh rate and QLED technology',
                'price': Decimal('699.99'),
                'image': 'products/odyssey-g7.jpg',
                'stock': 12,
                'available': True
            },
            {
                'category': 'Gaming Chairs',
                'name': 'Secretlab TITAN Evo 2022',
                'description': 'Premium gaming chair with 4-way L-ADAPT lumbar support',
                'price': Decimal('549.99'),
                'image': 'products/titan-evo.jpg',
                'stock': 15,
                'available': True
            },
            {
                'category': 'Gaming Chairs',
                'name': 'Razer Iskur X',
                'description': 'Ergonomic gaming chair with multi-layered synthetic leather',
                'price': Decimal('399.99'),
                'image': 'products/iskur-x.jpg',
                'stock': 18,
                'available': True
            },
            {
                'category': 'Gaming Peripherals',
                'name': 'Logitech G Pro X Wireless',
                'description': 'Professional gaming headset with Blue VO!CE technology',
                'price': Decimal('199.99'),
                'image': 'products/g-pro-x.jpg',
                'stock': 30,
                'available': True
            },
            {
                'category': 'Gaming Peripherals',
                'name': 'CORSAIR K100 RGB',
                'description': 'Optical-mechanical gaming keyboard with per-key RGB',
                'price': Decimal('229.99'),
                'image': 'products/k100-rgb.jpg',
                'stock': 22,
                'available': True
            }
        ]

        # Create products
        for product_data in products:
            category = created_categories[product_data['category']]
            product, created = Product.objects.get_or_create(
                category=category,
                name=product_data['name'],
                defaults={
                    'slug': slugify(product_data['name']),
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'image': product_data['image'],
                    'available': product_data['available']
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
            else:
                self.stdout.write(f'Product "{product_data["name"]}" already exists') 