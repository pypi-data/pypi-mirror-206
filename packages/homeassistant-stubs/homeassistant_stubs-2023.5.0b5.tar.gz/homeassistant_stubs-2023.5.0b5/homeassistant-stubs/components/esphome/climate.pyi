from . import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import ClimateAction, ClimateFanMode, ClimateInfo, ClimateMode, ClimatePreset, ClimateState, ClimateSwingMode
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_DIFFUSE as FAN_DIFFUSE, FAN_FOCUS as FAN_FOCUS, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_MIDDLE as FAN_MIDDLE, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_ACTIVITY as PRESET_ACTIVITY, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_HOME as PRESET_HOME, PRESET_NONE as PRESET_NONE, PRESET_SLEEP as PRESET_SLEEP, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

FAN_QUIET: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_CLIMATE_MODES: EsphomeEnumMapper[ClimateMode, HVACMode]
_CLIMATE_ACTIONS: EsphomeEnumMapper[ClimateAction, HVACAction]
_FAN_MODES: EsphomeEnumMapper[ClimateFanMode, str]
_SWING_MODES: EsphomeEnumMapper[ClimateSwingMode, str]
_PRESETS: EsphomeEnumMapper[ClimatePreset, str]

class EsphomeClimateEntity(EsphomeEntity[ClimateInfo, ClimateState], ClimateEntity):
    _attr_temperature_unit: Incomplete
    @property
    def precision(self) -> float: ...
    @property
    def hvac_modes(self) -> list[str]: ...
    @property
    def fan_modes(self) -> list[str]: ...
    @property
    def preset_modes(self) -> list[str]: ...
    @property
    def swing_modes(self) -> list[str]: ...
    @property
    def target_temperature_step(self) -> float: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    @property
    def supported_features(self) -> ClimateEntityFeature: ...
    @property
    def hvac_mode(self) -> str | None: ...
    @property
    def hvac_action(self) -> str | None: ...
    @property
    def fan_mode(self) -> str | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def swing_mode(self) -> str | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def target_temperature_low(self) -> float | None: ...
    @property
    def target_temperature_high(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
