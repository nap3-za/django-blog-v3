# Generated by Django 2.2 on 2021-03-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ext_link1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ext_link2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ext_link3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ext_link4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ext_link5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('general', 'General'), ('technology', 'Technology'), ('celebrity', 'Celebrities'), ('computers', 'Computers'), ('educational', 'Educational'), ('travel', 'Travel'), ('kids', 'Kids'), ('gaming', 'Gaming'), ('diy', 'Diy')], default='general', max_length=100),
        ),
    ]
