from django.db import migrations

def forwards(apps, schema_editor):
    PizzaModel = apps.get_model('demo', 'Pizza')
    PizzaModel.objects.create(**{
        'name': 'Margherita',
        'description': 'Single cheese topping',
        'cost': 9.99,
        })

class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(forwards),
    ]
