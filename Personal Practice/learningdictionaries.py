#Using dictionaries in python

store = {"USA": "Washington D.C.",
              "Lagos": "Ikeja",
                "Anambra": "Awka",
               "Ogun": "Abeokuta"}

#dir(capitals)

print(store.get("USA"))

store.update({"USA": "Sagamu"})

print(store.get("USA"))

store.pop("USA")

print(store.get("USA"))