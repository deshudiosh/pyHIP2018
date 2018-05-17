class Project(object):
    def __init__(self, name: str, url: str, times_to_vote: int):
        self._name = name
        self._url = url
        self._times_to_vote = times_to_vote

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def times_to_vote(self):
        return self._times_to_vote

    @times_to_vote.setter
    def times_to_vote(self, value):
        self._times_to_vote = value

