import json

class Job:
    def __init__(self) -> None:
        self.title = ""
        self.text = ""
        self.link = ""
        self.img = ""

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text = text

    def set_link(self, link):
        self.link = link
    def set_img(self, img):
        self.img = img

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

