# Generated by Django 3.2.23 on 2023-11-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0002_auto_20231120_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='brand',
            field=models.CharField(choices=[('Acer', 'Acer'), ('Apple', 'Apple'), ('Asus', 'Asus'), ('BenQ', 'BenQ'), ('BlackBerry', 'BlackBerry'), ('Dell', 'Dell'), ('Google', 'Google'), ('Honor', 'Honor'), ('HP', 'HP'), ('HTC', 'HTC'), ('Huawei', 'Huawei'), ('Lenovo', 'Lenovo'), ('LG', 'LG'), ('Microsoft', 'Microsoft'), ('Motorola', 'Motorola'), ('Nokia', 'Nokia'), ('Nvidia', 'Nvidia'), ('OnePlus', 'OnePlus'), ('Oppo', 'Oppo'), ('Panasonic', 'Panasonic'), ('Philips', 'Philips'), ('Samsung', 'Samsung'), ('Sony', 'Sony'), ('Sony Ericsson', 'Sony Ericsson'), ('Toshiba', 'Toshiba'), ('vivo', 'vivo'), ('Xiaomi', 'Xiaomi'), ('ZTE', 'ZTE')], max_length=20),
        ),
    ]
