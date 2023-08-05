from ..core import Recorder as Recorder
from ..db_schema import StatisticsMeta as StatisticsMeta
from ..models import StatisticMetaData as StatisticMetaData
from ..util import execute_stmt_lambda_element as execute_stmt_lambda_element
from _typeshed import Incomplete
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from typing import Literal

CACHE_SIZE: int
_LOGGER: Incomplete
QUERY_STATISTIC_META: Incomplete

def _generate_get_metadata_stmt(statistic_ids: set[str] | None = ..., statistic_type: Literal['mean'] | Literal['sum'] | None = ..., statistic_source: str | None = ...) -> StatementLambdaElement: ...
def _statistics_meta_to_id_statistics_metadata(meta: StatisticsMeta) -> tuple[int, StatisticMetaData]: ...

class StatisticsMetaManager:
    recorder: Incomplete
    _stat_id_to_id_meta: Incomplete
    def __init__(self, recorder: Recorder) -> None: ...
    def _clear_cache(self, statistic_ids: list[str]) -> None: ...
    def _get_from_database(self, session: Session, statistic_ids: set[str] | None = ..., statistic_type: Literal['mean'] | Literal['sum'] | None = ..., statistic_source: str | None = ...) -> dict[str, tuple[int, StatisticMetaData]]: ...
    def _assert_in_recorder_thread(self) -> None: ...
    def _add_metadata(self, session: Session, statistic_id: str, new_metadata: StatisticMetaData) -> int: ...
    def _update_metadata(self, session: Session, statistic_id: str, new_metadata: StatisticMetaData, old_metadata_dict: dict[str, tuple[int, StatisticMetaData]]) -> tuple[str | None, int]: ...
    def load(self, session: Session) -> None: ...
    def get(self, session: Session, statistic_id: str) -> tuple[int, StatisticMetaData] | None: ...
    def get_many(self, session: Session, statistic_ids: set[str] | None = ..., statistic_type: Literal['mean'] | Literal['sum'] | None = ..., statistic_source: str | None = ...) -> dict[str, tuple[int, StatisticMetaData]]: ...
    def get_from_cache_threadsafe(self, statistic_ids: set[str]) -> dict[str, tuple[int, StatisticMetaData]]: ...
    def update_or_add(self, session: Session, new_metadata: StatisticMetaData, old_metadata_dict: dict[str, tuple[int, StatisticMetaData]]) -> tuple[str | None, int]: ...
    def update_unit_of_measurement(self, session: Session, statistic_id: str, new_unit: str | None) -> None: ...
    def update_statistic_id(self, session: Session, source: str, old_statistic_id: str, new_statistic_id: str) -> None: ...
    def delete(self, session: Session, statistic_ids: list[str]) -> None: ...
    def reset(self) -> None: ...
    def adjust_lru_size(self, new_size: int) -> None: ...
