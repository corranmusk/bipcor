from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link

nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'BIPCOR',
#        Subgroup(
#            'Hosts',
#            View('List Hosts', 'main.hosts'),
#            View('Add Host', 'main.addhost'),
#        ),
#        Subgroup(
#            'Contacts',
#            View('List Contacts', 'main.contacts'),
#            View('Add Contact', 'main.addcontact'),
#            View('List Contact Groups','main.contactgroups')
#        ),
#        Subgroup(
#            'Config',
#            View('Show config status','configuration.checkconfig'),
#        ),
    )
