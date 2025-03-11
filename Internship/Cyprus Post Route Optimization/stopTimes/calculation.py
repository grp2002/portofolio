import csv
import json
import math


def distance_between_points(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Earth's radius in kilometers
    R = 6371
    # Calculate delta distances
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Convert distance from kilometers to meters
    return R * c * 1000

def is_user_in_range(user_lat, user_lon, mailbox_lat, mailbox_lon, range_meters):
    # Determine if the user is within a certain range of the mailbox
    return distance_between_points(user_lat, user_lon, mailbox_lat, mailbox_lon) <= range_meters

def load_mailboxes(filename):
    # Load mailbox locations from a JSON file
    with open(filename, 'r') as file:
        data = json.load(file)
        return [(item['id'], item['latitude'], item['longitude']) for item in data['data']]
    
def create_route_map(filename):  
    # Load JSON data from file
    with open(filename, 'r') as file:
        data = json.load(file)

    # Create a map of routes to opteboxIds
    route_map = {}
    for entry in data:
        route = entry["route"]
        opteboxId = entry["opteboxId"]
        if route not in route_map:
            route_map[route] = []
        route_map[route].append(opteboxId)

    return route_map

def find_best_matching_route(route_map, optebox_ids):
    best_match = None
    max_matches = 0
    missing_boxes = set()

    all_route_boxes = set()

    unmatched_boxes = optebox_ids - all_route_boxes

    for route, ids in route_map.items():
        matches = len(set(ids) & optebox_ids)
        if matches > max_matches:
            max_matches = matches
            best_match = route
            missing_boxes = set(ids) - optebox_ids
            unmatched_boxes = optebox_ids - set(ids)
    return best_match, missing_boxes, unmatched_boxes



def read_csv_data(filename):
    # Read user journey data from a CSV file
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the "Journey" line
        next(reader)  # Skip the "Lat, Lng, Time" header line
        data = []
        for row in reader:
            if row and "End Time:" not in row[0]:  # Check if the row is not the ending line
                lat, lon, time_str = row
                time_parts = time_str.split(":")
                time_seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
                data.append((float(lat), float(lon), time_seconds))
        return data
    
def format_time(seconds):
    # Convert seconds to minutes and seconds format
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def user_speed(prev_lat, prev_lon, lat, lng, prev_time, time):
    distance = distance_between_points(prev_lat, prev_lon, lat, lng)
    time_diff = time - prev_time
    if time_diff <= 0:
        return 0
    speed = (distance / 1000) / (time_diff / 3600)
    return speed

def main():
    # Load data
    mailboxes = load_mailboxes('boxLocations.json')
    user_data = read_csv_data('5.7(makris).csv')
    # Initialize count dictionary
    mailbox_time_count = {}
    # Initialize total distance traveled
    total_distance = 0
    
    visited_boxes = set()
    
    create_route_map('opteboxes.json')

    # Calculate total distance traveled
    for i in range(1, len(user_data)):
        lat1, lon1, time1 = user_data[i-1]
        lat2, lon2, time2 = user_data[i]
        total_distance += distance_between_points(lat1, lon1, lat2, lon2)
        
    # Count how often user is within range of each mailbox
    for i in range(1, len(user_data)):
        lat, lng, time = user_data[i]
        prev_lat, prev_lon, prev_time = user_data[i-1]
        speed = user_speed(prev_lat, prev_lon, lat, lng, prev_time, time)
        walking_speed_threshold = 5  # adjust this value to your desired walking speed threshold (in km/h)
        if speed <= walking_speed_threshold:
            for mailbox_id, mailbox_lat, mailbox_lon in mailboxes:
                if is_user_in_range(lat, lng, mailbox_lat, mailbox_lon, 20):
                    if mailbox_id not in mailbox_time_count:
                        mailbox_time_count[mailbox_id] = 0
                    mailbox_time_count[mailbox_id] += 1
                    visited_boxes.add(mailbox_id)
    
    
    # Write results to a CSV file
    with open("stoptimes.csv", 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Mailbox ID", "Stop Time"])
        for mailbox_id, count in mailbox_time_count.items():
            writer.writerow([mailbox_id, format_time(count)])

    # Print the results
    for mailbox_id, count in mailbox_time_count.items():
        print(f"User was in range of mailbox ID {mailbox_id} for {format_time(count)} ")
    print(f"Total distance traveled: {total_distance:.2f} meters")

    route_map = create_route_map('opteboxes.json')
    best_route, missing_boxes, unmatched_boxes = find_best_matching_route(route_map, visited_boxes)
    print(f"Route: {best_route}")
    if missing_boxes:
        print(f"These boxes were not visited: {sorted(missing_boxes)}")
    if unmatched_boxes:
        print(f"These boxes are not included in any route: {sorted(unmatched_boxes)}")
    
if __name__ == '__main__':
    main()
