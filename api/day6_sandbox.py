"""
Day 6: Shell 执行与沙箱 — execute tool

Deep Agents 的 LocalShellBackend 让 Agent 获得 execute 工具，
可以在本地受限目录下执行 Shell 命令。
"""

from deepagents import create_deep_agent
from deepagents.backends import LocalShellBackend


def demo_execute_tool():
    """execute tool 演示"""
    # 使用 LocalShellBackend 时，Agent 自动获得 execute 工具
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        backend=LocalShellBackend(root_dir="/tmp/deepagents-work", timeout=60),
        system_prompt="你是一个命令行助手，可以在 /tmp/deepagents-work 下执行命令。",
    )

    # Agent 可以调用 execute tool
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "在当前目录运行 ls -la 和 git status"
        }]
    })
    print("【execute 工具】Agent 可在受限目录下执行 Shell 命令")


def demo_sandbox_options():
    """生产环境的沙箱选项"""
    options = [
        ("LocalShellBackend", "本地直跑（推荐先用这个熟悉 execute 工具）"),
        ("LangSmithSandbox", "LangSmith 托管的远端沙箱（生产推荐）"),
        ("自定义 Backend", "实现 BackendProtocol 对接 Modal/Daytona/Deno 等"),
    ]
    print("【沙箱选项】")
    for name, desc in options:
        print(f"  {name}: {desc}")


if __name__ == "__main__":
    print("=== Day 6: Shell 执行与沙箱 ===\n")
    demo_sandbox_options()
