#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名: config.py
作者: ZZS
项目: LlmProject
创建日期: 2026/1/17
描述: 
"""

import os

# 项目根目录
project_root = os.path.dirname(os.path.abspath(__file__))

# 生产环境
# env = "prod"
# 测试环境
env = "test"
# 开发环境
# env = "dev"
# 预生产环境
# env = "pre_prod"



#定义配置文件
class Config:

    def __init__(self):
        # 大模型配置
        self.base_url = os.getenv('LLM_BASE_URL', 'https://api.siliconflow.cn/v1')
        self.api_key = os.getenv('LLM_API_KEY', '')
        self.model_name = os.getenv('LLM_MODEL', 'Qwen/Qwen2.5-72B-Instruct')

        # 数据库配置
        self.host = os.getenv('MYSQL_HOST', 'localhost')
        self.user = os.getenv('MYSQL_USER', 'root')
        self.password = os.getenv('MYSQL_PASSWORD', '')
        self.database = os.getenv('MYSQL_DATABASE', 'travel_rag')

        # 日志配置
        self.log_file = os.getenv('LOG_FILE', os.path.join(project_root, 'logs', 'app.log'))

        # 票务查询的12306接口地址
        self.url_123 = os.getenv('TICKET_API_URL', '')

        self.intent = {
            "weather":"WeatherQueryAssistant",
            "flight":"TicketQueryAssistant",
            "train":"TicketQueryAssistant",
            "concert":"TicketQueryAssistant",
            "order":"TicketOrderAssistant"
        }

        self.temperature = 0.1


    def get_mysql_config(self,env):
        """
        通过不同的环境获取不同的数据库配置
        :return:
        """
        # 支持按环境覆盖，未配置时回退到通用环境变量；不在代码中保存口令。
        env_name = {'prod': 'PROD', 'dev': 'DEV', 'test': 'TEST', 'pre_prod': 'PRE_PROD'}.get(env, 'DEFAULT')
        self.host = os.getenv(f'{env_name}_MYSQL_HOST', os.getenv('MYSQL_HOST', 'localhost'))
        self.user = os.getenv(f'{env_name}_MYSQL_USER', os.getenv('MYSQL_USER', 'root'))
        self.password = os.getenv(f'{env_name}_MYSQL_PASSWORD', os.getenv('MYSQL_PASSWORD', ''))
        self.database = os.getenv(f'{env_name}_MYSQL_DATABASE', os.getenv('MYSQL_DATABASE', 'travel_rag'))

        return self.host, self.user, self.password, self.database


if __name__ == '__main__':
    print(Config().log_file)
    print(Config().get_mysql_config(env))
    # ('localhost', 'root', 'root', 'travel_rag')
    # ('localhost', 'root2', 'root2', 'travel_rag')
