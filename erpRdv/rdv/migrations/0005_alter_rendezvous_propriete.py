# Generated by Django 4.0.3 on 2022-04-18 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0004_alter_propriete_type_propriete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='propriete',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propriete', to='rdv.propriete'),
        ),
    ]