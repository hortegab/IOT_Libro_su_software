# Generated by Django 2.2.1 on 2019-07-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prueba', '0004_departamentos_produccion_municipios'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='album/imagenes')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'AlbumImagenes',
                'verbose_name_plural': 'AlbumImageness',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
