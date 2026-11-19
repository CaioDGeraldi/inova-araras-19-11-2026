from django.db import migrations, models

from apps.core.models import new_account_code


def fill_account_codes(apps, schema_editor):
    User = apps.get_model("core", "User")
    for user in User.objects.all():
        user.account_code = new_account_code()
        user.save(update_fields=["account_code"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="account_code",
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.RunPython(fill_account_codes, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="user",
            name="account_code",
            field=models.CharField(default=new_account_code, max_length=32, unique=True),
        ),
    ]
