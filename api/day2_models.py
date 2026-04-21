"""
Day 2: 模型配置 — 多 Provider 支持

展示 Deep Agents 支持的各种模型 Provider，
以及如何切换模型。
"""

import os


def demo_model_providers():
    """Deep Agents 支持的模型 Provider"""
    providers = [
        ("openai", "gpt-4.1"),
        ("anthropic", "claude-sonnet-4-6"),
        ("google-genai", "gemini-2.0-pro"),
        ("openrouter", "anthropic/claude-sonnet-4-6"),
        ("fireworks", "accounts/fireworks/models/qwen2p5-72b-instruct"),
        ("ollama", "qwen2.5:7b"),
        ("groq", "llama-3.3-70b-versatile"),
        ("deepseek", "deepseek-chat"),
    ]
    print("【支持的 Provider 示例】")
    for provider, model in providers:
        print(f"  {provider}: {model}")


def demo_switch_model():
    """演示如何切换模型"""
    # 不需要改代码，只需要改 model 字符串
    model_str = "openai:gpt-4.1"

    # 或者通过环境变量
    # DEEP_AGENTS_MODEL=anthropic:claude-sonnet-4-6

    print(f"当前模型: {model_str}")


if __name__ == "__main__":
    print("=== Day 2: 模型配置 ===\n")
    demo_model_providers()
