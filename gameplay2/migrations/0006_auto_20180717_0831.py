# Generated by Django 2.0.5 on 2018-07-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay2', '0005_auto_20180715_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='move',
            old_name='move',
            new_name='game',
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('S', 'Second PLayer Move'), ('D', 'Draw'), ('F', 'First PLayer Move')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(editable=False),
        ),
    ]