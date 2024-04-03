import chainlit as cl
import json
import requests

# connect to API from ngrok
# then interface with chainlit client

colab_url = "https://73e4-34-106-55-57.ngrok-free.app/"

# format will be
ex = \
    """
{
  "prompt": "\n\n### Instructions:\nWhat is the capital of France?\n\n### Response:\n",
  "stop": [
    "\n",
    "###"
  ]
}
"""


def send_prompt(text):
    # some of the settings can be tweaked, performance is also not great
    to_send = {
        'prompt': f"\n\n### Instructions:\n{text}\n\n### Response:\n",
        'stop': ['\n', '###']
    }
    to_send_json = json.dumps(to_send)
    resp = requests.post(colab_url + "v1/completions", data=to_send_json)
    out = ""
    if resp.status_code == 200:
        resp_data = resp.json()
        out = resp_data["choices"][0]["text"]
    else:
        out = f"Error: {resp.status_code}"
    return out


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    display = send_prompt(message.content)

    # Send a response back to the user
    await cl.Message(
        content=f"{display}",
    ).send()
