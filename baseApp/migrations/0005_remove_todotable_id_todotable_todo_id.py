# Generated by Django 4.1.6 on 2023-02-14 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0004_remove_todotable_todo_id_todotable_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todotable',
            name='id',
        ),
        migrations.AddField(
            model_name='todotable',
            name='todo_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
