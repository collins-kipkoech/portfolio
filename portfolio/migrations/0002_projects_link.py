# Generated by Django 3.1.4 on 2021-01-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.CharField(default=True, max_length=500),
            preserve_default=False,
        ),
    ]