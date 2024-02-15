'''
import subprocess

result = subprocess.run(['wmic', 'diskdrive', 'get', 'serialnumber'], capture_output=True, text=True)
output = result.stdout.strip()

print(output)













# Function To Convert The Hash [256] Using Hex.
# Get Hardware Information [CPU Info + MAC Address + Hard Disk serial]
# Generate Unique ID

import hashlib
import platform
import psutil
import subprocess

def get_cpu_info():
    # Get processor information using platform module
    cpu_info = platform.processor()
    return f"CPU: {cpu_info}"

def get_mac_address():
    # Find the first available network interface and get its MAC address
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                # Convert each character to its ASCII value and then to an integer
                mac_integers = [int(ord(char)) for char in addr.address]
                # Use the converted integers with hex
                return ":".join(hex(i)[2:].zfill(2) for i in mac_integers)
    
    # Return a default value if no suitable network interface is found
    return "00:00:00:00:00:00"

def get_hardware_info():
    # Gather hardware information (you can customize this based on your requirements)
    cpu_info = get_cpu_info()
    mac_address = get_mac_address()
    disk_serial = subprocess.run(['wmic', 'diskdrive', 'get', 'serialnumber'], capture_output=True, text=True)
    # Extract the stdout attribute
    output = disk_serial.stdout.strip()

    # Combine hardware information into a string
    hardware_info_str = f"{cpu_info}{mac_address}{output}"

    return hardware_info_str

def generate_unique_id():
    # Get hardware information
    hardware_info = get_hardware_info()

    # Hash the hardware information to create a unique identifier
    unique_id = hashlib.sha256(hardware_info.encode()).hexdigest()

    return unique_id

# Example usage
unique_id = generate_unique_id()
print(f"Unique ID based on hardware information: {unique_id}")




# Function To Convert The Hash [256] To Uppercase And Formatted Into Groups Of Five Characters Separated By Hyphens
# Get Hardware Information [CPU Info + MAC Address + Hard Disk serial]
# Generate Unique ID


import hashlib
import platform
import psutil
import subprocess

def get_cpu_info():
    # Get processor information using the platform module
    cpu_info = platform.processor()
    return f"CPU: {cpu_info}"

def get_mac_address():
    # Find the first available network interface and get its MAC address
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                # Convert each character to its ASCII value and then to an integer
                mac_integers = [int(ord(char)) for char in addr.address]
                # Use the converted integers with hex
                return ":".join(hex(i)[2:].zfill(2) for i in mac_integers)
    
    # Return a default value if no suitable network interface is found
    return "00:00:00:00:00:00"

def get_hardware_info():
    # Gather hardware information (you can customize this based on your requirements)
    cpu_info = get_cpu_info()
    mac_address = get_mac_address()
    disk_serial = subprocess.run(['wmic', 'diskdrive', 'get', 'serialnumber'], capture_output=True, text=True)
    # Extract the stdout attribute
    output = disk_serial.stdout.strip()

    # Combine hardware information into a string
    hardware_info_str = f"{cpu_info}{mac_address}{output}"

    return hardware_info_str

def generate_unique_id():
    # Get hardware information
    hardware_info = get_hardware_info()

    # Hash the hardware information to create a unique identifier
    unique_id = hashlib.sha256(hardware_info.encode()).hexdigest().upper()

    # Format the hash into a readable pattern
    formatted_id = '-'.join([unique_id[i:i+5] for i in range(0, len(unique_id), 5)])

    return formatted_id

# Example usage
unique_id = generate_unique_id()
print(f"Unique ID based on hardware information: {unique_id}")















'''


# Function To Convert The Hash [1] To Uppercase And Format Using A Shorter Hash Function
# Get Hardware Information [CPU Info + MAC Address + Hard Disk serial]
# Generate Unique ID


import hashlib
import platform
import psutil
import subprocess

def get_cpu_info():
    # Get processor information using the platform module
    cpu_info = platform.processor()
    return f"CPU: {cpu_info}"

def get_mac_address():
    # Find the first available network interface and get its MAC address
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                # Convert each character to its ASCII value and then to an integer
                mac_integers = [int(ord(char)) for char in addr.address]
                # Use the converted integers with hex
                return ":".join(hex(i)[2:].zfill(2) for i in mac_integers)
    
    # Return a default value if no suitable network interface is found
    return "00:00:00:00:00:00"

def get_hardware_info():
    # Gather hardware information (you can customize this based on your requirements)
    cpu_info = get_cpu_info()
    mac_address = get_mac_address()
    disk_serial = subprocess.run(['wmic', 'diskdrive', 'get', 'serialnumber'], capture_output=True, text=True)
    # Extract the stdout attribute
    output = disk_serial.stdout.strip()

    # Combine hardware information into a string
    hardware_info_str = f"{cpu_info}{mac_address}{output}"

    return hardware_info_str

def generate_unique_id():
    # Get hardware information
    hardware_info = get_hardware_info()

    # Hash the hardware information to create a unique identifier
    unique_id = hashlib.sha1(hardware_info.encode()).hexdigest().upper()

    # Format the hash into a readable pattern
    formatted_id = '-'.join([unique_id[i:i+5] for i in range(0, len(unique_id), 5)])

    return formatted_id

# Example usage
unique_id = generate_unique_id()
print(f"Unique ID based on hardware information: {unique_id}")

