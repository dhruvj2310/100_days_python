##---------------------------------------------------------------------------------------##

## dictionary
travel_log = {
    "Frace": "Paris",
    "Germany": "Berlin"
}

## print Berlin
print(travel_log["Germany"])

##---------------------------------------------------------------------------------------##

## nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Print Lille
print(travel_log["France"][1])

##---------------------------------------------------------------------------------------##

## nested dictionary in dictionary in dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}


print(travel_log["Germany"]["cities_visited"][2])