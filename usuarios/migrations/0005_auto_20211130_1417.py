# Generated by Django 3.2.9 on 2021-11-30 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20211130_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_modificacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Confiabilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_modificacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=10000, null=True)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_modificacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(null=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.area')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_modificacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(null=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.area')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=10000, null=True)),
                ('num_buena_calificacion', models.IntegerField(null=True)),
                ('num_mala_calificacion', models.IntegerField(null=True)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_modificacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(null=True)),
                ('confiabilidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.confiabilidad')),
                ('pregunta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.pregunta')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.tema'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=10000, null=True)),
                ('comentario_id', models.IntegerField(null=True)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_modificacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(null=True)),
                ('confiabilidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.confiabilidad')),
                ('respuesta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.respuesta')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_modificacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.BooleanField(null=True)),
                ('respuesta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.respuesta')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
