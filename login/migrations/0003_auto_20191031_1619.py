# Generated by Django 2.2.5 on 2019-10-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['c_time'], 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='province',
            field=models.CharField(choices=[('GuangDong', '广东')], default='GuangDong', max_length=64),
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.CharField(choices=[('science', '理科'), ('art', '文科')], default='science', max_length=64),
        ),
    ]
