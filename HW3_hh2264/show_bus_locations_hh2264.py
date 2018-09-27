import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

    
key = sys.argv[1]
bus_line = sys.argv[2]

bus_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&LineRef="+bus_line
response = urllib.urlopen(bus_url)
bus_data = response.read().decode("utf-8")
bus_data = json.loads(bus_data)
vehicles = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_vehicles = len(vehicles)

print("Bus Line : "+bus_line)
print("Number of Active Buses : " +str(num_vehicles))

for n in range(num_vehicles):
    latitude = vehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = vehicles[n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus %s is at latitude % and longitude %s" %(n, latitude, longitude))



