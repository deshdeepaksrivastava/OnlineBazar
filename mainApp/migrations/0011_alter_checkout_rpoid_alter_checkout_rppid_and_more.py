# Generated by Django 4.0.4 on 2022-05-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_alter_newsletter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='rpoid',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='rppid',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='rpsid',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
