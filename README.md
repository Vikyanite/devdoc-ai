基础目录结构：

  ```text
  devdoc-ai/
    app/
      __init__.py
      main.py          # FastAPI 入口，路由定义
      config.py        # 配置 & 环境变量
      llm_client.py    # 大模型调用封装
      rag_service.py   # RAG 逻辑（先留空）
      schemas.py       # 请求/响应模型
    data/
      docs/            # Markdown 文档目录
    scripts/
      rebuild_index.py # 重建索引脚本（后面实现）
    tests/
      __init__.py
    .env.example
    README.md
    requirements.txt
  ```