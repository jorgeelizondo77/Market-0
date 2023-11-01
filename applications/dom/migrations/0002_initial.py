# Generated by Django 4.2.5 on 2023-10-05 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='municipio',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dom.entidad'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dom.pais'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entidad',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dom.pais'),
        ),
        migrations.AddField(
            model_name='entidad',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
    ]