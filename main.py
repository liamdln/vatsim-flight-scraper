from scraper import Scraper

# Vars
version = "1.0.0"
vatsimDataUrl = "http://data.vatsim.net"
dataItems = ["callsign", "latitude", "longitude", "altitude", "groundspeed", "planned_depairport", "planned_destairport"]
scraper = Scraper(dataItems)


print(f"""\nVATSIM Data Scraper v{version}
By Liam P\n""")

print("Will grab the following data items:")

for item in dataItems:
    print(item)

print(f"From: {scraper.buildUrl(vatsimDataUrl)}")

print(scraper.grabJson(vatsimDataUrl))