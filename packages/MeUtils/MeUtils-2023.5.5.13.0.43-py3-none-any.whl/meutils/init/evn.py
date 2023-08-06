#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : evn
# @Time         : 2023/4/27 16:57
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 

import os

# 环境变量配置
os.environ['JINA_HIDE_SURVEY'] = '0'
os.environ["TOKENIZERS_PARALLELISM"] = "true"

# LLM
os.environ['LLM_ROLE'] = '你扮演的角色是ChatLLM灵知大语言模型，是由Betterme开发'
os.environ['PROMPT_TEMPLATE'] = """
{role}
基于以下<>中的信息，简洁和专业的来回答问题。
信息：<{context}>
问题：{question}
如果无法从中得到答案，请说“根据已知信息无法回答该问题”或“没有提供足够的信息”，不允许在答案中添加编造成分，答案请使用中文。
""".strip()

if __name__ == '__main__':
    from pprint import pprint

    pprint(os.environ['PROMPT_TEMPLATE'])
