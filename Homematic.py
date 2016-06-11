import requests
import json


# Login
def login(homematic_ip, username, password):
    """
        :param homematic_ip: The IP of the Homematic
        :param username: The Username of the preferred User
        :param password: The Passwird of the preferred User
        :type homematic_ip: str
        :type username: str
        :type password: str
        :returns Session ID for the other functions
        :rtype str
    """
    data = {'method': 'Session.login', 'params': {'username': username, 'password': password}}
    headers = {'Content-type': 'application/json;charset=utf-8'}
    r = requests.post("http://" + homematic_ip + "/api/homematic.cgi", data=json.dumps(data), headers=headers)

    the_json = r.json()

    return the_json['result']


def getDevices(homematic_ip, session_id, interface):
    """
        :param homematic_ip: The IP of the Homematic
        :param session_id: The Session ID from the Login Method
        :param interface: the interface you want to connect
        :type homematic_ip: str
        :type session_id: str
        :type interface: str
        :returns Details registered Devices
        :rtype json
    """
    data = {'method': 'Device.listAllDetail', 'params': {'_session_id_': session_id, 'interface': interface}}
    headers = {'Content-type': 'application/json;charset=utf-8'}
    r = requests.post("http://" + homematic_ip + "/api/homematic.cgi", data=json.dumps(data), headers=headers)

    return r.json()


def setValue(homematic_ip, session_id, interface, address, valueKey, type, value):
    """
        :param homematic_ip: The IP of the Homematic
        :param session_id: The Session ID from the Login Method
        :param interface: the interface you want to connect
        :param address: the address of the device with the value you want to set
        :param valueKey: the value of the key you want to set
        :param type: the value type
        :param value: the value you want to set
        :type homematic_ip: str
        :type session_id: str
        :type interface: str
        :type address: str
        :type valueKey: str
        :type type: str
        :type value: str
        :rtype bool
    """

    data = {'method': 'Interface.setValue',
            'params': {
                '_session_id_': session_id,
                'interface': interface,
                'address': address,
                'valueKey': valueKey,
                'type': type,
                "value": value
            }
            }

    headers = {'Content-type': 'application/json;charset=utf-8'}
    r = requests.post("http://" + homematic_ip + "/api/homematic.cgi", data=json.dumps(data), headers=headers)
    return r.json()['result']


# BidCos-RF

def listMethods(homematic_ip):
    """
        :param homematic_ip: The IP of the Homematic
        :type homematic_ip: str
        :rtype json
    """

    data = {'method': 'system.listMethods',
            'params': ''
            }
    headers = {'Content-type': 'application/json;charset=utf-8'}
    r = requests.post("http://" + homematic_ip + "/api/homematic.cgi", data=json.dumps(data), headers=headers)

    return r.json()


# Logout
def logout(homematic_ip, session_id):
    """
        :param homematic_ip: The IP of the Homematic
        :type homematic_ip: str
        :rtype boolean
    """
    data = {'method': 'Session.logout', 'params': {'_session_id_': session_id}}
    headers = {'Content-type': 'application/json;charset=utf-8'}
    r = requests.post("http://" + homematic_ip + "/api/homematic.cgi", data=json.dumps(data), headers=headers)

    return r.json()['result']
