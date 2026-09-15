# SmartVoyage 旅行智能助手

基于 Agent2Agent（A2A）和 Model Context Protocol（MCP）的多智能体旅行助手示例，包含天气查询、票务查询、票务预订和景点推荐能力。

## 安全配置

复制 `.env.example` 为 `.env`，并在启动前将变量导入当前 shell。项目不会在代码中保存 LLM、天气服务或数据库凭据。

## 安装

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

## 运行

先准备 MySQL 数据库并执行 `sql/` 下的脚本，再分别启动 MCP 服务、A2A 服务，最后运行主程序：

```bash
streamlit run SmartVoyage/app.py
```

命令行入口为 `python -m SmartVoyage.main`。服务地址默认使用 `8002`、`8003` 和 `5005`-`5007` 端口，具体可在对应服务文件中调整。
