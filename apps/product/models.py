from django.db import models
from apps.supplier.models import Supplier

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name 
    
    class Meta:
        db_table = 'tag_table'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='products', null=True, blank=True)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity_in_stock = models.DecimalField(max_digits=5, decimal_places=0)
    reorder_level = models.SmallIntegerField()
    expiry_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.product_name}'
    
    class Meta:
        db_table = 'product_table'
        constraints = [
            models.CheckConstraint(check=models.Q(quantity_in_stock__gte=0), name='product_table_quantity_in_stock_check'),
            models.CheckConstraint(check=models.Q(reorder_level__gte=0), name='product_table_reorder_level_check'),
            models.CheckConstraint(check=models.Q(unit_price__gte=0), name='product_table_unit_price_check')
        ]
