from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

from v1.config import settings


class AuthenticateUserMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Simulate extracting user_id from a JWT or session
        user_id = settings.superuser_id

        # Attach the user_id to the request state
        request.state.user_id = user_id

        # Continue processing the request
        response = await call_next(request)
        return response
