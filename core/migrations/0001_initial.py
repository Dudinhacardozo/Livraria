# Generated by Django 5.1.1 on 2024-09-18 15:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Autor",
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Editora",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("site", models.URLField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("cidade", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
                "verbose_name_plural": "Usuários",
            },
        ),
        migrations.CreateModel(
            name="Compra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Carrinho"), (2, "Realizado"), (3, "Pago"), (4, "Entregue")], default=1
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="compras", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Livro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=255, verbose_name="Título")),
                ("isbn", models.CharField(blank=True, max_length=32, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "preco",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=7, null=True, verbose_name="Preço"
                    ),
                ),
                ("autores", models.ManyToManyField(blank=True, related_name="livros", to="core.autor")),
                (
                    "capa",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="core.categoria",
                    ),
                ),
                (
                    "editora",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="livros",
                        to="core.editora",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItensCompra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantidade", models.IntegerField(default=1)),
                (
                    "compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="itens", to="core.compra"
                    ),
                ),
                (
                    "livro",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.livro"),
                ),
            ],
        ),
    ]
