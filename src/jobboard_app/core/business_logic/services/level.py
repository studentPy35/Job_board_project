from core.models import Level


def get_position_levels() -> list[tuple[str, str]]:
    levels = [(level.name, level.name) for level in Level.objects.all()]
    return levels
