"""
Day 5: Pluggable Backends — 可插拔文件系统后端

展示 Deep Agents 支持的多种存储后端：
InMemory / Local / LangGraph Store
"""

from deepagents import create_deep_agent
from deepagents.backends import InMemoryBackend, LocalBackend


def demo_in_memory_backend():
    """内存后端：测试用，不落盘"""
    backend = InMemoryBackend()
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        backend=backend,
        system_prompt="你可以在内存中读写文件。",
    )
    print("【InMemoryBackend】所有文件操作不落盘，适合测试")


def demo_local_backend():
    """本地磁盘后端"""
    backend = LocalBackend(root="/tmp/deepagents-project")
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        backend=backend,
        system_prompt="你在 /tmp/deepagents-project 目录下工作。",
    )
    print("【LocalBackend】文件操作落地到本地磁盘")


def demo_langgraph_store():
    """LangGraph Store：跨线程持久化，适合生产"""
    from langgraph.store.memory import MemoryStore

    store = MemoryStore()
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        store=store,            # 跨对话持久化
        system_prompt="你有长期记忆，可以记住之前的对话内容。",
    )
    print("【LangGraph Store】跨线程持久化，适合生产环境")


if __name__ == "__main__":
    print("=== Day 5: Pluggable Backends ===\n")
    demo_in_memory_backend()
    demo_local_backend()
    demo_langgraph_store()
