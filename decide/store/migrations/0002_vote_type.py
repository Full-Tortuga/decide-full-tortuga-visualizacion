# Generated by Django 2.2.5 on 2021-12-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='type',
            field=models.CharField(choices=[('V', 'Voting'), ('BV', 'BinaryVoting'), ('MV', 'MultipleVoting'), ('EV', 'EscaladeVoting')], default='V', max_length=2),
        ),
    ]
