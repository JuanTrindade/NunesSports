# Generated by Django 5.0 on 2023-12-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nunesapp", "0002_rename_produtos_produto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="preco_produto",
            field=models.FloatField(),
        ),
    ]
