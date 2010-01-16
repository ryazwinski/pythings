'''
A simple module to wrapper the Withings.com REST api
'''

import simplejson
import urllib2

class BodyScale(Object):
    '''Class that implements communication with the Withings REST service.'''
    def __init__(self, host='wbsapi.withings.net', port=80,
            proxyhost='', proxyport=80):
        '''Setup communications defaults for the session

        Optional:
            host - service http host
            port - service http port
            proxyhost - if not '' is the host to proxy http through
            proxyport - if proxyhost is set, this is the http proxy port
        '''
        pass
    
    def get_measurements(self, user, key, startdate, enddate, meastype,
            lastupdate, category, limit, offset):
        '''Implements the withings getmeas method

        Required:
            user - the withings integer userid
            key - the sharing key for this user

        Optional:
            startdate - epoch format - retreive entries after this date
            enddate - epoch format - retrieve entries before this date
            meastype - integer - the type of data to receive
            lastupdate - epoch format - the last sync date - only get
                         updates since then)
            category - BodyScale.CAT_OBJECTIVE or BodyScale.CAT_MEASURES
            limit - limit the number of responses to limit
            offset - combined with limit to page through large datasets,
                     offset skips 'offset' elements from the newest backwards

        '''
        pass

    def get_user_info(self, user, key):
        '''Implements the withings getbyuserid method

        This service will return an array containing information regarding
        the specified user.
        This can be used to retrive a user's firstname, lastname, gender,
        or birthdate. 

        Required:
            user - the withings integer userid
            key - the sharing key for this user
        '''
        import hashlib

        '''calculate the hash for the password we'll post'''
        '''see http://www.withings.com/en/api/bodyscale#crypto'''

        pass

    def get_users_list(self, email, password):
        '''Implements the withings getuserslist method

        This service can be used to retreive a user's publickey and userid
        using the email and password combination of a Withings account.

        This service is useful in case the user's data sharing has to be
        activated from a third party web site. It allows all operations to
        be performed from this remote web site without forcing the user to
        actually open a session at my.withings.com. The use of this service
        is an option. The other option available for the user to perform the
        same task is to use the 'Share' overlay of the dashboard and have
        the user send an email to the third party application as explained 
        at http://www.withings.com/en/api/bodyscale#email.

        Using this service necessitates that the user trusts your website
        enough to enter their Withings account password.
        
        Please don't store it. 

        Required:
            email - the user's my.withings.com email address
            password - the user's my.withings.com password
        '''

        pass

    def update(self, email, key, isPublic):
        '''Implements the withings update method

        For a user's data to be accessible through this API, a prior
        authorization has to be given. This can be done directly from the
        'Share' overlay of the user Dashboard, or through the update() method.

        Please note that setting the ispublic to False automatically changes
        the publickey of the user to a new random value. 

        Required:
            userid - integer withings userid
            key - public key associated with the userid
            isPublic - True or False.  Settings to False disables sharing.
        '''
        pass

    def subscribe(self, userid, key, url):
        '''Implements the withings subscribe method

        This service allows third parties to subscribe to notifications.
        Once the notification service has been subscribed, the WBS API will
        notify the subscriber whenever the target user's measurements or
        objectives are added, modified or deleted.

        This allows third party applications to remain in sync with user's
        data.

        To monitor a user, its userid and publickey are needed. Please note
        that unless the subscribed users have made their measurements data
        public, no notifications will be sent (see user/update on how to
        enable it).

        Required:
            userid - withing integer userid
            key - public key matched with the userid
            url - the callback url withings will post updates to

            WBS API notification are merely HTTP POST requests to this URL
            (such as http://www.yourdomain.net/yourCustomApplication.php \
                    ?userid=123456&startdate=1260350649&enddate=1260350650
            Those requests contain startdate and enddate parameters (both
            are integers in EPOCH format) and the userid it refers to. It
            is up to the targeted system to issue a measure/getmeas request
            using both figures to retrieve updated data.
        '''

        pass

    def revoke(self, userid, key, url):
        '''Implements the withings revoke method

        This service allows third party applications to revoke a previously
        subscribed notification.

        This will disable the push feature between the WBS API and the
        specified applications for the specified user.

        Required:
            userid - integer withings userid of the target user
            key - public key for this userid
            url - the callback url to unsubscribe
        '''
        pass

    def check_sub(self, userid, key, url):
        '''Implements the withings get method

        This service allows third party applications to check whether the
        notification service was previously subscribed on a specific user
        and to retrieve the subscription expiry date.

        Required:
            userid - integer withings userid of the target user
            key - public key for this userid
            url - the callback url to check
        '''
