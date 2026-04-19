# Deep Agents 10 天系列教程

基于 `deepagents==0.5.3` 的代码示例。

## 环境安装

```bash
uv sync
```

## 文件结构

```
deepagents-10days/
├── api/
│   ├── day1_intro.py           # Day 1: 认识 Deep Agents
│   ├── day2_models.py          # Day 2: 模型配置
│   ├── day3_planning.py        # Day 3: 任务规划
│   ├── day4_filesystem.py      # Day 4: 虚拟文件系统
│   ├── day5_backends.py        # Day 5: Pluggable Backends
│   ├── day6_sandbox.py         # Day 6: Shell 执行与沙箱
│   ├── day7_subagent.py        # Day 7: 子 Agent
│   ├── day8_memory_permissions.py  # Day 8: 记忆与权限
│   ├── day9_skills_hitl.py     # Day 9: Skills 与 Human-in-the-loop
│   └── day10_cli_acp.py        # Day 10: CLI + ACP + 实战
├── core/
├── tests/
├── pyproject.toml
└── README.md
```

## 快速开始

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="你是一个助手",
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "你好"}]
})
```

## 环境变量

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export OPENAI_API_KEY=sk-...
```
