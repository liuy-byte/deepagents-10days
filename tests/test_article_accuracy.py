"""验证 Deep Agents 10 天系列示例代码与当前 deepagents SDK 对齐。

运行：uv run python tests/test_article_accuracy.py
"""

import sys
from pathlib import Path

# 把项目根目录加到 path，方便 `import api.xxx` / `import core.xxx`
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))


def test_all_modules_importable():
    """所有 day 示例 + core 模块都能干净 import（无 ImportError / SyntaxError）。"""
    modules = [
        "api.day1_intro",
        "api.day2_models",
        "api.day3_planning",
        "api.day4_filesystem",
        "api.day5_backends",
        "api.day6_sandbox",
        "api.day7_subagent",
        "api.day8_memory_permissions",
        "api.day9_skills_hitl",
        "api.day10_cli_acp",
        "api.main",
        "core.coding_agent",
    ]
    for m in modules:
        __import__(m)
    print(f"✓ import 全部通过（{len(modules)} 个模块）")


def test_key_constructors():
    """关键 API 的真实签名/字段。

    目的：防止有人再把文章里错的 API 抄回代码。
    """
    from deepagents.middleware.permissions import FilesystemPermission
    from deepagents.middleware.subagents import SubAgent, InterruptOnConfig
    from deepagents.backends import StateBackend, FilesystemBackend, LocalShellBackend
    from langgraph.store.memory import InMemoryStore

    # FilesystemPermission 字段是 paths（复数） + operations + mode
    perm = FilesystemPermission(
        paths=["/project/**"],
        operations=["read", "write"],
        mode="allow",
    )
    assert perm.paths == ["/project/**"]
    assert perm.mode == "allow"

    # SubAgent 必填字段：name / description / system_prompt
    sub = SubAgent(name="r", description="研究员", system_prompt="hi")
    assert sub["name"] == "r"

    # InterruptOnConfig 在 subagents 子模块（TypedDict，字典式访问）
    cfg = InterruptOnConfig(always=True, description="x")
    assert cfg["always"] is True

    # Backend 类名校验
    StateBackend()
    FilesystemBackend(root_dir="/tmp/x", virtual_mode=True)
    LocalShellBackend(root_dir="/tmp/x", timeout=10, virtual_mode=True)

    # Store 正确名字是 InMemoryStore，不是 MemoryStore
    InMemoryStore()

    print("✓ 关键构造器全部通过（permission/subagent/interrupt/backends/store）")


def test_create_deep_agent_signature():
    """create_deep_agent 关键参数仍然存在。"""
    import inspect
    from deepagents import create_deep_agent

    params = set(inspect.signature(create_deep_agent).parameters)
    for p in ["model", "tools", "system_prompt", "subagents", "skills",
              "permissions", "store", "backend", "interrupt_on", "checkpointer"]:
        assert p in params, f"create_deep_agent 缺少 {p} 参数：{params}"
    print("✓ create_deep_agent 签名正确")


if __name__ == "__main__":
    print("运行 Deep Agents 10 天系列测试...\n")
    test_all_modules_importable()
    test_key_constructors()
    test_create_deep_agent_signature()
    print("\n🎉 所有测试通过！")
