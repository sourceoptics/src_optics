# Generated by Django 2.0.10 on 2019-02-11 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=64, null=True)),
                ('username', models.TextField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.TextField(max_length=256)),
                ('commit_date', models.TextField(max_length=64, null=True)),
                ('author_date', models.TextField(max_length=64, null=True)),
                ('lines_added', models.IntegerField(default=0)),
                ('lines_removed', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='srcOptics.Author')),
            ],
        ),
        migrations.CreateModel(
            name='LoginCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=32)),
                ('password', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32)),
                ('admins', models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=256)),
                ('name', models.TextField(max_length=32)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orgs', to='srcOptics.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='logincredential',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srcOptics.Repository'),
        ),
        migrations.AddField(
            model_name='commit',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repos', to='srcOptics.Repository'),
        ),
    ]
