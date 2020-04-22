import requests

country = input("Enter the name of the country you want to know information about: ").lower()
responce = requests.get(f"https://restcountries.eu/rest/v2/name/{country}?fullText=true")
data_in_list = responce.json()
# Convert data from list to a dictionary
for i in data_in_list:
  data = i

print("")
print("Country name: " + data["name"])
print("Native name: " + data["nativeName"])
print("Capital: " + data["capital"])
print("Population: " + str(data["population"]))
print("Region: " + data["region"])
print("Subregion: " + data["subregion"])
print("Area: " + str(int(data["area"])) + "km")
print("Citizen: " + data["demonym"])
for subdata in data["currencies"]:
  print("Currency: " + subdata["name"] + " (" + subdata["symbol"] + ")")
for subdata in data["languages"]:
  print("Primary language: " + subdata["name"] + " (" + subdata["nativeName"] + ")")
for subdata in data["regionalBlocs"]:
  print("Regional Bloc: " + subdata["name"] + " (" + subdata["acronym"] + ")")