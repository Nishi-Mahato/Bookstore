# Generated by Django 3.0.3 on 2020-04-06 22:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField()),
                ('author_name', models.CharField(db_index=True, max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('cust_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_id', models.IntegerField()),
                ('publisher_name', models.CharField(db_index=True, max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ship_date', models.DateTimeField(auto_now_add=True)),
                ('ship_address', models.CharField(max_length=200)),
                ('ship_city', models.CharField(max_length=50)),
                ('ship_state', models.CharField(max_length=50)),
                ('ship_zipcode', models.CharField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('customerID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bookstore.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('New', 'New'), ('Like New', 'Like New'), ('Good', 'Good'), ('Acceptable', 'Acceptable')], default='New', max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('bookAuthorID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bookstore.Author')),
                ('bookPublisherID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bookstore.Publisher')),
            ],
        ),
    ]
