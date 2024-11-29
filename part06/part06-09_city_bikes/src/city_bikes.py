# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    stations = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
    return stations

def distance(stations: dict, station1: str, station2: str):
    import math
    for key,value in stations.items():
        if key == station1:
            location1 = value
        if key == station2:
            loctaion2 = value
    a = (location1[0] - loctaion2[0]) * 55.26
    b = (location1[1] - loctaion2[1]) * 111.2
    distance = math.sqrt(a**2 + b**2)
    return distance

def greatest_distance(stations: dict):
    longest = 0
    for key1 in stations:
        for key2 in stations:
            d = distance(stations, key1, key2)
            if longest <= d:
                longest = d
                name1 = key1
                name2 = key2
    return (name1, name2, longest)
        



