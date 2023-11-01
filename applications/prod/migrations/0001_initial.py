# Generated by Django 4.2.5 on 2023-10-08 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Unidad_Venta',
            },
        ),
        migrations.CreateModel(
            name='Unidad_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Unidad_Compra',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=60)),
                ('sku', models.CharField(max_length=20)),
                ('upc', models.CharField(max_length=20)),
                ('cuenta_contable', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_sat', models.CharField(blank=True, max_length=20, null=True)),
                ('unidad_sat', models.CharField(blank=True, max_length=20, null=True)),
                ('qrcaja', models.CharField(blank=True, max_length=20, null=True)),
                ('qrpalet', models.CharField(blank=True, max_length=20, null=True)),
                ('costo_promedio', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('margen', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('comentario', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prod.categoria')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('unidad_compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prod.unidad_compra')),
                ('unidad_venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prod.unidad_venta')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
