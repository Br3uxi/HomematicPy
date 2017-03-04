# HomematicPython
Easy Python Libary for HomeMatic Systems
## Installing
```shell
pip install git+https://github.com/Breuxi/HomematicPy.git
```
## Examples (examples/example.py)

### Login
```python
session_id = Homematic.login(homematic_ip, "API", "api")
print(session_id)
```

### Get Devices
```python
devices = Homematic.getDevices(homematic_ip, session_id, "BidCos-RF")
print(json.dumps(devices, sort_keys=True, indent=4))
```
### Set Value
```python
value_set = Homematic.setValue(homematic_ip, session_id, "BidCos-RF", "NEQ0153210:1", "STATE", "boolean", "0")
if value_set:
    print("Value STATE was set to 0")
else:
    print("Cant set Value STATE to 0")
```
### List Methods
```python
print(Homematic.listMethods(homematic_ip))
print(Homematic.getValue(homematic_ip, session_id, "BidCos-RF", "NEQ0153210:1", "STATE"))
```

### Log out
```python
logout = Homematic.logout(homematic_ip, session_id)
if logout:
    print("Successfully logged out!")
else:
    print("Log out failed")
```
