import os
import tkinter as tk
from tkinter import ttk
import pytz
from datetime import datetime
from time_zones import country_time_zones, generate_map_for_country
import pyttsx3
import webbrowser
from PIL import Image, ImageTk

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def unique_filename(filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(new_filename):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

def show_time():
    selected_country = country_combo.get()
    tz_list = country_time_zones.get(selected_country)
    time_display.delete(1.0, tk.END)
    
    # Ensure the directory for opened maps exists
    ensure_directory_exists('OPENED maps')
    
    if tz_list:
        for tz in tz_list:
            try:
                tz_info = pytz.timezone(tz)
                time_in_country = datetime.now(tz_info).strftime('%I:%M %p')
                display_text = f"The current time in {selected_country} ({tz}) is: {time_in_country}\n"
                time_display.insert(tk.END, display_text)
                
                # Announce only the time
                time_only_text = f"The time is {time_in_country}\n"
                speak_text(time_only_text)
                
            except pytz.UnknownTimeZoneError:
                error_text = f"Unknown time zone: {tz}\n"
                time_display.insert(tk.END, error_text)
                speak_text(error_text)
        
        # Generate and save the map
        map_filename = generate_map_for_country(selected_country)
        if not map_filename:
            no_map_text = "Failed to generate map.\n"
            time_display.insert(tk.END, no_map_text)
            speak_text(no_map_text)
            return
        
        map_filename_in_directory = os.path.join('OPENED maps', os.path.basename(map_filename))
        # Ensure unique filename
        map_filename_in_directory = unique_filename(map_filename_in_directory)
        try:
            os.rename(map_filename, map_filename_in_directory)
            display_map(map_filename_in_directory)
        except FileExistsError:
            # Handle case where file already exists
            time_display.insert(tk.END, f"Map file already exists: {map_filename_in_directory}\n")
            speak_text(f"Map file already exists: {map_filename_in_directory}")
    else:
        no_time_zones_text = "No time zones available for this country.\n"
        time_display.insert(tk.END, no_time_zones_text)
        speak_text(no_time_zones_text)

def display_map(map_filename):
    map_window = tk.Toplevel(root)
    map_window.title("Country Map")
    
    # Display the map as an HTML file in the default browser
    try:
        webbrowser.open(map_filename)
    except Exception as e:
        tk.Label(map_window, text=f"Error opening map: {str(e)}").pack()

def show_world_map():
    map_window = tk.Toplevel(root)
    map_window.title("World Map")
    
    try:
        # Load and display the world map image
        world_map_img = Image.open("images/world_map.png")  # Ensure this path is correct
        world_map_photo = ImageTk.PhotoImage(world_map_img)
        
        img_label = tk.Label(map_window, image=world_map_photo)
        img_label.image = world_map_photo
        img_label.pack()

        # Bind click event to label (if you want to handle clicks)
        img_label.bind("<Button-1>", on_map_click)
    except Exception as e:
        tk.Label(map_window, text=f"Error loading world map: {str(e)}").pack()

def on_map_click(event):
    print(f"Clicked at {event.x}, {event.y}")

def toggle_dark_mode():
    if dark_mode_button.config('relief')[-1] == 'sunken':
        # Light mode
        root.config(bg='white')
        time_display.config(bg='white', fg='black', insertbackground='black')
        country_label.config(bg='white', fg='black')
        time_button.config(bg='lightgray', fg='black')
        map_button.config(bg='lightgray', fg='black')
        dark_mode_button.config(relief='raised', bg='lightgray', fg='black', text='Switch to Dark Mode')
    else:
        # Dark mode
        root.config(bg='black')
        time_display.config(bg='black', fg='white', insertbackground='white')
        country_label.config(bg='black', fg='white')
        time_button.config(bg='gray', fg='white')
        map_button.config(bg='gray', fg='white')
        dark_mode_button.config(relief='sunken', bg='gray', fg='white', text='Switch to Light Mode')

root = tk.Tk()
root.title("World Clock")

country_label = tk.Label(root, text="Select a country:")
country_label.pack(pady=10)

country_combo = ttk.Combobox(root, values=list(country_time_zones.keys()))
country_combo.pack(pady=10)

time_button = tk.Button(root, text="What's The Time", command=show_time)
time_button.pack(pady=10)

time_display = tk.Text(root, height=10, width=50)
time_display.pack(pady=10)

# Add button for world map
map_button = tk.Button(root, text="Show World Map", command=show_world_map)
map_button.pack(pady=10)

# Add button for dark mode toggle
dark_mode_button = tk.Button(root, text="Switch to Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

root.mainloop()