# Generated by Django 4.1 on 2022-08-28 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_customer_user_alter_customer_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]