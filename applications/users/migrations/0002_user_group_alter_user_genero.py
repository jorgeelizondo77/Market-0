# Generated by Django 4.2.5 on 2023-10-15 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usr_group', to='auth.group', verbose_name='Perfil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='genero',
            field=models.CharField(blank=True, choices=[('O', ''), ('H', 'Hombre'), ('M', 'Mujer')], max_length=1),
        ),
    ]