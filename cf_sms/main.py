import base64

def hello_pubsub(cloud_event):
    print(base64.b64decode(cloud_event.data["message"]["data"]))