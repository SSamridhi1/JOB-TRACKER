"""
Shared pytest fixtures.

Why this file exists:
    conftest.py is pytest's convention for fixtures shared across multiple
    test files. Having ONE test client fixture here (instead of every test
    file rebuilding its own) keeps tests consistent and DRY.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """A TestClient for making requests against the app without a real server."""
    return TestClient(app)
