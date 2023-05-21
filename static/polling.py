from browser import ajax, document, html, timer

def on_complete(req):
    document['my-div'] <= html.P(req.text)

def make_request():
    ajax.get('/dynamic/data', oncomplete=on_complete)
    timer.set_timeout(make_request, 5000)


make_request()