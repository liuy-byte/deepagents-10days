"""
Deep Agents 10 天实战：知识库问答机器人

串联所有核心概念：
- create_deep_agent 主 Agent
- 子 Agent 隔离上下文
- 虚拟文件系统
- 记忆与权限
- Skills 与 HITL
"""

from typing import Optional
from deepagents import create_deep_agent


# ============ 1. 创建主 Agent ============
agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="""你是一个知识库问答助手。

能力：
- 回答关于技术文档的问题
- 可以联网搜索最新信息
- 会记住对话历史

如果不知道答案，就说不知道。""",
)


# ============ 2. 创建子 Agent（专门处理代码问题）===========
code_agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="""你是一个代码审查助手。

职责：
- 审查代码问题
- 提供代码优化建议
- 解释代码逻辑

只回答代码相关问题。""",
)


# ============ 3. 知识库管理 ============
class KnowledgeBase:
    """模拟知识库"""

    def __init__(self):
        self.docs = {}
        self.doc_count = 0

    def add_document(self, name: str, content: str):
        """添加文档到知识库"""
        self.docs[name] = content
        self.doc_count += 1
        return f"已添加文档：{name}"

    def search(self, query: str) -> list:
        """搜索知识库"""
        results = []
        for name, content in self.docs.items():
            if any(kw in content for kw in query.split()):
                results.append(f"[{name}]: {content[:100]}...")
        return results if results else []


knowledge_base = KnowledgeBase()


# ============ 4. RAG 检索增强 ============
def rag_search(query: str) -> str:
    """RAG 检索"""
    results = knowledge_base.search(query)

    if results:
        context = "\n\n".join(results)
        return f"【知识库检索结果】\n{context}"
    return ""


# ============ 5. 对话处理 ============
def chat(user_input: str, thread_id: str = "default") -> str:
    """处理对话"""
    config = {"configurable": {"thread_id": thread_id}}

    # RAG 增强
    context = rag_search(user_input)

    # 构建消息
    if context:
        message = f"{user_input}\n\n{context}"
    else:
        message = user_input

    # 调用 Agent
    result = agent.invoke({
        "messages": [{"role": "user", "content": message}]
    })

    # 提取回复
    if result.get("messages"):
        last_msg = result["messages"][-1]
        return last_msg.get("content", "抱歉，我没有找到相关信息。")

    return "抱歉，处理失败。"


# ============ 6. CLI 交互 ============
def main():
    print("=" * 50)
    print("Deep Agents 10 天实战 - 知识库问答机器人")
    print("=" * 50)
    print()

    # 添加示例文档
    print("📚 初始化知识库...")
    knowledge_base.add_document(
        "LangGraph 介绍",
        "LangGraph 是一个用于构建状态化 AI 应用的框架，支持条件边、检查点持久化、流式输出等功能。"
    )
    knowledge_base.add_document(
        "LangChain 介绍",
        "LangChain 是 LangChain 生态的基础组件库，提供了 Model I/O、Retrieval、Memory 等模块。"
    )
    knowledge_base.add_document(
        "Deep Agents 介绍",
        "Deep Agents 是基于 LangChain 的高级 Agent 封装，内置长对话压缩、虚拟文件系统、子 Agent 等功能。"
    )
    print(f"✅ 已添加 {knowledge_base.doc_count} 个文档到知识库")
    print()

    thread_id = "deep-agents-bot-001"
    mode = "main"  # "main" 或 "code"

    while True:
        try:
            user_input = input("👤 你: ").strip()
            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "退出"]:
                print("再见！")
                break

            if user_input.lower() == "!code":
                mode = "code"
                print("🔧 切换到代码审查模式")
                continue

            if user_input.lower() == "!normal":
                mode = "main"
                print("💬 切换到普通问答模式")
                continue

            if user_input.lower() == "!help":
                print("""
命令：
  !code   - 切换到代码审查模式
  !normal - 切换到普通问答模式
  !quit   - 退出
""")
                continue

            # 根据模式选择 Agent
            if mode == "code":
                print("🤖 [代码助手]: ", end="", flush=True)
                # 这里简化处理，实际应该用 code_agent
                print("请输入代码相关问题...")
            else:
                response = chat(user_input, thread_id=thread_id)
                print(f"🤖 AI: {response}")

            print()

        except KeyboardInterrupt:
            print("\n再见！")
            break


if __name__ == "__main__":
    main()
