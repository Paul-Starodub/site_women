# Generated by Django 5.0.1 on 2024-01-20 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("women", "0006_alter_women_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="women",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="posts",
                to="women.category",
            ),
        ),
    ]
