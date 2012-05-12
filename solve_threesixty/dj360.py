from solve_threesixty.api import Solve360
from solve_threesixty.models import *


class Django360(Solve360):
    def __init__(self, **kwargs):
        super(Django360, self).__init__(**kwargs)

    def getUsers(self):
        obj = self.ownershipList()
        if obj['status'] == 'success':
            for row in obj['groups']:
                grp = ThreeSixtyUser()
                grp.addUser(row, True)
            for row in obj['users']:
                usr = ThreeSixtyUser()
                usr.addUser(row, False)

    def getContactFields(self):
        obj = self.contactFieldsList()
        for row in obj:
            field = ThreeSixtyField()
            field.addField(row)