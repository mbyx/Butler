from dataclasses import dataclass
import arrow

@dataclass
class Plan:
    """An entry in the database."""
    name: str
    due_date: arrow.Arrow

    def __repr__(self) -> str:
        date, time = self.due_date.date(), self.due_date.time()
        return f'{self.name}: {date.day}/{date.month}/{date.year} {time.hour}:{time.minute}:{time.second}'