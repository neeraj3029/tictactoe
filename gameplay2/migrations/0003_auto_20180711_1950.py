# Generated by Django 2.0.5 on 2018-07-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay2', '0002_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('S', 'Second PLayer Move'), ('F', 'First PLayer Move'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
