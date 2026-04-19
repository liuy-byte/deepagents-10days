"""配置管理"""

import json
import os
from pathlib import Path
from typing import Literal
from pydantic import BaseModel, Field


class AgentConfig(BaseModel):
    model: str = "anthropic:claude-sonnet-4-6"
    permissions_enabled: bool = True
    memory_enabled: bool = True
    sandbox_enabled: bool = False
    interrupt_on_delete: bool = True

    @classmethod
    def from_json(cls, path: str | Path) -> "AgentConfig":
        with open(path, "r", encoding="utf-8") as f:
            return cls(**json.load(f))

    def resolve_env_vars(self) -> None:
        if model := os.environ.get("DEEPAGENTS_MODEL"):
            self.model = model


def load_config(path: str | Path | None = None) -> AgentConfig:
    if path is None:
        config_path = Path(__file__).parent.parent / "config.json"
    else:
        config_path = Path(path)

    if config_path.exists():
        config = AgentConfig.from_json(config_path)
    else:
        config = AgentConfig()

    config.resolve_env_vars()
    return config
