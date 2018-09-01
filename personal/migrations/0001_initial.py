# Generated by Django 2.0.7 on 2018-08-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='node1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value1V', models.CharField(max_length=50)),
                ('value1I', models.CharField(max_length=50)),
                ('value1P', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='node2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value2V', models.CharField(max_length=50)),
                ('value2I', models.CharField(max_length=50)),
                ('value2P', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='node3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value3V', models.CharField(max_length=50)),
                ('value3I', models.CharField(max_length=50)),
                ('value3P', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuesV', models.CharField(max_length=50)),
                ('valuesI', models.CharField(max_length=50)),
                ('valuesP', models.CharField(max_length=50)),
            ],
        ),
    ]