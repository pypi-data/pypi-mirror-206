# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import Callable
from typing import Generator

import iso3166
from pydantic.validators import str_validator


# Corrections for wrong names
COUNTRY_NAMES: dict[str, str] = {
    'NL': 'The Netherlands'
}


class ISO3166Base(str):
    length: int

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., str | None], None, None]:
        yield str_validator
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> str:
        if len(v) != cls.length:
            raise ValueError('Value is not an ISO 3166 code.')
        try:
            return cls(cls._get_country(v))
        except LookupError:
            raise ValueError(f"Invalid code: {v}")

    @classmethod
    def _get_country(cls, v: str) -> str:
        raise NotImplementedError


class ISO3166Alpha2(ISO3166Base):
    length: int = 2

    @property
    def name(self) -> str:
        if str(self) in COUNTRY_NAMES:
            return COUNTRY_NAMES[self]
        c = iso3166.countries_by_alpha2.get(self)
        if c is None:
            raise LookupError
        return c.name

    @classmethod
    def __modify_schema__(
        cls,
        field_schema: dict[str, Any]
    ) -> None:
        field_schema.update( # pragma: no cover
            title='Country code',
            description='An ISO 3166 alpha-2 country code.',
            type='string',
        )

    @classmethod
    def _get_country(cls, v: str) -> str:
        c = iso3166.countries_by_alpha2.get(v)
        if c is None:
            raise LookupError
        return c.alpha2