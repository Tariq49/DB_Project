# Generated by Django 5.0.6 on 2024-07-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_remove_product_categories_product_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, unique=True)),
            ],
            options={
                "db_table": "tag_table",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(related_name="products", to="product.tag"),
        ),
    ]