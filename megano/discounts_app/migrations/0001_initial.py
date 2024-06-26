# Generated by Django 4.2 on 2024-02-29 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('type_of_discount', models.CharField(choices=[('per', 'Per cent'), ('fa', 'Fixed amount'), ('fp', 'Fixed price')], default='per', max_length=3, verbose_name='type')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='amount')),
                ('final_sum_min', models.PositiveIntegerField(null=True, verbose_name='final_sum_min')),
                ('final_sum_max', models.PositiveIntegerField(blank=True, default=1000000, verbose_name='final_sum_max')),
                ('products_quantity', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='product_quantity')),
            ],
            options={
                'verbose_name': 'cart discount',
                'verbose_name_plural': 'cart discounts',
            },
        ),
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('group_1', models.ManyToManyField(related_name='group_1', to='catalog.product')),
                ('group_2', models.ManyToManyField(related_name='group_2', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
            },
        ),
        migrations.CreateModel(
            name='SetDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('type_of_discount', models.CharField(choices=[('per', 'Per cent'), ('fa', 'Fixed amount'), ('fp', 'Fixed price')], default='per', max_length=3, verbose_name='type')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='amount')),
                ('product_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_discounts', to='discounts_app.productset')),
            ],
            options={
                'verbose_name': 'set discount',
                'verbose_name_plural': 'set discounts',
            },
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('type_of_discount', models.CharField(choices=[('per', 'Per cent'), ('fa', 'Fixed amount'), ('fp', 'Fixed price')], default='per', max_length=3, verbose_name='type')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='amount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_discounts', to='catalog.product')),
                ('seller', models.ManyToManyField(related_name='product_discounts', to='profile_app.seller')),
            ],
            options={
                'verbose_name': 'product discount',
                'verbose_name_plural': 'product discounts',
            },
        ),
    ]
