import subprocess,json,os


 
"""
def get_node_grid_addresses():

	try:
		node_network = os.popen("sudo docker inspect zalenium").read()#.decode("utf-8")
		driver_port = "".join([x.split("=")[1] for x in  json.loads(node_network)[0]['Config']['Env'] if x.split("=")[0] == "NODE_PORT" ])
		network_name = os.popen("sudo docker network ls").read().split("\n")[1].split()[1]
		network_json = os.popen("sudo docker network inspect " + network_name).read().strip()
		network_containers = json.loads(network_json)[0]["Containers"]

		nodes_addresses = {}

		for network_container in network_containers.items():
			node_address = network_container[1]['IPv4Address'].split("/")[0]
			node_name    = network_container[1]['Name']
			try:
				node_index   = int(node_name.split("_")[-1])
				nodes_addresses[node_index] = node_address + ":" + driver_port 
			except ValueError:
				pass
		return nodes_addresses

	except IndexError:
		return {}
"""
	

def get_node_zal_addresses():
	driver_addresses = []
	number_of_browsers = os.popen("sudo docker container ls").read().count("elgalu/selenium:latest")
	for container_number in range(1,number_of_browsers+1):
		container_name = os.popen("sudo docker container ls").read().split("\n")[container_number].split()[-1]
		container_json = os.popen("sudo docker container inspect " + container_name).read()
		container_json_loaded = json.loads(container_json)[0]
		ip_address = container_json_loaded["NetworkSettings"]["IPAddress"]
		driver_port = "".join([x.split("=")[1] for x in  container_json_loaded['Config']['Env'] if x.split("=")[0] == "SELENIUM_MULTINODE_PORT" ])
		full_address = "{0}:{1}".format(ip_address,driver_port)
		driver_addresses.append(full_address)
	return driver_addresses

print(get_node_zal_addresses())
		

		

		







