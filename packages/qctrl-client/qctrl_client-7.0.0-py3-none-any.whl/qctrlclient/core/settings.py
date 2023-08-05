# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from dataclasses import dataclass
from functools import cached_property
from typing import (
    Callable,
    Optional,
    Union,
)

from .products import Product
from .router.base import BaseRouter


@dataclass
class CoreClientSettings:
    """Settings class for core clients.

    Parameters
    ----------
    router : Union[BaseRouter, Callable]
        The router to be used in the core client. Can be either
        an instance of `BaseRouter` or a callable which accepts
        no arguments and returns an instance of `BaseRouter`.
    product: Optional[Product]
        Information about the product that the client provides
        access to. Required for any remote execution of workflows
        (e.g. `ApiRouter`).
    organization : Optional[str]
        The organization that a core workflow should run as.
        Required for any remove execution of workflows (e.g.
        `ApiRouter`).
    """

    router: Union[BaseRouter, Callable]
    product: Optional[Product] = None
    organization: Optional[str] = None

    def update(self, **kwargs):
        """Updates settings fields."""

        for attr, value in kwargs.items():
            if not hasattr(self, attr):
                raise AttributeError(f"Invalid field: {attr}")

            setattr(self, attr, value)

        # clear any cached router as config changes could
        # alter it
        self._clear_cached_router()

    def _clear_cached_router(self):
        """Clears the cached router."""
        try:
            delattr(self, "_router")
        except AttributeError:
            pass

    @cached_property
    def _router(self) -> BaseRouter:
        """Prepares the router to be used by the core client."""

        router = self.router

        if isinstance(router, BaseRouter):
            pass

        elif callable(router):
            router = router()

        if not isinstance(router, BaseRouter):
            raise ValueError(f"Invalid router: {router}")

        return router

    def get_router(self) -> BaseRouter:
        """Returns the configured router to be used by the client."""
        return self._router
