# Fusion Cyber Takehome

First, run the python notebook in google colab. You will need to have an ngrok authentication token, and include it under your secrets tab, with the name "NGROK". The final commands in the notebook close the server, don't run them until you are finished.

Once you have the python notebook running, change the public url in the local_ui.py to the one output in the notebook. Then run ``chainlit run local_ui.py -w`` to have a simple UI for the chatbot.
