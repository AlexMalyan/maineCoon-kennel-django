# Generated by Django 5.0 on 2023-12-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cattery', models.CharField(max_length=255)),
                ('merits', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Кот'), ('F', 'Кошка')], max_length=1)),
                ('bitrh', models.DateField()),
                ('description', models.TextField()),
                ('mating', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
