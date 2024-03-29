# Generated by Django 4.2.9 on 2024-01-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("adress", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("imageLink", models.CharField(max_length=100)),
                ("idioms", models.CharField(max_length=100)),
                ("currentJob", models.CharField(max_length=100)),
                ("mainFormation", models.CharField(max_length=100)),
                ("socialMedia", models.CharField(max_length=100)),
                ("mainStack", models.CharField(max_length=100)),
                ("problemsISolve", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Academic",
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
                ("title", models.CharField(max_length=100)),
                ("imageLink", models.CharField(max_length=100)),
                ("shortDescription", models.CharField(max_length=200)),
                ("when", models.CharField(max_length=100)),
                ("where", models.CharField(max_length=100)),
                ("challenges", models.CharField(max_length=100)),
                ("Achievements", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Achievements",
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
                ("title", models.CharField(max_length=100)),
                ("imageLink", models.CharField(max_length=100)),
                ("shortDescription", models.CharField(max_length=200)),
                ("when", models.CharField(max_length=100)),
                ("where", models.CharField(max_length=100)),
                ("challenges", models.CharField(max_length=100)),
                ("Achievements", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Jobs",
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
                ("title", models.CharField(max_length=100)),
                ("imageLink", models.CharField(max_length=100)),
                ("shortDescription", models.CharField(max_length=200)),
                ("when", models.CharField(max_length=100)),
                ("where", models.CharField(max_length=100)),
                ("challenges", models.CharField(max_length=100)),
                ("Achievements", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
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
                ("projectType", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("imageLink", models.CharField(max_length=100)),
                ("shortDescription", models.CharField(max_length=200)),
                ("projectLink", models.CharField(max_length=100)),
                ("updatedAt", models.DateField()),
            ],
        ),
    ]
