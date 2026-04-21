"""
Day 10: CLI + ACP + 实战

Deep Agents CLI：终端编程助手
ACP：Agent Client Protocol，集成到编辑器
实战：串联所有能力做一个完整应用
"""

from deepagents import create_deep_agent


def demo_cli():
    """Deep Agents CLI"""
    # 安装
    # uv tool install 'deepagents-cli[anthropic,openai]'
    #
    # 启动
    # deepagents --model anthropic:claude-sonnet-4-6
    #
    # 常用命令
    # /model <provider:model>  切换模型
    # /help                   显示帮助
    # /exit                   退出
    print("【CLI】deepagents --model <provider:model>")


def demo_acp():
    """ACP：Agent Client Protocol"""
    # ACP 让你在编辑器里使用 Deep Agents
    # 支持 Zed 等编辑器
    #
    # 安装 ACP 后，在编辑器中配置：
    # {
    #   "deepagents": {
    #     "model": "anthropic:claude-sonnet-4-6"
    #   }
    # }
    print("【ACP】在编辑器中集成 Deep Agents")


def demo_full_integration():
    """串联所有能力：RAG 问答机器人"""
    from langgraph.store.memory import InMemoryStore
    from deepagents.middleware.permissions import FilesystemPermission

    # 完整配置
    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        # 记忆
        store=InMemoryStore(),
        # 权限
        permissions=[
            FilesystemPermission(
                paths=["/project/docs/**"],
                operations=["read"],
                mode="allow",
            ),
        ],
        # 子 Agent
        subagents=[],
        # 沙箱（执行命令）
        backend=None,  # 使用默认后端
        # 人为介入
        interrupt_on={
            "delete_file": True,
        },
        system_prompt="""你是一个文档助手，职责：
1. 读取 /project/docs 下的文档
2. 回答用户关于文档的问题
3. 如果需要执行命令（如搜索），先申请审批
4. 保持对话记忆，记住之前的偏好""",
    )
    print("【完整实战】RAG 问答机器人：记忆 + 权限 + 子 Agent + 人为介入")


if __name__ == "__main__":
    print("=== Day 10: CLI + ACP + 实战 ===\n")
    demo_full_integration()
