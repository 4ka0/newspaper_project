# Generated by Django 3.0.8 on 2020-08-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200819_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(default='../media/images/suzaku.jpg', upload_to='images/'),
        ),
    ]