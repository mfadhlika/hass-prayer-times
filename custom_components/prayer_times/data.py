"""Custom types for prayer_times."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import PrayertimesApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type PrayertimesConfigEntry = ConfigEntry[PrayertimesData]


@dataclass
class PrayertimesData:
    """Data for the Blueprint integration."""

    client: PrayertimesApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
