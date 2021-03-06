# Generated by Django 3.0.2 on 2020-02-19 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_todo_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tcomments', to='first.Todo')),
            ],
        ),
    ]
