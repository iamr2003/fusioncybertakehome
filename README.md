# Fusion Cyber Takehome

First, run the python notebook in google colab. You will need to have an ngrok authentication token, and include it under your secrets tab, with the name "NGROK". This will start a flask server to allow running commands on a LangChain on top of llama2.

Once you have the python notebook running, change the public url in the local_ui.py to the ngroke one that is outputted in the notebook. Then run ``chainlit run local_ui.py -w`` to have a simple UI for the chatbot.


I would highly recommend using a stronger google colab version than the base level, performance becomes very slow when using LangChain. In this demo, the model is limited to producing only 10 tokens for speed. However, without langchain the model can run significantly faster.
