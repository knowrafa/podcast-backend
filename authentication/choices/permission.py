from django.utils.translation import ugettext_lazy as _


class PermissionChoices:

    @staticmethod
    def acess():
        """
        Define you own acesses here.
        :return: Tuple's list with acesses keys and values.
        """
        return (
            ('admin', _('Administrator')),
            ('doctor', _('Doctor')),
            ('nurse', _('Nurse')),
            ('manager', _('Manager')),
            ('coordinator', _('Coordinator')),
            ('guest', _('Guest')),
        )

    @staticmethod
    def acess_level():
        """
        Define you own acess levels here
        :return: Tuple's list with acess level keys and values
        """
        return (
            ('r', _('Read Only')),
            ('rw', _('Read and Write')),
            ('rwd', _('Read, Write and Delete')),
        )