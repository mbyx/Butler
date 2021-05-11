from dataclasses import dataclass
from plan import Plan
import arrow

@dataclass
class Database:
    """The file that stores the plans."""
    path: str

    def write(self, plans: list[Plan]) -> bool:
        """Write a list of plans into the database. Overwrites existing plans."""
        with open(self.path, 'w') as database:
            database.writelines([f'{plan.name}\n{plan.due_date}\n' for plan in plans])

    def read(self) -> list[Plan]:
        """Read all plans currently stored in the database."""
        lst: list[Plan] = []
        with open(self.path, 'r') as database:
            lines = database.readlines()
            # Divide lines into chunks of 2.
            plans = [lines[x:x + 2] for x in range(0, len(lines), 2)]
            
            for name, due_date in plans:
                name, due_date = name.strip(), arrow.get(due_date.strip())
                lst.append(Plan(name, due_date))
            
        return lst