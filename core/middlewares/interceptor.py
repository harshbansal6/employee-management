from requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        url = request.url.path
        method = request.method
        headers = dict(request.headers)
        body_bytes = b""

        # Read the request body in chunks to avoid blocking
        async for chunk in request.stream():
            body_bytes += chunk

        async def receive():
            return {"type": "http.request", "body": body_bytes}

        request._receive = receive
        response: Response = await call_next(request)
        return response