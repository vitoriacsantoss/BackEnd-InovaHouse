# Generated by Django 5.0.6 on 2024-09-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_agendamento_imoveis_comodidade_imoveis"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="imoveis",
            name="foto",
        ),
        migrations.AddField(
            model_name="imoveis",
            name="foto",
            field=models.ManyToManyField(blank=True, default=None, null=True, to="uploader.image"),
        ),
    ]
