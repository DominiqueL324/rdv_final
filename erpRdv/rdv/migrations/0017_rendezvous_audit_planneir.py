# Generated by Django 4.1.1 on 2022-10-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0016_alter_propriete_adresse_alter_rendezvous_couleur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='audit_planneir',
            field=models.IntegerField(null=True, verbose_name='Audit planneur'),
        ),
    ]