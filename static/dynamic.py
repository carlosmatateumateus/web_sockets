from browser import ajax, bind, document, html

def on_complete(req):
    document['my-div'] <= html.P(req.text)

@bind('#btn', 'click')
def click_btn(evt):
    ajax.get('/dynamic/data', oncomplete=on_complete)