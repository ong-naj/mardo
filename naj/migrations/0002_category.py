# Generated by Django 4.0.4 on 2023-01-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]
