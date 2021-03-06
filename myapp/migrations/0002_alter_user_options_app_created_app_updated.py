# Generated by Django 4.0.3 on 2022-03-15 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='app',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
