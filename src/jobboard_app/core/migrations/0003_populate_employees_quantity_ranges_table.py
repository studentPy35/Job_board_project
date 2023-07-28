from typing import Any

from core.models import EmployeesQuantityRange
from django.db import migrations

DEFAULT_QUANTITY_RANGES = ("up to 50", "from 50 to 100", "from 101 to 500", "from 501 to 1000", "more than 1000")


def populate_quantity_table(apps: Any, schema_editor: Any) -> None:
    for quantity_range in DEFAULT_QUANTITY_RANGES:
        EmployeesQuantityRange.objects.create(name=quantity_range)


def reverse_table_population(apps: Any, schema_editor: Any) -> None:
    for quantity_range in DEFAULT_QUANTITY_RANGES:
        EmployeesQuantityRange.objects.get(name=quantity_range).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_populate_level_table"),
    ]

    operations = [
        migrations.RunPython(
            code=populate_quantity_table,
            reverse_code=reverse_table_population,
        )
    ]
