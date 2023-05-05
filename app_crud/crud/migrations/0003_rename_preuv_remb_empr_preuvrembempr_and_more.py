# Generated by Django 4.2.1 on 2023-05-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_demande_emprunt_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preuv_Remb_Empr',
            new_name='PreuvRembEmpr',
        ),
        migrations.AlterField(
            model_name='users',
            name='e_mail',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='statut',
            field=models.CharField(choices=[('TRESORIER', 'TRESORIER'), ('SECRETAIRE', 'SECRETAIRE'), ('ASSISTANT TRESORIER', 'ASSISTANT TRESORIER'), ('REPORTEUR', 'REPORTEUR')], max_length=30),
        ),
    ]
