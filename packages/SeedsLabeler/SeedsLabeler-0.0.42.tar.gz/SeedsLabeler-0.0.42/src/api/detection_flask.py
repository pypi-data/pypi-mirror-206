import requests
import json
import pickle
class FlaskClient(object):
    def __init__(self, host = 'localhost', project="Striga_Strat1", APItoken=""):
        self.host = host
        # self.port = port
        self.project = project
        self.APItoken = APItoken


    def processImageLabels(self, data):
        # print(data.text)
        data_json = json.loads(data.text)
        # return pickle.loads(data.text)
        boxes = []
        labels_words = []
        scores = []
        for rect in data_json["body"]["annotations"][0]["rects"]:
            # print(rect)
            r = [rect["rect"]["x"], rect["rect"]["y"], 
                 rect["rect"]["x"] +rect["rect"]["width"], rect["rect"]["y"] +rect["rect"]["height"]]
            boxes.append(r)
            labels_words.append(rect["labelName"])
            scores.append(1.0)

        return (boxes,labels_words,scores)
        # return (data_json['boxes'], data_json['labels_words'], data_json['scores'])


    def sendDetectionImage(self, image_path):
    #  '''sends image in bytes and gets JSON file'''
        try:
            print('Trying to send Image to server')
            if image_path is None:
                print('image path is none')
                return
            print('Read an image')
            
            # http://cloudlabeling:4000/api/predict
            if "cloudlabeling.org" in self.host:
                im = open(image_path, 'rb')
                image_bytes = im.read()
                x = requests.post(self.host, data=image_bytes, headers={
                                "content-type": "image/jpeg", "project_id": self.project, "api_token": self.APItoken})
                data_json = json.loads(x.text)
                return (data_json['boxes'], data_json['labels_words'], data_json['scores'])
            
            elif "thya" in self.host:
                url = self.host
                headers = {
                    'x-api-key': self.APItoken,
                }
                payload = {
                    'projectId': (None, self.project),
                    'images': (image_path, open(image_path, 'rb'))
                }
                print(url)
                print(headers)
                print(payload)
                x = requests.post(url, headers=headers, files=payload)
                # print(response.text)

                # print('Send a response')
                return self.processImageLabels(x)

        except Exception as e:
            print("Closed a thread for server", str(e))
            return None
