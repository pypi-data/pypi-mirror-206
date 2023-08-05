#
# Copyright 2023 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING, Union

from trafaret import DataError

from .errors import ClientError

if TYPE_CHECKING:
    from .models.use_cases.use_case import UseCase

DefaultUseCase = Optional[Union["UseCase", str]]


@dataclass
class Context:
    """
    Interface for initializing, accessing, and setting variables that should persist.
    """

    _use_case: DefaultUseCase = field(init=False, default=None)

    @property
    def use_case(self) -> DefaultUseCase:
        """Returns the default Use Case. If a string representing the Use Case ID
        was provided, lookup, cache, and return the actual entity."""
        if isinstance(self._use_case, str):
            try:
                from .models.use_cases.use_case import (  # pylint: disable=import-outside-toplevel
                    UseCase,
                )

                self._use_case = UseCase.get(use_case_id=self._use_case)
            except (DataError, ClientError) as e:
                raise ValueError("Current use case is invalid.", e)
        return self._use_case or None

    @use_case.setter
    def use_case(self, value: DefaultUseCase = None) -> None:
        self._use_case = value


_context: ContextVar[Context] = ContextVar("current_context", default=Context())
