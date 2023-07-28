from __future__ import annotations

from typing import TYPE_CHECKING

from django.forms import ValidationError

if TYPE_CHECKING:
    from django.core.files import File


class TagsValidator:
    def __init__(self, max_number: int) -> None:
        self.max_number = max_number

    def __call__(self, value: str) -> None:
        number = len(value.split("\r\n"))
        if number > self.max_number:
            raise ValidationError(message=f"Maximal number of tags is {self.max_number}")
        else:
            return None


class ValidateFileExtension:
    def __init__(self, available_extensions: list[str]) -> None:
        self.available_extensions = available_extensions

    def __call__(self, file: File) -> None:
        extension = file.name.split(".")[-1]
        if extension not in self.available_extensions:
            raise ValidationError(message="Unavailable file extension.")
        else:
            return None


class ValidateFileSize:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size

    def __call__(self, file: File) -> None:
        if file.size > self.max_size:
            raise ValidationError(message=f"Max size of file is {int(self.max_size / 1000000)} MB")
