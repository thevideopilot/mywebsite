# Generated by Django 3.0.4 on 2020-04-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='hobbies',
            field=models.TextField(default='python'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='skills',
            field=models.TextField(default='python'),
            preserve_default=False,
        ),
    ]
