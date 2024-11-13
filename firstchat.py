from http import HTTPStatus
from dashscope import Application
import time


def call_agent_app(prompt, api_key):
    response = Application.call(app_id='',
                                prompt=prompt,
                                api_key=api_key)

    if response.status_code != HTTPStatus.OK:
        print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code, response.message))
        return None
    else:
        output_text = response.output.get("text", "")

        return output_text


def stream_output(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # 模拟输出延迟，让每个字符逐步输出
    print()  # 打印结束后换行


def chatbot():
    api_key = 'sk-35eeb2de4bad4e97916b15cec7c4dab9'  
    print("你好，我是你的智能助手。有问题请问我吧！（输入'再见'可以结束对话）")
    while True:
        user_input = input("你: ")
        if user_input.lower() in ["再见", "结束", "拜拜"]:
            stream_output("助手: 感谢您的咨询，再见")
            break
        else:
            response = call_agent_app(user_input, api_key)
            if response:
                # 提取输出中的关键信息，只显示回答部分
                relevant_output = response.split('，')[0] + '，' + response.split('，')[1]
                stream_output(f"助手: {relevant_output}")


if __name__ == '__main__':
    chatbot()
