"""
Day 5: Pluggable Backends — 可插拔文件系统后端

展示 Deep Agents 支持的多种存储后端：
StateBackend（内存）/ FilesystemBackend（磁盘）/ LangGraph Store（跨线程）
"""

from deepagents import create_deep_agent
from deepagents.backends import StateBackend, FilesystemBackend


def demo_state_backend():
    """StateBackend：文件保存在 LangGraph State 中，进程内有效，不落盘"""
    backend = StateBackend()
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        backend=backend,
        system_prompt="你可以在内存中读写文件。",
    )
    print("【StateBackend】所有文件操作只在 State 中，适合测试")


def demo_filesystem_backend():
    """FilesystemBackend：落地到本地磁盘"""
    backend = FilesystemBackend(root_dir="/tmp/deepagents-project")
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        backend=backend,
        system_prompt="你在 /tmp/deepagents-project 目录下工作。",
    )
    print("【FilesystemBackend】文件操作落地到本地磁盘")


def demo_langgraph_store():
    """LangGraph Store：跨线程持久化，适合生产"""
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore()
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        store=store,            # 跨对话持久化
        system_prompt="你有长期记忆，可以记住之前的对话内容。",
    )
    print("【LangGraph Store】跨线程持久化，适合生产环境")


if __name__ == "__main__":
    print("=== Day 5: Pluggable Backends ===\n")
    demo_state_backend()
    demo_filesystem_backend()
    demo_langgraph_store()
