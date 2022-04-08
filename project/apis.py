from typing import Annotated, Any

from hintapi import Path, Query, Body, Depends, Routes, JSONResponse

from .schemas import Message

routes = Routes()


@routes.http.get("/")
def homepage(
    name: str = Query(..., example="World"),
) -> Annotated[Any, JSONResponse[200, {}, Message]]:
    """
    Homepage

    Returns a greeting message.
    """
    return {"message": f"Hello, {name}!"}
