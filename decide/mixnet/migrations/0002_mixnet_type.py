# Generated by Django 2.2.5 on 2022-01-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixnet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mixnet',
            name='type',
            field=models.CharField(choices=[('V', 'Voting'), ('BV', 'BinaryVoting'), ('MV', 'MultipleVoting'), ('SV', 'ScoreVoting')], default='V', max_length=2),
        ),
    ]
