# Generated by Django 3.0.5 on 2020-05-01 05:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=200)),
                ('baby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='babies.Baby')),
            ],
        ),
    ]
