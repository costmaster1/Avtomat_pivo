# Generated by Django 4.0.6 on 2022-08-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vitrina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka_piva', models.CharField(max_length=150)),
                ('cena_piva', models.IntegerField()),
                ('kol_piva', models.IntegerField()),
                ('birka_piva', models.ImageField(upload_to='upload/')),
            ],
        ),
    ]
