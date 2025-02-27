from Projects.src.Organization.Committee.committee import *

class BasicProgramCommittee(BasicCommittee):

    _topics: set

    def __init__(self, *, name, email, members, chairman, topics):
        if not hasattr(self, '_topics_initialized'):
            super().__init__(
                name=name,
                email=email,
                members=members,
                chairman=chairman
            )
            self._topics = topics
            self._topics_initialized = True

    @property
    def topics(self):
        return self._topics

    @topics.setter
    def topics(self, topics):
        if isinstance(topics, set) and topics:
            self._topics = topics
        else:
            raise ValueError("Темы должны быть заданным непустым множеством.")

    def is_topic_valid(self, topic: str):
        return topic in self._topics



