import psutil 
import requests


MEMORY_THRESHOLD = 80

API_ENDPOINT = ""

print(psutil.virtual_memory().percent)

def check_memory_usage():
    mem = psutil.virtual_memory()
    if mem.percent > MEMORY_THRESHOLD:
        send_alarm(mem.percent)


def send_alarm(usage):
    payload = {
        "message" f"Memory usage exceeded! Currently using {usage}% of available memory."
    }
    response = requests.post(API_ENDPOINT, json=payload)
    if response.status_code == 200:
        print("Alarm sent succesfully!")
    else:
        print(f"Failed to send alarm! Server responded with: {response.text}")


# if __name__ == "__main__":
#     check_memory_usage()