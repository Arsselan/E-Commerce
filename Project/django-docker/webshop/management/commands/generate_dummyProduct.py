#author: Arsselan
from random import choice, randint
from faker import Faker
from django.core.management.base import BaseCommand
from ...models import Product, Seller

fake = Faker()

class Command(BaseCommand):
    help = 'Generiert Dummy-Sportproduktdaten'

    def handle(self, *args, **kwargs):
        sellers = Seller.objects.all()

        sports = [
            'Fußball', 'Basketball', 'Tennis', 'Volleyball', 'Schwimmen', 
            'Laufen', 'Golf', 'Radsport', 'Boxen', 'Yoga'
        ]

        adjectives = [
            'Hochleistungs-', 'Komfortable', 'Professionelle', 'Ergonomische', 'Wetterbeständige',
            'Leichte', 'Robuste', 'Atmungsaktive', 'Stilvolle', 'Unterstützende'
        ]

        products = []

        for _ in range(10):
            seller = choice(sellers)
            sport = choice(sports)
            adjective = choice(adjectives)

            product_name = f"{adjective}{sport} {fake.word()}"
            product_desc = f"{adjective} {sport} für {fake.sentence()}"

            products.append({
                'seller': seller,
                'name': product_name,
                'desc': product_desc,
                'price': randint(10, 1000),
                'stock': randint(0, 100),
            })

        Product.objects.bulk_create(
            Product(**product_data) for product_data in products
        )

        self.stdout.write(self.style.SUCCESS('Dummy-Sportproduktdaten wurden erfolgreich generiert.'))
