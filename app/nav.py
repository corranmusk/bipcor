from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link

nav = Nav()


@nav.navigation()
def mynavbar():
    return Navbar(
        "BIPCOR",
        Subgroup(
            "Reports",
            View("Summary", "main.summary"),
            View("List burrently banned", "main.currentlyBanned"),
            View("Add Report", "main.reportIPAddr"),
            View("All Reports", "main.allReports"),
        ),
        Subgroup(
            "Tokens",
            View("Generate Token", "main.generateToken"),
            View("List Tokens", "main.listTokens"),
            View("Summary", "main.tokenSummary"),
        ),
        Subgroup(
            "Log",
            View("Show Log", "main.showLog"),
            View("Add Entry", "main.addLogEntry"),
        )
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
