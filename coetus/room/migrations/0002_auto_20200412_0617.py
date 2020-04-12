# Generated by Django 2.2.9 on 2020-04-12 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='files',
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='room.room')),
            ],
        ),
    ]
