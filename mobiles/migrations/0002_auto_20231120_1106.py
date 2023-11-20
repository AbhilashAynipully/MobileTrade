# Generated by Django 3.2.23 on 2023-11-20 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='mobile_pic1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[740, 740], upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='mobile_pic2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[740, 740], upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='mobile_pic3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[740, 740], upload_to='mobiles/'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='mobile_pic4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[740, 740], upload_to='mobiles/'),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobiles.mobile')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]