"""
Task 1: Formatting Flight Itineraries
    Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:
    - "Itinerary 1: Alice - From New York to London
    - Itinerary 2: Bob - From Tokyo to San Francisco"
"""
travelers = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]


def itinerary_list(traveler_info):
    for i, person in enumerate(traveler_info):
        name = person[0]
        origin = person[1]
        destination = person[2]
        print(f"Itinerary {i + 1}: {name} - From {origin} to {destination}")


if __name__ == "__main__":
    itinerary_list(travelers)
