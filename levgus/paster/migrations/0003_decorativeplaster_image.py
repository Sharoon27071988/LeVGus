# Generated by Django 5.0.4 on 2024-04-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paster', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='decorativeplaster',
            name='image',
            field=models.ImageField(default=1, upload_to='decorativeplaster/', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]