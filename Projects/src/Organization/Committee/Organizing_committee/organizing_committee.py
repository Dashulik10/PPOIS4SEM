from Projects.src.Organization.Committee.Program_committee.basic_program_committee import *
from Projects.src.Organization.Committee.Organizing_committee.venue import Venue
from Projects.src.Person.Organizer.organizer import *

class OrganizingCommittee(BasicCommittee):

    _venue: Venue

    def __init__(self, *, name, email, members, chairman, venue: Venue):
        if not hasattr(self, '_venue_initialized'):
            super().__init__(
                name=name,
                email=email,
                members=members,
                chairman=chairman
            )
            self.venue = venue
            self._venue_initialized = True

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        self._venue = venue

    def print_chairman_info(self):
        if self.chairman:
            print("Председатель организационного комитета: ")
            print(self.chairman)


    def get_member_details(self):
        if not self.members:
            print("В комитете пока нет участников.")
        else:
            print("Информация по всем участникам организационного комитета:")
            for idx, member in enumerate(self.members, 1):
                print(f"{idx}. {member}")

    def add_member(self, member):
        if member not in self._members:
            self._members.add(member)

    def __str__(self):
        return (f"Организационный комитет:\n"
                f"Председатель: {self.chairman}\n"
                f"Количество членов: {len(self.members)}")

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "members": [member.to_dict() for member in self.members],
            "chairman": self.chairman.to_dict() if self.chairman else None,
            "venue": self.venue.to_dict(),
        }

    @classmethod
    def from_dict(cls, data):
        venue = Venue.from_dict(data["venue"]) if "venue" in data else None
        committee = cls(
            name=data["name"],
            email=data["email"],
            members=set(),
            chairman=Person.from_dict(data["chairman"]) if data.get("chairman") else None,
            venue=venue
        )
        # Восстановление участников
        if "members" in data:
            for member_data in data["members"]:
                member = Organizer.from_dict(member_data)
                committee.members.add(member)
                return committee