from os import wait
import speedtest 
import time

test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers() # get list of servers
print("Choosing best server...")
best = test.get_best_server() # choose best servers

print(f"Found: {best['host']} located in {best['country']}")

time.sleep(5)
print("------------------------------------------------------")
ping_result = test.results.ping
print(f"Ping: {ping_result} ms")
print("------------------------------------------------------")
download_result = test.download()
print(f"Download speed: {float(download_result / 1024 / 1024):.2f} Mbps")
print("------------------------------------------------------")
upload_result = test.upload()
print(f"Upload speed: {float(upload_result / 1024 / 1024):.2f} Mbps")
print("------------------------------------------------------")





