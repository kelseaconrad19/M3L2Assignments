"""
Task 1: Stock Prices
    - Create a function to calculate the average closing price of a specific stock symbol over all dates.
    - Ensure your solution handles cases where the stock symbol does not exist in the data.
"""


# def calc_average(stocks):
#     closing_prices = []
#     for ele in stocks:
#         closing_price = ele[-1]
#         closing_prices.append(closing_price)
#     total = sum(closing_prices)
#     num = len(closing_prices)
#     average = round((total / num), 2)
#     return average
#
#
# stock_data = [
#     ("AAPL", "2021-01-01", 130.0),
#     ("AAPL", "2021-01-02", 132.0),
#     ("MSFT", "2021-01-01", 220.0),
# ]
#
# if __name__ == "__main__":
#     print(calc_average(stock_data))


"""
Task 2: 
    - Develop a function to list all attendees of a specific event.
    - Implement a feature to count the number of attendees for each event.
"""


def attendance_count(attendee_list):
    event = input("Event: ").lower()
    event_attendees = 0
    for person in attendee_list:
        if person[1].lower() == event:
            event_attendees += 1
            print(f"{person[0]}")
        else:
            continue
    print(f"Number of attendees: {event_attendees}")


attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
]

if __name__ == "__main__":
    attendance_count(attendees)
