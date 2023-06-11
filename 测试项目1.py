

#MiniMax 快速开始
import requests
import readline
group_id = "请填写您的group_id"
api_key = "请填写您的api_key"

#构建请求头：根据鉴权信息构建请求头（group_id和api_key为需要您替换的鉴权信息）
url = f'https://api.minimax.chat/v1/text/chatcompletion?GroupId={group_id}'
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

#构建请求内容
#本示例是基于python在终端交互的对话，input关键字内的提示词根据您的场景替换成对应的用户输入获取代码或参数。 其余参数，不建议您修改。
#prefix, user_name, bot_name = choose_prefix()
#tokens_to_generate可自行修改，范围为0-4096
request_body = {
        "model":"abab5-chat",
        "tokens_to_generate": 512,
        'messages': []
}
#添加循环完成多轮交互
while True:
    #下面的输入获取是基于python终端环境，请根据您的场景替换成对应的用户输入获取代码
    line = input("发言:")
    # 将当次输入内容作为用户的一轮对话添加到messages
    request_body['messages'].append({"sender_type": "USER","text": line})

    #完成交互
#通过requests库提供的post能力对api进行调用，复制下面的代码即可完成多轮交互。
#注意：每一轮回复都需要追加到messages中，这样才能在多轮的对话中记住对话历史。
    response = requests.post(url, headers=headers, json=request_body)
    reply = response.json()['reply']
    print(f"reply: {reply}")
    #  将当次的ai回复内容加入messages
    request_body['messages'].append({"sender_type": "BOT","text": reply})