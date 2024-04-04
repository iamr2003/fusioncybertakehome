import chainlit as cl
import json
import requests

#UPDATE THIS WITH URL FROM COLAB
colab_url = "https://9615-35-236-248-237.ngrok-free.app/"


def send_prompt(text):
    to_send = {
        'prompt': text,
    }
    headers = {'Content-Type': 'application/json'}
    to_send_json = json.dumps(to_send)
    resp = requests.post(colab_url + "/prompt", data=to_send_json, headers=headers)
    out = ""
    if resp.status_code == 200:
        resp_data = resp.json()
        out = resp_data["response"]
    else:
        out = f"Error: {resp.status_code}"
    return out


@cl.on_message
async def main(message: cl.Message):
    display = send_prompt(message.content)

    await cl.Message(
        content=f"{display}",
    ).send()
