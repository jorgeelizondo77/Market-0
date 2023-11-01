# Generated by Django 4.2.5 on 2023-10-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oc', '0004_rename_cantidad_orden_compra_total_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden_compra',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='orden_compra_detalle',
            name='importe',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]