import subprocess,json

network_name = subprocess.check_output("sudo docker network ls",shell=1).decode("utf-8").split("\n")[1].split()[1]
network_json = subprocess.check_output("sudo docker network inspect " + network_name,shell=1).decode("utf-8").strip()
network_containers = json.loads(network_json)[0]["Containers"]

nodes_addresses = {}
port_number = str(4444)

for network_container in network_containers.items():
	node_address = network_container[1]['IPv4Address'].split("/")[0]
	node_name    = network_container[1]['Name']
	try:
		node_index   = int(node_name.split("_")[-1])
		nodes_addresses[node_index] = node_address + ":" + port_number 
	except ValueError:
		pass
	

print(nodes_addresses)


		

		







