"""
Day 1: 认识 Deep Agents — 与 LangChain/LangGraph 的关系

本文件展示 Deep Agents 与 LangChain/LangGraph 的关系，
以及 create_deep_agent 的基本用法。
"""

from deepagents import create_deep_agent
from langchain_core.tools import tool


def demo_basic_agent():
    """最基础的 Deep Agent 演示"""
    # 定义一个简单工具（用 @tool 装饰器）
    @tool
    def get_weather(city: str) -> str:
        """获取城市天气"""
        return f"{city} 今天晴天，25°C"

    # 创建 Agent
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        tools=[get_weather],
        system_prompt="你是一个乐于助人的天气助手",
    )

    # 调用 Agent
    result = agent.invoke({
        "messages": [{"role": "user", "content": "北京今天天气怎么样？"}]
    })

    # 打印最后一条消息
    print("【Agent 响应】")
    print(result["messages"][-1].content)


def demo_vs_langchain():
    """
    Deep Agents vs LangChain Agent 的区别

    LangChain Agent：
    - 需要手动配置 tools、prompt、agent type
    - 缺少内置的任务规划、文件系统等能力

    Deep Agents：
    - create_deep_agent 一行创建
    - 内置 write_todos、ls/read/write/edit_file 等工具
    - 内置 human-in-the-loop、permissions、subagents 等能力
    """
    print("【对比】")
    print("LangChain:  需要手动配置 tools + prompt + agent type")
    print("Deep Agents: create_deep_agent 一行搞定，内置丰富工具")


if __name__ == "__main__":
    print("=== Day 1: 认识 Deep Agents ===\n")
    demo_vs_langchain()
    print("\n如需运行实际 Agent，请设置 ANTHROPIC_API_KEY 环境变量")
