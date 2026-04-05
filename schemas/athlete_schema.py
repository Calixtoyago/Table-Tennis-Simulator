from pydantic import BaseModel, field_validator

class Athlete(BaseModel):
    name: str
    attack: int
    defense: int
    serve: int

    @field_validator("attack", "defense", "serve")
    @classmethod
    def validate_stats(cls, value):
        if not 0 <= value <= 20:
            raise ValueError("Invalid attributes")
        return value