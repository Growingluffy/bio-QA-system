# -*- coding: utf-8 -*-
# 测试函数
from service import TemplateBot

if __name__ == '__main__':
    template_bot = TemplateBot()
    while 1:
        query = raw_input('请输入问句：')
        answer = template_bot.reply(query)
        print answer
