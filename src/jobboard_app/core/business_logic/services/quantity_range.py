from src.jobboard_app.core.models import EmployeesQuantityRange


def get_quantity_range() -> list[tuple[str, str]]:
    quantities = [(quantity.name, quantity.name) for quantity in EmployeesQuantityRange.objects.all()]
    return quantities
