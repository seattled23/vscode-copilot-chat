from typing import Optional


class Hero:
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None

    def reject_none(cls, v):
        assert v is not None
        return v
