# Generated by Django 4.0.3 on 2022-03-21 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bailleur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True, verbose_name='Nom du bailleur')),
                ('prenom', models.CharField(max_length=100, null=True, verbose_name='prenom du bailleur')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='email du bailleur')),
                ('reference', models.CharField(max_length=100, null=True, verbose_name='référence du bailleur')),
            ],
        ),
        migrations.CreateModel(
            name='Locataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom du locataire')),
                ('prenom', models.CharField(max_length=100, verbose_name='prénom du locataire')),
                ('email', models.CharField(max_length=100, verbose_name='Email du locataire')),
                ('telephone', models.CharField(max_length=30, null=True, verbose_name='Telephone du locataire')),
            ],
        ),
        migrations.CreateModel(
            name='Propriete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface', models.CharField(max_length=100, null=True, verbose_name='Surface du bien')),
                ('numero', models.CharField(max_length=100, null=True, verbose_name='numéro de porte de la propriété')),
                ('numeroParking', models.CharField(max_length=100, null=True, verbose_name='Numéro de parking')),
                ('adresse', models.CharField(max_length=100, verbose_name='Adresse de la propriété')),
                ('codePostal', models.CharField(max_length=100, null=True, verbose_name='Code postal de la propriété')),
                ('ville', models.CharField(max_length=100, null=True, verbose_name='ville de la propriété')),
                ('adresseComplementaire', models.CharField(max_length=100, null=True, verbose_name='Adresse complémentaire de la propriété')),
                ('numeroCave', models.CharField(max_length=100, null=True, verbose_name='Numéro de cave de la propriété')),
                ('numeroSol', models.CharField(max_length=100, null=True, verbose_name='Numéro de sol')),
                ('bailleur', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bailleur', to='rdv.bailleur')),
                ('locataire', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locataire', to='rdv.locataire')),
            ],
        ),
        migrations.CreateModel(
            name='TypeIntervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name="Type d'intervention")),
                ('statut', models.IntegerField(verbose_name='Statut')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de modification')),
            ],
        ),
        migrations.CreateModel(
            name='TypePropriete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Type')),
                ('statut', models.IntegerField(verbose_name='statut du model')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de modification')),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_lot', models.CharField(max_length=100, null=True, verbose_name='ref lot')),
                ('ref_rdv_edl', models.CharField(max_length=100, null=True, verbose_name='reference rendez-vous EDL')),
                ('client', models.IntegerField(verbose_name='Client')),
                ('date', models.DateTimeField(null=True, verbose_name='Date et heure du RDV')),
                ('passeur', models.BigIntegerField(null=True, verbose_name='Passeur')),
                ('agent', models.IntegerField(verbose_name='Agent responsable du RDV')),
                ('longitude', models.CharField(max_length=100, null=True, verbose_name='longitude')),
                ('latitude', models.CharField(max_length=100, null=True, verbose_name='latitude')),
                ('intervention', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='type_intervention', to='rdv.typeintervention')),
                ('propriete', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='propriete', to='rdv.propriete')),
            ],
        ),
        migrations.CreateModel(
            name='RdvReporteDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancienneDate', models.DateTimeField(verbose_name='Ancienne date de RDV')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de mise à jour')),
                ('rdv', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Rendez_vous_date', to='rdv.rendezvous')),
            ],
        ),
        migrations.CreateModel(
            name='RdvReporteAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancien_agent', models.IntegerField(verbose_name='Ancien agent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de mise à jour')),
                ('rdv', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Rendez_vous_agent', to='rdv.rendezvous')),
            ],
        ),
        migrations.AddField(
            model_name='propriete',
            name='type_propriete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='type_de_propriete', to='rdv.typepropriete'),
        ),
    ]
