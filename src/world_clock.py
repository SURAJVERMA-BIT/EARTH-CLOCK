import pytz
from datetime import datetime, timedelta
from time_zones import country_time_zones, get_standard_country_name, get_all_timezones, get_country_coordinates
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    # Replace unwanted characters and format the time string
    text = text.replace('/', ' ').replace('-', ' ').replace(':', ' ')
    # Optionally, remove the year if you don't want it spoken
    text = ' '.join(text.split()[1:])  # Removes the first part (year) from the string
    engine.say(text)
    engine.runAndWait()

def display_time_for_country():
    print("You can choose from the following countries:")
    for country in country_time_zones.keys():
        print(f"- {country}")

    selected_country = input("Enter the country you'd like to know the time of: ")
    standardized_country = get_standard_country_name(selected_country)

    if standardized_country and standardized_country in country_time_zones:
        time_zones = country_time_zones[standardized_country]
        for tz in time_zones:
            tz_info = pytz.timezone(tz)
            time_in_country = datetime.now(tz_info).strftime(' %I:%M %p %Y-%m-%d')
            message = f"The current time in {standardized_country} ({tz}) is: {time_in_country}"
            print(message)
            speak(message)
    else:
        message = "Sorry, you must be searching a planet from Mars definately ."
        print(message)
        speak(message)

def display_time_for_multiple_countries():
    selected_countries = input("Enter the countries you'd like to know the time of (comma-separated): ")
    countries = [country.strip() for country in selected_countries.split(",")]

    for country in countries:
        standardized_country = get_standard_country_name(country)
        if standardized_country and standardized_country in country_time_zones:
            time_zones = country_time_zones[standardized_country]
            for tz in time_zones:
                tz_info = pytz.timezone(tz)
                time_in_country = datetime.now(tz_info).strftime('%Y-%m-%d %I:%M %p')
                message = f"The current time in {standardized_country} ({tz}) is: {time_in_country}"
                print(message)
                speak(message)
        else:
            message = f"Sorry, {country} is not on earth."
            print(message)
            speak(message)

def display_custom_time_zone():
    custom_tz = input("Enter a specific time zone (e.g., 'Asia/Kolkata'): ")
    if custom_tz in get_all_timezones():
        tz_info = pytz.timezone(custom_tz)
        time_in_custom_zone = datetime.now(tz_info).strftime('%Y-%m-%d %I:%M %p')
        message = f"The current time in {custom_tz} is: {time_in_custom_zone}"
        print(message)
        speak(message)
    else:
        message = "Sorry, that time zone is not recognized."
        print(message)
        speak(message)

def display_time_with_dst(time_zone):
    tz = pytz.timezone(time_zone)
    now = datetime.now(tz)
    is_dst = now.dst() != timedelta(0)
    message = f"Time: {now.strftime('%Y-%m-%d %I:%M %p')} (DST: {'Yes' if is_dst else 'No'})"
    print(message)
    speak(message)

def display_country_on_map(selected_country):
    import folium

    latitude, longitude = get_country_coordinates(selected_country)
    m = folium.Map(location=[latitude, longitude], zoom_start=4)
    folium.Marker([latitude, longitude], popup=selected_country).add_to(m)
    m.save('map.html')
    message = f"Map has been saved to 'map.html'."
    print(message)
    speak(message)

# Start the script
if __name__ == "__main__":
    display_time_for_country()
