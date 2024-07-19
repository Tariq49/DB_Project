products = Product.objects.all()



# Get products with unit_price greater than 50
expensive_products = Product.objects.filter(unit_price__gt=50)

# Get products with a specific name
named_product = Product.objects.filter(product_name="NaCl 0.9% 100ml")

# Get products that are not in a specific category
non_fluid_products = Product.objects.exclude(category__category_name="Fluids")

# Get a product by primary key
product = Product.objects.get(pk=1)

exact_product = Product.objects.filter(product_name__exact="NaCl 0.9% 100ml")

# case insensitive
case_insensitive_product = Product.objects.filter(product_name__iexact="nacl 0.9% 100ml")

# contains substring match
products_with_nacl = Product.objects.filter(product_name__contains="NaCl")

# starts with 
products_starting_with_n = Product.objects.filter(product_name__startswith="N")

# in a list
selected_products = Product.objects.filter(product_name__in=["NaCl 0.9% 100ml", "Intrafix Safeset"])

# Aggregations 

# Count

from django.db.models import Count

product_count = Product.objects.count()

# Sum, Avg, Max, Min 
from django.db.models import Sum, Avg, Max, Min

total_quantity = Product.objects.aggregate(Sum('quantity_in_stock'))
average_price = Product.objects.aggregate(Avg('unit_price'))
max_price = Product.objects.aggregate(Max('unit_price'))
min_price = Product.objects.aggregate(Min('unit_price'))

# prefetch related objects
products = Product.objects.prefetch_related('tags').all()

# Get all products supplied by a specific supplier
supplier = Supplier.objects.get(pk=1)
supplier_products = supplier.product_set.all()


from django.db.models import Q

# Products with unit price greater than 50 or quantity in stock less than 10
complex_query_products = Product.objects.filter(Q(unit_price__gt=50) | Q(quantity_in_stock__lt=10))

# Get the first 5 products
limited_products = Product.objects.all()[:5]

# Update the unit price of a product
Product.objects.filter(pk=1).update(unit_price=55.00)


# Delete a product
Product.objects.filter(pk=1).delete()
