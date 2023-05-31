# Generated by Django 4.1 on 2023-05-31 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0017_remove_userinfo_id_userinfo_reg_no_userinfo_room_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='reg_no',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='room_no',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
