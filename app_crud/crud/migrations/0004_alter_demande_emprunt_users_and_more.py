# Generated by Django 4.2.1 on 2023-05-05 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_rename_preuv_remb_empr_preuvrembempr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande_emprunt',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.users'),
        ),
        migrations.AlterField(
            model_name='preuv_cotis_sinistre',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.users'),
        ),
        migrations.AlterField(
            model_name='preuv_cotisation',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.users'),
        ),
        migrations.AlterField(
            model_name='preuvrembempr',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.users'),
        ),
    ]
