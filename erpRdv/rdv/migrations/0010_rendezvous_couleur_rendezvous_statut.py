# Generated by Django 4.1.1 on 2022-09-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0009_propriete_type_rendezvous_consignes_particuliere_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='couleur',
            field=models.CharField(default='red', max_length=30, verbose_name='couleur du RDV'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='statut',
            field=models.CharField(default='Attente prise en charge', max_length=30, verbose_name='Statut du RDV'),
        ),
    ]
