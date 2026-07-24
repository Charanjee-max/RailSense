from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.logger import logger

from app.exceptions.custom_exceptions import (
    BadRequestException,
    ConflictException,
    ForbiddenException,
    ResourceNotFoundException,
    UnauthorizedException,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(ResourceNotFoundException)
    async def resource_not_found_handler(
        request: Request,
        exc: ResourceNotFoundException,
    ):
        logger.warning(
            f"404 Not Found | {request.method} {request.url.path} | {exc.message}"
        )

        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": exc.message,
            },
        )

    @app.exception_handler(BadRequestException)
    async def bad_request_handler(
        request: Request,
        exc: BadRequestException,
    ):
        logger.warning(
            f"400 Bad Request | {request.method} {request.url.path} | {exc.message}"
        )

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": exc.message,
            },
        )

    @app.exception_handler(UnauthorizedException)
    async def unauthorized_handler(
        request: Request,
        exc: UnauthorizedException,
    ):
        logger.warning(
            f"401 Unauthorized | {request.method} {request.url.path} | {exc.message}"
        )

        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "message": exc.message,
            },
        )

    @app.exception_handler(ForbiddenException)
    async def forbidden_handler(
        request: Request,
        exc: ForbiddenException,
    ):
        logger.warning(
            f"403 Forbidden | {request.method} {request.url.path} | {exc.message}"
        )

        return JSONResponse(
            status_code=403,
            content={
                "success": False,
                "message": exc.message,
            },
        )

    @app.exception_handler(ConflictException)
    async def conflict_handler(
        request: Request,
        exc: ConflictException,
    ):
        logger.warning(
            f"409 Conflict | {request.method} {request.url.path} | {exc.message}"
        )

        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "message": exc.message,
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        logger.warning(
            f"422 Validation Error | {request.method} {request.url.path}"
        )

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "Validation failed.",
                "errors": exc.errors(),
            },
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(
            f"500 Internal Server Error | {request.method} {request.url.path}"
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error.",
            },
        )