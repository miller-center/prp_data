class Node(object):

    def __init__(self, nid, title, president, date, text, participants):
        self.nid = nid
        self.title = title
        self.president = president
        self.date = date
        self.text = text
        self.participants = participants

    def get_all_text(self):
        return ' '.join(self.text)
