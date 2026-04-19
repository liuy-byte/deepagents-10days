"""
Day 3: 任务规划 — write_todos 任务分解与执行

Deep Agents 内置 write_todos 工具，
让 Agent 能够分解复杂任务并追踪进度。
"""

from deepagents import create_deep_agent


def demo_write_todos():
    """write_todos 内置工具演示"""
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        system_prompt="你是一个任务规划助手，擅长将复杂任务分解为步骤。",
    )

    # Agent 会自动调用 write_todos 工具分解任务
    result = agent.invoke({
        "messages": [{"role": "user", "content": "帮我规划一下如何学习 Deep Agents"}]
    })

    print("【任务规划结果】")
    for msg in result["messages"]:
        if hasattr(msg, "content") and isinstance(msg.content, list):
            for block in msg.content:
                if hasattr(block, "text"):
                    print(f"  {block.text[:200]}")


def demo_todo_structure():
    """write_todos 的数据结构"""
    # write_todos 工具调用的典型输入格式
    todos_input = {
        "todos": [
            {
                "id": "1",
                "content": "阅读 Deep Agents 官方文档",
                "status": "in_progress",
                "priority": "high",
            },
            {
                "id": "2",
                "content": "搭建开发环境",
                "status": "pending",
                "priority": "high",
            },
            {
                "id": "3",
                "content": "运行 Quickstart 示例",
                "status": "pending",
                "priority": "medium",
            },
        ]
    }
    print("【write_todos 数据格式】")
    print(todos_input)


if __name__ == "__main__":
    print("=== Day 3: 任务规划 ===\n")
    demo_todo_structure()
