"""
advanced_features_and_security
--------------------------------

A modular package providing advanced feature implementations and
security mechanisms for modern Python applications.

This package includes:

- Authentication and authorization utilities
- Token and session management
- Encryption and secure data handling
- Permission-based feature gating
- Logging and monitoring integrations
- Helper modules for building secure modular architectures

Modules inside this package are organized to allow clean separation of
concerns while enabling easy import and flexible extension.
"""

# Package version
__version__ = "1.0.0"

# Import key exposed modules (adjust if your module names differ)
from .auth import AuthenticationManager, TokenService
from .security import EncryptionService, PermissionManager
from .features import FeatureToggle, FeatureRegistry
from .logging_utils import SecurityLogger

__all__ = [
    "AuthenticationManager",
    "TokenService",
    "EncryptionService",
    "PermissionManager",
    "FeatureToggle",
    "FeatureRegistry",
    "SecurityLogger",
]
