# Generated by Django 2.2 on 2021-03-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', max_length=100),
        ),
    ]
