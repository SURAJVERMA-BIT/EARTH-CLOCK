# World Clock with GUI

## Overview

This project is a world clock application with a graphical user interface (GUI) built using Python. It allows users to select a country, view the current time in that country, and visualize a map of the selected country. The application also includes text-to-speech functionality to announce the current time.

## Features

- **Country Selection**: Choose a country from a dropdown list.
- **Time Display**: View the current time in the selected country.
- **Map Display**: See an interactive map of the selected country.
- **Text-to-Speech**: Hear the current time announced in a friendly format.
- **Dark Mode**: Toggle between light and dark themes for the GUI.

## Installation

1. **Clone the Repository:**

    git clone https://github.com/SURAJVERMA-BIT/world-clock.git
    cd world-clock

2. **Create a Virtual Environment (Optional but recommended):**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

3. **Install Dependencies:**

    Ensure you have `requirements.txt` in your project directory and run:

    
    pip install -r requirements.txt

## Usage

1. **Run the Application:**

    python gui.py

2. **Select a Country:**
    - Use the dropdown menu to select a country.

3. **View Time and Map:**
    - Click "Show Time" to view the current time and see the map.

4. **Toggle Dark Mode:**
    - Click the "Toggle Dark Mode" button to switch between light and dark themes.

## Requirements

- **Python** (version 3.7 or above)
- **Libraries**:
    - `tkinter`
    - `pyttsx3`
    - `pytz`
    - `pycountry`
    - `folium`
    - `webbrowser`

## Troubleshooting

- **Map Not Displaying**: Ensure you have an active internet connection and the necessary permissions for generating maps.
- **Text-to-Speech Issues**: Verify that `pyttsx3` is properly installed and configured.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Email:** sv9052788@example.com
- **GitHub:** [SURAJVERMA-BIT](https://github.com/SURAJVERMA-BIT)

## TIP
Keep practising and practising........All the best 

[def]: LICENSE