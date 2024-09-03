class Article:
    def __init__(self, name, link, upvote):
        self.name = name
        self.link = link
        self.upvote = int(upvote.split()[0])

