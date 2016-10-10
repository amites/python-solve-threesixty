import base64
import httplib
import json
import logging

try:
    from django.conf import settings
except ImportError:
    import settings


###########
# Utility #
###########

def clearEmpties(d):
    """
    Removes empty values from a dict.
    """
    return dict([(k, v) for k, v in d.items() if v and len(v) > 0])

logger = logging.getLogger('solve_threesixty')


#############
# API Class #
#############

class Solve360:
    def __init__(self, **kwargs):
        self.server = kwargs.get('server', settings.SOLVE360_SERVER)
        self.user = kwargs.get('user', settings.SOLVE360_USER)
        self.password = kwargs.get('password', settings.SOLVE360_PASS)
        self.owner = kwargs.get('owner', settings.SOLVE360_OWNERID)
        self.connection = None

    def connect(self, verb, uri, body='', data_type='json'):
        """
        Base connector class to Solve360.
        """
        if verb not in ('GET', 'POST', 'PUT', 'DELETE'):
            logger.error('Invalid verb for Solve360 {}'.format(verb))
            return False

        if data_type not in ('json', 'xml'):
            logger.error('Invalid data type for Solve360 {}'.format(verb))
            return False

        headers = {
            'Authorization': 'Basic {}'.format(
                base64.encodestring(
                    ":".join([self.user, self.password]).encode(
                        'utf-8')).replace('\n', '')),
            'Content-Type': 'application/{}'.format(data_type),
            'Accept': 'application/{}'.format(data_type),
        }

        self.connection = httplib.HTTPSConnection(self.server)
        if settings.DEBUG:
            self.connection.set_debuglevel(1)
        self.connection.request(verb, uri, body, headers)
        response = self.connection.getresponse()
        if response.status not in (200, 201):
            logger.error(
                'Unable to post to Solve360 at {} - {}:{}\nPayload: {}'.format(
                    uri, response.status, response.reason, body))
        else:
            return response.read()

    def connect_json(self, verb, uri, body_dict):
        """
        Base Connector class to Solve360 with data payload.
        """
        payload = self.connect(
            verb, uri, json.dumps(clearEmpties(body_dict),
                                  separators=(',', ':')), data_type='json')
        self.close()
        return payload

    def close(self):
        if self.connection:
            self.connection.close()

    def contact_show(self, contact_id):
        """
        Returns raw response of all fields for contact.
        """
        payload = self.connect('GET', '/contacts/{}'.format(contact_id))
        self.close()
        return payload

    def contact_list(self, data):
        """
        Searches for contacts using kwargs to search.
        See http://norada.com/norada/crm/external_api_reference_contacts
        for available search arguments.
        Returns raw response.
        """
        payload = self.connect_json('GET', '/contacts', data)
        self.close()
        return payload

    def contact_delete(self, contact_id):
        """
        Deletes a contact by ID.
        """
        payload = self.connect('DELETE', '/contacts/{}'.format(contact_id))
        self.close()
        return payload

    def category_list(self):
        """
        Returns raw response of Categories available.
        """
        payload = self.connect('GET', '/contacts/categories/')
        self.close()
        return payload

    def field_list(self):
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
            fields[j['name']] = label
        return fields

    def ownership_list(self):
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
            uri = '/report/{}'.format(uri)
        if len(kwargs) > 0:
            uri += '?'
            for key in kwargs:
                uri += '{}={}&'.format(key, kwargs[key])
            uri = uri[:-1]
        payload = self.connect('GET', uri)
        self.close()
        return payload

    def opportunity_list(self, **kwargs):
        return self.report('opportunities', **kwargs)

    def opportunity_add(self, **kwargs):
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
                    raise Exception(
                        'Invalid valuecurrency must be one of: {}'.format(
                            ', '.join(values)))
            elif key == 'valueinterval':
                values = ['fixed price', 'per hour', 'per day', 'per week',
                          'per month', 'per quarter', 'per month',
                          'per quarter', 'per year', ]
                if kwargs[key] not in values:
                    raise Exception(
                        'Invalid valueinterval must be one of: {}'.format(
                            ', '.join(values)))
            elif key == 'status':
                values = ['Discussion', 'Pending', 'Won', 'Lost', 'On-hold', ]
                if kwargs[key] not in values:
                    raise Exception('Invalid status must be one of: {}'.format(
                        ', '.join(values)))

            body[key] = kwargs[key]
        response = self.connect_json('POST', '/opportunity', body)
        return response
