# Generated by Django 2.2 on 2019-06-09 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190609_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]