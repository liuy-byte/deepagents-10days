"""Coding Agent — 串联 Deep Agents 所有能力的实战项目"""

from typing import Any

from deepagents import create_deep_agent
from deepagents.middleware.permissions import FilesystemPermission
from deepagents.middleware.human_in_the_loop import InterruptOnConfig

from core.config import AgentConfig


class CodingAgent:
    """
    串联 Deep Agents 所有能力的编程助手 Agent。

    能力：
    - 任务规划（write_todos）
    - 虚拟文件系统（ls/read/write/edit_file）
    - Shell 执行（execute，沙箱模式下）
    - 子 Agent 派生
    - 长期记忆（Memory Store）
    - 文件权限控制
    - 人为介入（危险操作审批）
    """

    def __init__(self, config: AgentConfig | None = None):
        self.config = config or AgentConfig()
        self._agent: Any = None
        self._setup()

    def _setup(self) -> None:
        # 权限配置
        permissions = None
        if self.config.permissions_enabled:
            permissions = [
                FilesystemPermission(
                    path="/project/**",
                    operations=["read", "write"],
                ),
                FilesystemPermission(
                    path="/tmp/**",
                    operations=["read", "write", "execute"],
                ),
            ]

        # 人为介入配置
        interrupt_on = None
        if self.config.interrupt_on_delete:
            interrupt_on = {
                "delete_file": True,
            }

        # 构建系统提示词
        system_prompt = """你是一个专业的编程助手。

职责范围：
1. 读取和理解代码文件
2. 编写和修改代码
3. 运行测试和构建命令
4. 分解复杂任务为可执行步骤

工作流程：
1. 理解用户需求
2. 使用 write_todos 分解任务
3. 按步骤执行，每步记录结果
4. 完成后总结输出

安全规则：
- 删除文件前必须确认
- 执行 Shell 命令前说明风险
- 不访问项目目录外的文件"""

        # 创建 Agent
        self._agent = create_deep_agent(
            model=self.config.model,
            system_prompt=system_prompt,
            permissions=permissions,
            interrupt_on=interrupt_on,
        )

    def invoke(self, messages: list[dict]) -> dict:
        """执行对话"""
        return self._agent.invoke({"messages": messages})

    def chat(self, user_input: str, history: list[dict] | None = None) -> str:
        """单轮对话"""
        messages = history or []
        messages.append({"role": "user", "content": user_input})
        result = self.invoke(messages)
        assistant_msg = result["messages"][-1].content
        messages.append({"role": "assistant", "content": assistant_msg})
        return assistant_msg, messages


def demo():
    """演示 Coding Agent"""
    config = AgentConfig(
        model="anthropic:claude-sonnet-4-6",
        permissions_enabled=True,
        memory_enabled=True,
        interrupt_on_delete=True,
    )

    agent = CodingAgent(config)

    # 对话示例
    response, _ = agent.chat("帮我规划一下如何用 Deep Agents 写一个 CLI 工具")
    print(response)


if __name__ == "__main__":
    demo()
