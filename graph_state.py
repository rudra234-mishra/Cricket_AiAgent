from typing import TypedDict,Annotated
from pydantic import BaseModel,Field


class odi(TypedDict):
    matches:Annotated[int,Field(description="total matches in odi",ge=1)]
    runs:Annotated[int,Field(description="total runs in odi",ge=1)]
    hundreds:Annotated[int,Field(description="total hundreds in odi",ge=1)]
    fifties:Annotated[int,Field(description="total fifties in odi",ge=1)]
    fours:Annotated[int,Field(description="total fours in odi",ge=1)]
    sixes:Annotated[int,Field(description="total sixes in odi",ge=1)]
    highest_score:Annotated[int,Field(description="Highest Score In Odi",ge=1)]

class t20(TypedDict):
    matches:Annotated[int,Field(description="total matches in t20",ge=1)]
    runs:Annotated[int,Field(description="total runs in t20",ge=1)]
    hundreds:Annotated[int,Field(description="total hundreds in t20",ge=0)]
    fifties:Annotated[int,Field(description="total fifties in t20",ge=0)]
    fours:Annotated[int,Field(description="total fours in t20",ge=1)]
    sixes:Annotated[int,Field(description="total sixes in t20",ge=1)]
    highest_score:Annotated[int,Field(description="Highest Score In t20",ge=1)]

class test(TypedDict):
    matches:Annotated[int,Field(description="total matches in test",ge=1)]
    runs:Annotated[int,Field(description="total runs in test",ge=1)]
    hundreds:Annotated[int,Field(description="total hundreds in test",ge=1)]
    fifties:Annotated[int,Field(description="total fifties in test",ge=1)]
    fours:Annotated[int,Field(description="total fours in test",ge=1)]
    sixes:Annotated[int,Field(description="total sixes in test",ge=1)]
    highest_score:Annotated[int,Field(description="Highest Score In test",ge=1)]


class ipl(TypedDict):
    matches:Annotated[int,Field(description="total matches in ipl",ge=1)]
    runs:Annotated[int,Field(description="total runs in ipl",ge=1)]
    hundreds:Annotated[int,Field(description="total hundreds in ipl",ge=1)]
    fifties:Annotated[int,Field(description="total fifties in ipl",ge=1)]
    fours:Annotated[int,Field(description="total fours in ipl",ge=1)]
    sixes:Annotated[int,Field(description="total sixes in ipl",ge=1)]
    highest_score:Annotated[int,Field(description="Highest Score In ipl",ge=1)]


class Total(TypedDict):

    Name:Annotated[str,Field(description="Name Of the Player")]
    ODI:odi
    T20:t20
    TEST:test
    IPL:ipl
    Summary:Annotated[str,Field(description="Summary Of that player")]