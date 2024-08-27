import json
import logging
from schema import Schema, Regex, And, Use, SchemaError, Optional


def work(as_json: str) -> str:
    schema = Schema(
        {
            "foo": {
                "version": And(Use(int), lambda x: x > 0),
                "blocks": {Optional(Regex("^block\\d+$")): {"data": str}},
            }
        }
    )
    data = json.loads(as_json)
    try:
        data = schema.validate(data)
    except SchemaError as er:
        logging.error(f"Failed to validate json: {er}")
        return json.dumps({})

    data["foo"]["version"] = 3
    rv = json.dumps(data)
    return rv
