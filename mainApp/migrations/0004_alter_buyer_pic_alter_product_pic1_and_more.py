# Generated by Django 4.0.4 on 2022-04-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_product_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='pic',
            field=models.FileField(blank=True, default='defaultlogopic.png', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default='nopic.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default='nopic.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, default='nopic.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, default='nopic.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='pic',
            field=models.FileField(blank=True, default='defaultlogopic.png', null=True, upload_to='images'),
        ),
    ]