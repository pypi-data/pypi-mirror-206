from datetime import datetime as _datetime
import typing as _typing
from typing import Optional as _Optional

from pydantic import BaseModel as __BaseModel, Field as _Field

class SnapshotMeta(__BaseModel):
    user_id: int
    challenge_id: int
    is_verified: bool = False
    verified_message: _Optional[str]
    date_created: _datetime
    internal_error: _Optional[str]  # might be removed in future. moderator attribute
    id: int
    is_from_code_run: bool
    challenge_name: str
    is_result_json_loadable: _Optional[bool] = _Field(alias="is_json_data_loadable")
    # backend responses with alias name, we rename it into schema name
    result_file_url: _Optional[str] = _Field(alias="json_data_file_url")


class Snapshot(SnapshotMeta):
    result: _typing.Any
    "loaded result of snapshot"
