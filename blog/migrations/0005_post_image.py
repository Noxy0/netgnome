# Generated by Django 4.1 on 2023-02-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_copmment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image', upload_to='images'),
        ),
    ]