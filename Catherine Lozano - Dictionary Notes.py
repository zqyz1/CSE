states = {
    "CA": "California",
          "VA": "Virginia",
          "MD": "Maryland",
          "RI": "Rhode Island",
          "NV": "Nevada"

}
print(states["CA"])
print(states["NV"])

nested_dictionary = {
      "CA": {
          "NAME": "CALIFORNIA",
          "POPULATION": 39557045 # 39,557,045
      },
      "VA": {
          "NAME": "VIRGINIA",
          "POPULATION": 8517685 #8,517,685
      },
      "MD":{
          "NAME": "MARYLAND",
          "POPULATION": 8517685 # 8,517,685
      },
      "RI":{
          "NAME": "RHODE ISLAND",
          "POPULATION": 1057315 # 1,057,315
      },
      "NV": {
          "NAME": "NEVADA",
          "POPULATION": 3034392 # 3,034,392
      }
}

print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])

complex_dictionary = {
      "CA": {
          "NAME": "CALIFORNIA",
          "POPULATION": 39557045, # 39,557,045
          "CITIES": [
               "Fresno",
               "San Francisco",
               "Los Angeles"
          ]
      },
      "VA": {
          "NAME": "VIRGINIA",
          "POPULATION": 8517685, # 8,517,685
          "CITIES": [
               "Richmond",
               "Norfolk",
               "Alexandria"
          ]
      },
      "MD":{
          "NAME": "MARYLAND",
          "POPULATION": 8517685, # 8,517,685
          "CITIES": [
               "Bethesda",
               "Baltimore",
               "Annapolis"
          ]
      },
      "RI":{
          "NAME": "RHODE ISLAND",
          "POPULATION": 1057315, # 1,057,315
          "CITIES": [
               "Providence",
               "Newport",
               "Warwick"
          ]
      },
      "NV": {
          "NAME": "NEVADA",
          "POPULATION": 3034392, # 3,034,392
          "CITIES": [
               "Carson City",
               "Las Vegas",
               "Reno"
          ]
      }
}

print(complex_dictionary["RI"]["CITIES"][2])

print(complex_dictionary["VA"]["NAME"])
print(complex_dictionary["MD"]["CITIES"][0])

print(complex_dictionary.keys())
print(nested_dictionary.items())

print()
for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

for state, facts in complex_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print('=' * 20)
    print('=' * 20)




















