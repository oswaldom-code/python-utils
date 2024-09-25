import docker
import json
import csv

client = docker.from_env()

def bytes_to_mb(bytes_value):
    return round(bytes_value / (1024 ** 2), 2)

def bytes_to_gb(bytes_value):
    return round(bytes_value / (1024 ** 3), 2)

def get_container_info():
    containers_info = []
    containers = client.containers.list()
    
    for container in containers:
        info = container.attrs
        
        stats = container.stats(stream=False)
        
        container_info = {
            "Name": info['Name'],
            "Image": info['Config']['Image'],
            "IP": info['NetworkSettings']['IPAddress'],
            "Ports": info['NetworkSettings']['Ports'],
            "Volumes": info['Mounts'],
            "Networks": list(info['NetworkSettings']['Networks'].keys()),
            "CPU Usage": f"{stats['cpu_stats']['cpu_usage']['total_usage'] / 1_000_000:.2f} MCPU",
            "Memory Usage (MB)": bytes_to_mb(stats['memory_stats'].get('usage', 0)), 
        }
        containers_info.append(container_info)
    
    return containers_info

def export_to_json(data, filename='container_info.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename='container_info.csv'):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

if __name__ == "__main__":
    info = get_container_info()
    export_to_json(info)
    export_to_csv(info)
    print(f"Exported container information to JSON and CSV.")
