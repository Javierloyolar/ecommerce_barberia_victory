import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_barberia.settings')
django.setup()
from products.models import Category, Product


# 1. Crear Categorías

cat_barba, _ = Category.objects.get_or_create(name='Cuidado de Barba')
cat_cabello, _ = Category.objects.get_or_create(name='Estilizado de Cabello')
cat_herramientas, _ = Category.objects.get_or_create(name='Herramientas Profesionales')

# 2. Crear Productos

products_data = [
{'name': 'Aceite para Barba Premium', 'price': 12990, 'stock': 50, 'category': cat_barba},
{'name': 'Pomada Mate Victory', 'price': 15500, 'stock': 35, 'category': cat_cabello},
{'name': 'Bálsamo para Barba', 'price': 10990, 'stock': 20, 'category': cat_barba},
]
for p in products_data:

    Product.objects.get_or_create(**p)
    print("¡Base de datos de Victory Barber poblada con éxito!")