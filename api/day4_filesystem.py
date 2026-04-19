"""
Day 4: 虚拟文件系统 — ls/read/write/edit_file

Deep Agents 内置虚拟文件系统工具，
支持内存、磁盘、LangGraph Store 等多种后端。
"""

from deepagents import create_deep_agent


def demo_virtual_filesystem():
    """虚拟文件系统工具演示"""
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        system_prompt="你是一个文件管理助手，擅长读写文件和目录操作。",
    )

    # 列出当前目录
    result = agent.invoke({
        "messages": [{"role": "user", "content": "列出当前目录的文件"}]
    })
    print("【ls 结果】")
    print(result["messages"][-1].content[:300])


def demo_file_operations():
    """文件操作工具列表"""
    tools = [
        ("ls", "列出目录内容"),
        ("read_file", "读取文件内容"),
        ("write_file", "写入文件内容"),
        ("edit_file", "编辑文件内容（基于 diff）"),
    ]
    print("【虚拟文件系统工具】")
    for tool, desc in tools:
        print(f"  {tool}: {desc}")


if __name__ == "__main__":
    print("=== Day 4: 虚拟文件系统 ===\n")
    demo_file_operations()
