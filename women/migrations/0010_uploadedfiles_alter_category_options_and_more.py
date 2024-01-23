# Generated by Django 5.0.1 on 2024-01-23 01:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("women", "0009_husband_women_husband"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadedFiles",
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
                ("file", models.FileField(upload_to="uploads_model")),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="women",
            options={
                "ordering": ["-time_create"],
                "verbose_name": "Famous woman",
                "verbose_name_plural": "Famous women",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                db_index=True, max_length=100, verbose_name="Category"
            ),
        ),
        migrations.AlterField(
            model_name="women",
            name="content",
            field=models.TextField(blank=True, verbose_name="Article"),
        ),
        migrations.AlterField(
            model_name="women",
            name="is_published",
            field=models.BooleanField(
                choices=[(False, "Draft"), (True, "Published")],
                default=0,
                verbose_name="status",
            ),
        ),
        migrations.AlterField(
            model_name="women",
            name="title",
            field=models.CharField(max_length=255, verbose_name="women title"),
        ),
    ]