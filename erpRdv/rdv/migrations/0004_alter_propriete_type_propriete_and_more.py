# Generated by Django 4.0.3 on 2022-04-18 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0003_alter_typepropriete_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriete',
            name='type_propriete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_de_propriete', to='rdv.typepropriete'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='intervention',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_intervention', to='rdv.typeintervention'),
        ),
    ]