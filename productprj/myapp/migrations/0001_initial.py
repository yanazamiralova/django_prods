# Generated by Django 4.0.3 on 2024-01-12 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=10, verbose_name='Номер')),
                ('order_date', models.DateField(verbose_name='Дата заказа')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('cust', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.customers')),
                ('prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.products')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]