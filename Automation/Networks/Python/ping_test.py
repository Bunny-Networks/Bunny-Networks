import subprocess

def ping_device(host):
    try:
        # Ping the host once and capture the output
        output = subprocess.check_output(["ping", "-c", "1", host], universal_newlines=True)
        
        # Check if the ping was successful
        if "1 packets transmitted, 1 received" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def main():
    # Replace '192.168.1.1' with the IP address or hostname you want to ping
    host = "8.8.8.8"
    
    # Ping the device
    if ping_device(host):
        print(f"Ping to {host} was successful!")
        # Do something on success
        # For example, continue with the script or execute some logic
    else:
        print(f"Ping to {host} failed.")
        # Do something on failure
        # For example, retry, alert the user, or exit

if __name__ == "__main__":
    main()

