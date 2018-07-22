# Generated by Django 2.0.5 on 2018-07-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay2', '0010_auto_20180717_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('S', 'Second PLayer Move'), ('F', 'First PLayer Move'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]