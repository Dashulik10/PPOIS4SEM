from Projects.src.Person.person import *


class BasicCommittee:
    _name: str
    _email: str
    _members: set

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BasicCommittee, cls).__new__(cls)
        return cls._instance

    def __init__(self, *, name, email, members, chairman):
        if not hasattr(self, '_initialized'):
            self._name = name
            self._email = email
            self._members = members
            self._chairman = chairman
            self._initialized = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name is too long")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if "@" in email:
            self._email = email

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        if isinstance(members, set):
            self._members = members
        else:
            raise ValueError("Members is not a set")

    @property
    def chairman(self):
        return self._chairman

    @chairman.setter
    def chairman(self, chairman):
        if chairman not in self._members:
            self._members.add(chairman)
        self._chairman = chairman
        self._members.add(chairman)

