class RailSenseException(Exception):
    """Base exception for all custom exceptions."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ResourceNotFoundException(RailSenseException):
    """Raised when a requested resource is not found."""
    pass


class BadRequestException(RailSenseException):
    """Raised for invalid requests."""
    pass


class UnauthorizedException(RailSenseException):
    """Raised when authentication fails."""
    pass


class ForbiddenException(RailSenseException):
    """Raised when the user does not have permission."""
    pass


class ConflictException(RailSenseException):
    """Raised when a resource already exists."""
    pass