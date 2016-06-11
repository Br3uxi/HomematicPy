import Homematic

homematic_ip = "192.168.0.4"

# Login
session_id = Homematic.login(homematic_ip, "API", "api")
print(session_id)

# GetDevices
devices = Homematic.getDevices(homematic_ip, session_id, "BidCos-RF")
print(devices)

# Set Value
value_set = Homematic.setValue(homematic_ip, session_id, "BidCos-RF", "NEQ0153210:1", "STATE", "boolean", "0")
if value_set:
    print("Value STATE was set to 0")
else:
    print("Cant set Value STATE to 0")

# List methods
print(Homematic.listMethods(homematic_ip))

print(Homematic.getValue(homematic_ip, session_id, "BidCos-RF", "NEQ0153210:1", "STATE"))

# Log out
logout = Homematic.logout(homematic_ip, session_id)
if logout:
    print("Successfully logged out!")
else:
    print("Log out failed")
