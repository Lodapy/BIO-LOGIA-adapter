"""Minimal public adapter for private client features.

This module is intentionally a thin integration shim. The real customer logic,
UI, schemas, session storage, and sensitive media remain in the private
repository behind authenticated access.
"""
from __future__ import annotations

import os
from typing import Any, Dict, Optional

import httpx


class ClientFeaturesUnavailable(RuntimeError):
    """Raised when the private service is not configured or unreachable."""


class ClientFeaturesClient:
    def __init__(self, base_url: Optional[str] = None, token: Optional[str] = None):
        self.base_url = (base_url or os.getenv("CLIENT_FEATURES_BASE_URL", "")).rstrip("/")
        self.token = token or os.getenv("CLIENT_FEATURES_TOKEN", "")
        if not self.base_url or not self.token:
            raise ClientFeaturesUnavailable(
                "CLIENT_FEATURES_BASE_URL and CLIENT_FEATURES_TOKEN are required"
            )

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Cache-Control": "no-store",
        }

    def submit(self, client_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        response = httpx.post(
            f"{self.base_url}/intake/submit",
            headers=self._headers(),
            json={"client_name": client_name, "payload": payload},
            timeout=30.0,
        )
        response.raise_for_status()
        return response.json()
