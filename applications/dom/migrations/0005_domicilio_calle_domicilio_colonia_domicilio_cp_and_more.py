# Generated by Django 4.2.5 on 2023-10-15 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0004_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='domicilio',
            name='calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='colonia',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='cp',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='entidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dom.entidad'),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dom.municipio'),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='numero_externo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='numero_interno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dom.pais'),
        ),
    ]
