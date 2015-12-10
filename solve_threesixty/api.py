import base64
import httplib
import logging
#import string
try:
    import simplejson as json
except ImportError:
    import json

try:
    from django.conf import settings
except ImportError:
    import settings

try:
    from general.utils_dict import clearEmpties
except ImportError:
    def clearEmpties(d):
        """
        Removes empty values from a dict.
        """
        return {k: v for k, v in d.items() if v and len(v) > 0}

logger = logging.getLogger('solve_threesixty')


class Solve360:
    def __init__(self, **kwargs):
        self.server = kwargs.get('server', settings.SOLVE360_SERVER)
        self.user = kwargs.get('user', settings.SOLVE360_USER)
        self.password = kwargs.get('password', settings.SOLVE360_PASS)
        self.owner = kwargs.get('owner', settings.SOLVE360_OWNERID)
        self.connection = False

    #noinspection PyDictCreation,PyDictCreation
    def connect(self, verb, uri, body='', type='json'):
        """
        Base connector class to Solve360.
        """
        if not verb in ['GET', 'POST', 'PUT', 'DELETE']:
            logger.error('Invalid verb for Solve360 %s' % verb)
            return False

        if not type in ['json', 'xml']:
            logger.error('Invalid data type for Solve360 %s' % verb)
            return False

        headers = {
            'Authorization': 'Basic %s' %
                 base64.encodestring(":".join(
                        [self.user, self.password]
                    ).encode('utf-8')).replace('\n', ''),
        }

        headers['Content-Type'] = 'application/%s' % type
        headers['Accept'] = 'application/%s' % type

        self.connection = httplib.HTTPSConnection(self.server)
        if settings.DEBUG:
            self.connection.set_debuglevel(1)
        self.connection.request(verb, uri, body, headers)
        response = self.connection.getresponse()
        if not response.status in (200, 201):
            logger.error('Unable to post to Solve360 at %s -' \
                            + '%s:%s\nPayload: %s'
                            % (uri, response.status, response.reason, body))
        else:
#            self.connection.close()
            return response.read()

    def connectJSON(self, verb, uri, body_dict):
        """
        Connects to Solve360 using JSON passing body_dict for arguments.
        """
        payload = self.connect(verb, uri, json.dumps(clearEmpties(body_dict),
            separators=(',', ':')), type='json')
        self.close()
        return payload

    def close(self):
        if self.connection:
            self.connection.close()

    def contactShow(self, contact_id):
        """
        Returns raw response of all fields for contact.
        """
        payload = self.connect('GET', '/contacts/%s' % contact_id)
        self.close()
        return payload

    def contactList(self, kwargs):
        """
        Searches for contacts using kwargs to search.
        See http://norada.com/norada/crm/external_api_reference_contacts
        for available search arguments.
        Returns raw response.
        """
        payload = self.connectJSON('GET', '/contacts', kwargs)
        self.close()
        return payload

    def contactDelete(self, contact_id):
        """
        Deletes a contact by ID.
        """
        payload = self.connect('DELETE', '/contacts/%s' % contact_id)
        self.close()
        return payload

    def categoryList(self):
        """
        Returns raw response of Categories available.
        """
        payload = self.connect('GET', '/contacts/categories/')
        self.close()
        return payload

    def fieldsList(self):
        """
        Returns a dict of { field_name : field_title }
        for all fields in account.
        """
        payload = self.connect('GET', '/contacts/fields/')
        self.close()
        fields = {}
        for j in payload['fields']:
            try:
                label = json.loads(j['label'])
                if isinstance(label, dict):
                    label = label['title']
            except ValueError:
                label = j['label']
#            print '%s : %s' % (label, j['name'])
            fields[j['name']] = label
#        return payload
        return fields

    def ownershipList(self):
        """
        Returns raw response of Contact Owners.
        """
        payload = self.connect('GET', '/ownership/')
        self.close()
        return payload

    def report(self, uri, **kwargs):
        """
        Basic report processing sub-function.
        Refer to http://bit.ly/solve360-api-reports
        """
        if uri[0] != '/':
            uri = '/report/%s' % uri
        if len(kwargs) > 0:
            uri += '?'
            for key in kwargs:
                uri += '%s=%s&' % (key, kwargs[key])
            uri = uri[:-1]
        payload = self.connect('GET', uri)
        self.close()
        return payload

    def opportunityList(self, **kwargs):
        """
        Returns a list of opportunities based on kwargs filters.
        """
        return self.report('opportunities', **kwargs)

    def opportunityAdd(self, **kwargs):
        """
        Simple add opportunity function, checks for valid values for required
        string fields.
        Refer to http://bit.ly/solve360-api-contact
        """
        body = {}
        for key in kwargs:
            if key == 'valuecurrency':
                values = ['USD', 'EUR', 'GBP', 'CAD', 'AUD', 'BRL', 'CHF',
                          'CNY', 'DKK', 'HKD', 'HRK', 'HUF', 'INR', 'JPY',
                          'MXN', 'MYR', 'NOK', 'NZD', 'RUB', 'SEK', 'SGD',
                          'THB', 'ZAR', ]
                if kwargs[key] not in values:
                    raise Exception('Invalid valuecurrency must be one of: %s'\
                                        % ', '.join(values))
            elif key == 'valueinterval':
                values = ['fixed price', 'per hour', 'per day', 'per week',
                          'per month', 'per quarter', 'per month',
                          'per quarter', 'per year', ]
                if kwargs[key] not in values:
                    raise Exception('Invalid valueinterval must be one of: %s'\
                                        % ', '.join(values))
            elif key == 'status':
                values = ['Discussion', 'Pending', 'Won', 'Lost', 'On-hold', ]
                if kwargs[key] not in values:
                    raise Exception('Invalid status must be one of: %s'\
                                        % ', '.join(values))

            body[key] = kwargs[key]
        response = self.connectJSON('POST', '/opportunity', body)
        return response
