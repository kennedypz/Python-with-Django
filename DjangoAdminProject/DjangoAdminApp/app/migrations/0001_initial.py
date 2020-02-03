# Generated by Django 3.0.2 on 2020-01-27 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('Ruim', 'ruim'), ('Ótimo', 'ótimo'), ('Bom', 'bom')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_nascimento', models.DateTimeField(verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=20)),
                ('profissao', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=20)),
                ('placa', models.CharField(max_length=8)),
                ('cor', models.CharField(choices=[('Branco', 'branco'), ('Azul', 'azul'), ('Preto', 'preto'), ('Amarelo', 'amarelo'), ('Vermelho', 'vermelho'), ('Prata', 'prata')], max_length=20)),
                ('ano', models.CharField(max_length=4)),
                ('preco', models.FloatField()),
                ('foto_capa', models.ImageField(upload_to='images')),
                ('tipo', models.CharField(choices=[('Carro', 'carro'), ('Moto', 'moto')], max_length=10)),
                ('acessorios', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Acessorio')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Proprietario')),
            ],
        ),
    ]