import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

key = sys.argv[1]
bus_line = sys.argv[2]
file_name = sys.argv[3]


bus_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line
response = urllib.urlopen(bus_url)
bus_data = response.read().decode("utf-8")
bus_data = json.loads(bus_data)
vehicles = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_vehicles = len(vehicles)


file = open(file_name, "w")
file.write("Latitude,Longitude,Stop Name,Stop Status\n")

for n in range(num_vehicles):
    latitude = vehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = vehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    
    try:
        stop =  vehicles[n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except:
        stop = "N/A"

    try:
        status = vehicles[n]['MonitoredVehicleJourney']["OnwardCalls"]['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except:
        status = "N/A"
        
    file.write('%s,%s,%s,%s\n'%(latitude, longitude, stop, status))

file.close()




