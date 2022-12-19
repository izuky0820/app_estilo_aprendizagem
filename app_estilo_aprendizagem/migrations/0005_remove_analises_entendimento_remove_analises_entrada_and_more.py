# Generated by Django 4.1.2 on 2022-12-19 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_estilo_aprendizagem', '0004_alter_formulario_date_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analises',
            name='entendimento',
        ),
        migrations.RemoveField(
            model_name='analises',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='analises',
            name='percepcao',
        ),
        migrations.RemoveField(
            model_name='analises',
            name='processamento',
        ),
        migrations.AddField(
            model_name='analises',
            name='analise_entendimento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='analise_entrada',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='analise_percepcao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='analise_processamento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='dimensao_entendimento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='dimensao_entrada',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='dimensao_percepcao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='dimensao_processamento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='reflexao_entendimento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='reflexao_entrada',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='reflexao_percepcao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='reflexao_processamento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='analises',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_estilo_aprendizagem.turma'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não Binário'), ('O', 'Outro')], max_length=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_pessoa',
            field=models.CharField(choices=[('N', 'Núcleo de Apoio ao Educando'), ('E', 'Estudante'), ('D', 'Docente'), ('S', 'Secretario')], max_length=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_estilo_aprendizagem.turma'),
        ),
    ]