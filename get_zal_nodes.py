import subprocess,json,os

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
		

		

		







