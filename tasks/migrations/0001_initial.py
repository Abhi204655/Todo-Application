# Generated by Django 2.2.6 on 2019-12-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('completed', models.BooleanField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
