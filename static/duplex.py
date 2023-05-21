from browser import prompt, websocket, window, html, document, bind

@bind('#send', 'click')
def send_message(evt):
    ws.send(f'({nome}) {document["text"].value}')
    document['text'].value = ""

def on_message(evt):
    messages = document['messages']
    messages <= html.P(evt.data)
    messages.scrollTop = messages.scrollHeight - messages.clientHeight

def on_open(evt):
    ws.send(f'({nome}) Entrou na sala!')

nome = prompt('Degite seu nome: ')
ws = websocket.WebSocket(
    f'ws://{window.location.host}/ws/duplex/{nome}'
)

ws.bind('message', on_message)
ws.bind('open', on_open)