# Generated by Django 4.2 on 2024-02-29 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'new'), (2, 'paid'), (3, 'not_paid'), (4, 'pending')], default=1, verbose_name='status')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, verbose_name='quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='cart_app.cart', verbose_name='cart')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]