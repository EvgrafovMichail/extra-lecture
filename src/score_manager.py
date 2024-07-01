"""
Объекты для расчета продуктовых метрик.
"""


from queue import PriorityQueue
from typing import Sequence


class ScoreManager:
    """
    Объект для расчета количества уникальных пользователей за указанный период.
    """

    _heap: PriorityQueue
    _record_time_mapping: dict[int, int]
    _timer: int
    _accumulation_period: int

    def __init__(self, accumulation_period: int) -> None:
        """
        Инициализирует менеджер продуктовой метрики.

        Args:
            accumulation_period: целое число - период накопления - период времени,
                за который осуществляется учет количества уникальных пользователей.

        Return:
            None.

        Raises:
            ValueError возбуждается, если переданное значение accumulation_period не
                может быть представлено в виде натурального числа (целое число, более нуля).
        """
        # ВАШ КОД
        pass

    def add_records(self, records: Sequence[int]) -> None:
        """
        Добавляет записи о пользователях, посетивших приложение в текущей день.

        Перед добавлением новых записей удаляет информацию о записях, потерявших
        актуальность.
        После добавления новых записей текущей день считается завершенным, счетчик
        времени инкреминируется.

        Args:
            records: последовательность целых чисел - идентефикаторы пользователей,
                посетивших приложение в данный день.
        
        Return:
            None.
        """
        # ВАШ КОД
        pass

    @property
    def score(self) -> int:
        """
        Значение метрики за период времени accumulation_period.
        """
        # ВАШ КОД
        return 0 # этот код можно менять

    def _delete_outdated_records(self) -> None:
        """
        Удаляет устаревшие записи.
        """
        # ВАШ КОД
        pass
