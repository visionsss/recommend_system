# Generated by Django 2.2.5 on 2019-10-29 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_remove_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('guangdong', '广东')], default='广东', max_length=32)),
                ('subject', models.CharField(choices=[('arts', '文科'), ('sciences', '理科')], default='理科', max_length=32)),
                ('score', models.IntegerField(max_length=32)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]
