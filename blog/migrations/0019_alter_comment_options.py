# Generated by Django 3.2.5 on 2021-08-05 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20210805_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت\u200cها'},
        ),
    ]
