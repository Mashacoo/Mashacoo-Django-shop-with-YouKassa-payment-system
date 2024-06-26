# Generated by Django 4.2 on 2024-02-29 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profile_app.models.profile
import profile_app.models.seller


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('logo', models.ImageField(blank=True, upload_to=profile_app.models.seller.seller_images_directory_path, verbose_name='Logotype')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='phone number')),
                ('avatar', models.ImageField(blank=True, upload_to=profile_app.models.profile.profile_images_directory_path, verbose_name='profile avatar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
