from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier_id = models.PositiveSmallIntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=50)

    def __str__(self)-> str:
        return f'{self.supplier_name}'
    
    class Meta:
        db_table = 'supplier_table'