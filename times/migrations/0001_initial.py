# Generated by Django 3.0.4 on 2020-05-10 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('to_do_submit', models.TimeField(blank=True, null=True)),
                ('arrive_submit', models.TimeField(blank=True, null=True)),
                ('feedback_submit', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Time',
            },
        ),
    ]
