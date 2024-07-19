from django.db import models
from apps.product.models import Product

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=5, decimal_places=0)
    order_date = models.DateField()
    

    class Meta:
        db_table = 'order_table'
        constraints = [
            models.CheckConstraint(check=models.Q(order_quantity__gte=0), name='order_table_order_quantity_check')
        ]
