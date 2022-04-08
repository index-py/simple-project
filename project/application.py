from hintapi import HintAPI

from .conf import settings
from .apis import routes

app = HintAPI(
    debug=settings.debug,
    routes=routes,
)
