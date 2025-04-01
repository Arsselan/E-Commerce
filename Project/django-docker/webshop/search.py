

# author: Sarish
from .models import Product

def search_products(query):
    # Suche nach Produkten, die den Suchbegriff enthalten
    results = Product.objects.filter(name__icontains=query)
    return results