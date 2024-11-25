# Generated by Django 4.2.11 on 2024-11-25 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='CARRIER_NAME')),
            ],
            options={
                'verbose_name': 'carrier',
                'verbose_name_plural': 'carriers',
                'db_table': 'carrier',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='CATEGORY_NAME', max_length=45)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Создан'), (2, 'В пути'), (3, 'Доставлен')], default=1)),
                ('address', models.TextField(default='USER_ADDRESS')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price_at_order', models.FloatField(default=0.0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='base.order')),
            ],
            options={
                'verbose_name': 'order details',
                'verbose_name_plural': 'order details',
                'db_table': 'order_details',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='PRODUCT_NAME', max_length=45)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('weight', models.FloatField(default=0.0)),
                ('width', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('length', models.FloatField(default=0.0)),
                ('image_ref', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='base.category')),
                ('orders', models.ManyToManyField(related_name='products', through='base.OrderDetails', to='base.order')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='WAREHOUSE_NAME', max_length=45)),
                ('location', models.TextField(default='WAREHOUSE_LOCATION')),
                ('capacity', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'warehouse',
                'verbose_name_plural': 'warehouses',
                'db_table': 'warehouse',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='base.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='base.warehouse')),
            ],
            options={
                'verbose_name': 'stock',
                'verbose_name_plural': 'stocks',
                'db_table': 'stock',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='warehouses',
            field=models.ManyToManyField(related_name='products', through='base.Stock', to='base.warehouse'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='base.product'),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='shipment', serialize=False, to='base.order')),
                ('tracking_number', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'В пути'), (2, 'Доставлен')], default=1)),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='base.carrier')),
            ],
            options={
                'verbose_name': 'shipment',
                'verbose_name_plural': 'shipments',
                'db_table': 'shipment',
            },
        ),
    ]
