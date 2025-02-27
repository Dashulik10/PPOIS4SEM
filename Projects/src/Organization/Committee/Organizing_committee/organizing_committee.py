from Projects.src.Organization.Committee.Program_committee.basic_program_committee import *
from Projects.src.Organization.Committee.Organizing_committee.venue import Venue

class OrganizingCommittee(BasicCommittee):

    _venue: Venue

    def __init__(self, *, name, email, members, chairman, venue):
        if not hasattr(self, '_venue_initialized'):
            super().__init__(
                name=name,
                email=email,
                members=members,
                chairman=chairman
            )
            self._venue = venue
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
