# Example Web Application that accesses basic profile a #LinkedIn user using OAUTH2.0 and python3-linkedin API

# imports
import os.path
import json
import io

# import CherryPy
import cherrypy

# import the python3-linkedin api wrapper
from linkedin import linkedin
from linkedin import server


# Authorize the web application user to access LinkedIn services using OAuth2
applicationKey = "86rw6lgdullx2c"
applicationSecret = " w6LuKO9AXCCBd3Q6"

retURL = "https://etion.be/blablabla.php"
authentication = linkedin.LinkedInAuthentication(
    applicationKey,
    applicationSecret,
    retURL,
    [linkedin.PERMISSIONS.BASIC_PROFILE]
  )

# Get the authorization URL
authorizationURL = authentication.authorization_url

# Serves the LinkedIn authorization page
class LinkedInAuthorization:

    @cherrypy.expose
    def index(self):
        # redirect to LinkedIn authorization URL happens here
        raise cherrypy.HTTPRedirect(authorizationURL)


# Class for initial app home page and the post authorization app home page a.k.a return-URL

# The post authorization page displays the basic user profile as a JSON string
class HomeProfile:

    @cherrypy.expose
    def index(self, *args, **kwargs):
        content = io.StringIO()
        # Home page case - after authorization
        if len(kwargs) > 0:
            authCode = kwargs["code"]
            authentication.authorization_code = authCode
            token = authentication.get_access_token()
            application = linkedin.LinkedInApplication(
                token=token.access_token)
            basicProfile = application.get_profile()
            profileString = json.dumps(basicProfile)
            content.write(json.dumps(profileString, indent=4, sort_keys=True))
            output = content.getvalue()
            content.close()
            return [bytes(output, 'utf-8')]

        # Home page case - before authorization

        content.write('<html>')
        content.write('<head>')
        content.write('<title>')
        content.write(
            'Sample web application that gets LinkedIn access and prints basic user profile')
        content.write('</title>')
        content.write('</head>')
        content.write('<body>')
        content.write(
            '<h1>Sample web application that prints LinkedIn basic user profile using OAUTH 2.0</h1>')
        content.write(
            '<p>Sample web application that gets Linkedin authorization from the ')
        content.write('user and prints the basic user profile</p>')
        content.write('<form action="for_linkedin_access" method="post">')
        content.write(
            '<input type="submit" value="Authorize Sample Application for Linkedin Access">')
        content.write('</form>')
        content.write('</body>')
        output = content.getvalue()
        content.close()
        return [bytes(output, 'utf-8')]

conf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')
print()

if __name__ == '__main__':
    # cherrypy.tree.mount(HomeProfile(), '/', config=conf)
    cherrypy.tree.mount(HomeProfile(), '/')
    """ cherrypy.tree.mount(LinkedInAuthorization(),
                        '/for_linkedin_access', config=conf) """
    cherrypy.tree.mount(LinkedInAuthorization(),
                        '/for_linkedin_access')
    cherrypy.engine.start()
    cherrypy.engine.block()
