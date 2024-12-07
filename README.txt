As an engineer I’d like to understand what ports are accessible on a given host to ensure that firewall rules have been applied correctly while debugging. 
I’d also like to understand the history of that host to see if anything has recently changed.

Technical details:
Given a webpage with a blank text box
When a user types in an ip or hostname
Then an NMAP scan is done (using the NMAP command line tool) against ports 0-1000 which returns the open ports back the UI page for that host
 
Given a webpage with a blank text box
When a user types in an invalid ip or hostname
Then an error message should appear asking the user to re-submit
 
Given a webpage with a blank text box 
When a user types in an ip or hostname
Then the results of the latest scan appear as well as the history of previous scans for that host
 
Given a user submitting an ip or hostname into the textbox
When ports are different from the previous query
Then a list of ports that have been added and/or subtracted will be visible to the user for example if port 80 is open now but wasn’t open on the previous run that should be called out
 
Given a user looking to interact with this project as a webservice
When an HTTP call is made to a specified endpoint
Then the history of an ip address or hostname is returned in a JSON format


How to use:

-Start flask, set app to app.py
-Open the app on localhost port 5000.
-Follow instructions and type in domains.
	-Only one domain per line
-Return will contain host, open ports, past ports, 
and newly closed and opened ports from a previous scan.
