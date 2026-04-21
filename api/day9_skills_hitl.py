"""
Day 9: Skills 与 Human-in-the-loop

Skills：可复用的领域技能扩展
Human-in-the-loop：敏感操作需要人工审批
"""

from deepagents import create_deep_agent
from deepagents.middleware.subagents import InterruptOnConfig


def demo_skills():
    """Skills：复用 Prompt + 工具的技能包"""
    # 内置 Skill 示例
    skills = [
        "langchain:code-review",      # 代码审查技能
        "langchain:write-tests",      # 写测试技能
    ]

    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        skills=skills,
        system_prompt="你是一个开发助手，可以调用专业技能完成任务。",
    )
    print("【Skills】可复用的领域技能扩展")


def demo_human_in_the_loop():
    """Human-in-the-loop：敏感操作需要人工审批"""
    # 配置哪些工具需要审批
    interrupt_on = {
        "delete_file": True,          # 删除文件需要确认
        "execute": InterruptOnConfig(
            always=True,
            description="Shell 命令执行需要审批",
        ),
        "write_file": InterruptOnConfig(
            when=lambda ctx: "/etc" in ctx["path"],  # 写系统目录需要确认
        ),
    }

    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        interrupt_on=interrupt_on,
    )
    print("【Human-in-the-loop】敏感操作暂停，等待人工审批")


if __name__ == "__main__":
    print("=== Day 9: Skills 与 Human-in-the-loop ===\n")
    demo_skills()
    demo_human_in_the_loop()
