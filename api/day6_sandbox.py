"""
Day 6: Shell 执行与沙箱 — execute tool

Deep Agents 的 execute tool 允许 Agent 执行 Shell 命令，
配合沙箱后端实现安全隔离。
"""

from deepagents import create_deep_agent
from deepagents.backends.sandbox import SandboxBackend


def demo_execute_tool():
    """execute tool 演示"""
    # 使用沙箱后端时，Agent 获得 execute 工具
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        backend=SandboxBackend(),  # 沙箱后端
        system_prompt="你是一个命令行助手，可以在沙箱中执行命令。",
    )

    # Agent 可以调用 execute tool
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "在当前目录运行 ls -la 和 git status"
        }]
    })
    print("【execute 工具】Agent 可执行 Shell 命令")


def demo_sandbox_backends():
    """支持的沙箱后端"""
    backends = [
        ("Modal", "云端隔离执行环境"),
        ("Daytona", "本地沙箱服务"),
        ("Deno", "JavaScript 运行时沙箱"),
    ]
    print("【支持的沙箱后端】")
    for name, desc in backends:
        print(f"  {name}: {desc}")


if __name__ == "__main__":
    print("=== Day 6: Shell 执行与沙箱 ===\n")
    demo_sandbox_backends()
