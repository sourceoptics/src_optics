# Generated by Django 2.2.2 on 2019-07-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source_optics', '0002_auto_20190717_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='force_next_pull',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='logincredential',
            name='ssh_private_key',
            field=models.TextField(blank=True, null=True),
        ),
    ]
