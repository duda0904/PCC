# Generated by Django 4.0.3 on 2023-02-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_alter_animal_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
