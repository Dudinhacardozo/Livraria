# Generated by Django 5.0.2 on 2024-08-16 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_autor_email_livro"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name": "Autor", "verbose_name_plural": "Autores"},
        ),
    ]