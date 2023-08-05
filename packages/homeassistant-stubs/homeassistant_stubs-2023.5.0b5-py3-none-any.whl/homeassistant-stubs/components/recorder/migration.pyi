from . import Recorder as Recorder
from .auto_repairs.statistics.duplicates import delete_statistics_duplicates as delete_statistics_duplicates, delete_statistics_meta_duplicates as delete_statistics_meta_duplicates
from .const import SupportedDialect as SupportedDialect
from .db_schema import Base as Base, CONTEXT_ID_BIN_MAX_LENGTH as CONTEXT_ID_BIN_MAX_LENGTH, DOUBLE_PRECISION_TYPE_SQL as DOUBLE_PRECISION_TYPE_SQL, EventTypes as EventTypes, Events as Events, LEGACY_STATES_ENTITY_ID_LAST_UPDATED_INDEX as LEGACY_STATES_ENTITY_ID_LAST_UPDATED_INDEX, LEGACY_STATES_EVENT_ID_INDEX as LEGACY_STATES_EVENT_ID_INDEX, MYSQL_COLLATE as MYSQL_COLLATE, MYSQL_DEFAULT_CHARSET as MYSQL_DEFAULT_CHARSET, SCHEMA_VERSION as SCHEMA_VERSION, STATISTICS_TABLES as STATISTICS_TABLES, SchemaChanges as SchemaChanges, States as States, StatesMeta as StatesMeta, Statistics as Statistics, StatisticsMeta as StatisticsMeta, StatisticsRuns as StatisticsRuns, StatisticsShortTerm as StatisticsShortTerm, TABLE_STATES as TABLE_STATES
from .models import process_timestamp as process_timestamp
from .queries import batch_cleanup_entity_ids as batch_cleanup_entity_ids, find_entity_ids_to_migrate as find_entity_ids_to_migrate, find_event_type_to_migrate as find_event_type_to_migrate, find_events_context_ids_to_migrate as find_events_context_ids_to_migrate, find_states_context_ids_to_migrate as find_states_context_ids_to_migrate, has_used_states_event_ids as has_used_states_event_ids
from .statistics import get_start_time as get_start_time
from .tasks import CommitTask as CommitTask, PostSchemaMigrationTask as PostSchemaMigrationTask, StatisticsTimestampMigrationCleanupTask as StatisticsTimestampMigrationCleanupTask
from .util import database_job_retry_wrapper as database_job_retry_wrapper, get_index_by_name as get_index_by_name, retryable_database_job as retryable_database_job, session_scope as session_scope
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from homeassistant.util.ulid import ulid_at_time as ulid_at_time, ulid_to_bytes as ulid_to_bytes
from sqlalchemy.engine import CursorResult as CursorResult, Engine as Engine
from sqlalchemy.orm.session import Session as Session

LIVE_MIGRATION_MIN_SCHEMA_VERSION: int
_EMPTY_ENTITY_ID: str
_EMPTY_EVENT_TYPE: str
_LOGGER: Incomplete

class _ColumnTypesForDialect:
    big_int_type: str
    timestamp_type: str
    context_bin_type: str
    def __init__(self, big_int_type, timestamp_type, context_bin_type) -> None: ...

_MYSQL_COLUMN_TYPES: Incomplete
_POSTGRESQL_COLUMN_TYPES: Incomplete
_SQLITE_COLUMN_TYPES: Incomplete
_COLUMN_TYPES_FOR_DIALECT: dict[SupportedDialect | None, _ColumnTypesForDialect]

def raise_if_exception_missing_str(ex: Exception, match_substrs: Iterable[str]) -> None: ...
def _get_schema_version(session: Session) -> int | None: ...
def get_schema_version(session_maker: Callable[[], Session]) -> int | None: ...

class SchemaValidationStatus:
    current_version: int
    schema_errors: set[str]
    valid: bool
    def __init__(self, current_version, schema_errors, valid) -> None: ...

def _schema_is_current(current_version: int) -> bool: ...
def validate_db_schema(hass: HomeAssistant, instance: Recorder, session_maker: Callable[[], Session]) -> SchemaValidationStatus | None: ...
def _find_schema_errors(hass: HomeAssistant, instance: Recorder, session_maker: Callable[[], Session]) -> set[str]: ...
def live_migration(schema_status: SchemaValidationStatus) -> bool: ...
def migrate_schema(instance: Recorder, hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], schema_status: SchemaValidationStatus) -> None: ...
def _create_index(session_maker: Callable[[], Session], table_name: str, index_name: str) -> None: ...
def _execute_or_collect_error(session_maker: Callable[[], Session], query: str, errors: list[str]) -> bool: ...
def _drop_index(session_maker: Callable[[], Session], table_name: str, index_name: str, quiet: bool | None = ...) -> None: ...
def _add_columns(session_maker: Callable[[], Session], table_name: str, columns_def: list[str]) -> None: ...
def _modify_columns(session_maker: Callable[[], Session], engine: Engine, table_name: str, columns_def: list[str]) -> None: ...
def _update_states_table_with_foreign_key_options(session_maker: Callable[[], Session], engine: Engine) -> None: ...
def _drop_foreign_key_constraints(session_maker: Callable[[], Session], engine: Engine, table: str, columns: list[str]) -> None: ...
def _apply_update(instance: Recorder, hass: HomeAssistant, engine: Engine, session_maker: Callable[[], Session], new_version: int, old_version: int) -> None: ...
def _correct_table_character_set_and_collation(table: str, session_maker: Callable[[], Session]) -> None: ...
def post_schema_migration(instance: Recorder, old_version: int, new_version: int) -> None: ...
def _wipe_old_string_statistics_columns(instance: Recorder) -> None: ...
def _wipe_old_string_time_columns(instance: Recorder, engine: Engine, session: Session) -> None: ...
def _migrate_columns_to_timestamp(instance: Recorder, session_maker: Callable[[], Session], engine: Engine) -> None: ...
def _migrate_statistics_columns_to_timestamp(instance: Recorder, session_maker: Callable[[], Session], engine: Engine) -> None: ...
def _context_id_to_bytes(context_id: str | None) -> bytes | None: ...
def _generate_ulid_bytes_at_time(timestamp: float | None) -> bytes: ...
def migrate_states_context_ids(instance: Recorder) -> bool: ...
def migrate_events_context_ids(instance: Recorder) -> bool: ...
def migrate_event_type_ids(instance: Recorder) -> bool: ...
def migrate_entity_ids(instance: Recorder) -> bool: ...
def post_migrate_entity_ids(instance: Recorder) -> bool: ...
def cleanup_legacy_states_event_ids(instance: Recorder) -> bool: ...
def _initialize_database(session: Session) -> bool: ...
def initialize_database(session_maker: Callable[[], Session]) -> bool: ...
