"""
Day 8: 记忆与权限 — Memory Store + Filesystem Permissions

展示 LangGraph Memory Store 长期记忆和声明式权限控制。
"""

from deepagents import create_deep_agent
from deepagents.middleware.permissions import FilesystemPermission


def demo_memory_store():
    """长期记忆：跨对话记住之前的内容"""
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore()

    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        store=store,
        system_prompt="你有长期记忆，可以记住之前的对话内容。",
    )

    # 第一次对话：学习用户偏好
    agent.invoke({
        "messages": [{"role": "user", "content": "我叫张三，喜欢用中文交流"}]
    })

    # 第二次对话：记住上下文
    result = agent.invoke({
        "messages": [{"role": "user", "content": "我叫什么名字？"}]
    })
    print("【记忆查询结果】", result["messages"][-1].content)


def demo_filesystem_permissions():
    """声明式文件权限控制"""
    # 精确控制文件访问范围
    permissions = [
        FilesystemPermission(
            paths=["/project/src/**"],     # 代码目录：读写
            operations=["read", "write"],
            mode="allow",
        ),
        FilesystemPermission(
            paths=["/project/docs/**", "/project/**/*.py"],  # 文档 + Python 文件：只读
            operations=["read"],
            mode="allow",
        ),
        # 危险路径：明确禁止
        FilesystemPermission(
            paths=["/etc/**", "/home/**"],
            operations=["read", "write"],
            mode="deny",
        ),
    ]

    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        permissions=permissions,
    )
    print("【权限配置】代码读写、文档只读、系统目录禁止访问")


if __name__ == "__main__":
    print("=== Day 8: 记忆与权限 ===\n")
    demo_filesystem_permissions()
