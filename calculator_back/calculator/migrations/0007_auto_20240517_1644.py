# Generated by Django 3.0 on 2024-05-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_auto_20240517_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='breakfast',
            name='username',
            field=models.CharField(default='son_1', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='username',
            field=models.CharField(default='son_1', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='username',
            field=models.CharField(default='son_1', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='snack',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='snack',
            name='username',
            field=models.CharField(default='son_1', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sport',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sport',
            name='username',
            field=models.CharField(default='son_1', max_length=100, primary_key=True, serialize=False),
        ),
    ]
