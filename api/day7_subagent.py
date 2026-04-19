"""
Day 7: 子 Agent — task tool 上下文隔离

使用 task tool 派生专业子 Agent，
避免主 Agent 上下文被污染。
"""

from deepagents import create_deep_agent
from deepagents.middleware.subagents import SubAgent


def demo_task_tool():
    """task tool 演示：派生子 Agent 处理子任务"""
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        system_prompt="你是一个项目助手，可以派生子 Agent 处理专业任务。",
    )

    # Agent 收到复杂任务后自动分解
    # 主 Agent 负责规划，子 Agent 负责执行
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "帮我分析这个代码库，然后写一份文档"
        }]
    })
    print("【task tool】Agent 自动派生子 Agent 处理子任务")


def demo_subagent_config():
    """子 Agent 配置"""
    # 预定义子 Agent
    researcher = SubAgent(
        name="researcher",
        model="anthropic:claude-sonnet-4-6",
        system_prompt="你是一个研究员，专门收集和分析信息。",
    )

    writer = SubAgent(
        name="writer",
        model="anthropic:claude-sonnet-4-6",
        system_prompt="你是一个技术写手，擅长写清晰简洁的文档。",
    )

    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        subagents=[researcher, writer],  # 预定义子 Agent
    )
    print("【预定义子 Agent】researcher + writer")


if __name__ == "__main__":
    print("=== Day 7: 子 Agent ===\n")
    demo_subagent_config()
