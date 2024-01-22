# Generated by Django 4.0.6 on 2022-07-29 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rlbApp', '0004_rename_id_cliente_fk_mesa_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_cliente_fk',
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL),
        ),
    ]