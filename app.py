import streamlit as st
import requests
import base64
from database import get_crops_by_soil
from setup import setup_authentication
authenticator = setup_authentication()
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set the title with custom color
st.markdown("<h1 style='color: #4CAF50;'>Climate-Resilient Crop Advisory System</h1>", unsafe_allow_html=True)

# Add a background image with a transparent overlay
background_image = get_base64_image("pexels-souvenirpixels-414612.jpg")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.4); /* Semi-transparent black overlay */
        z-index: -1;
    }}
    </style>
    <div class="overlay"></div>
    """,
    unsafe_allow_html=True
)

# Custom style for input boxes
input_style = """
<style>
    input, select {
        border-radius: 5px;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.8); /* Slightly transparent background for input boxes */
    }
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

# Input fields for user data with custom style
st.markdown("<h3 style='color: #FFA726;'>Enter your location:</h3>", unsafe_allow_html=True)
location = st.text_input("", key="location_input")

st.markdown("<h3 style='color: #FFA726;'>Select your soil type:</h3>", unsafe_allow_html=True)
soil_type = st.selectbox("", ["Sandy", "Clay", "Silty", "Peaty", "Chalky", "Loamy"], key="soil_select")

# Your actual API key
api_key = '15ebc8242fb34eafbaf21234240408'

# Function to fetch weather data
def fetch_weather(location):
    weather_api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    try:
        response = requests.get(weather_api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

# Fetch and display weather data
if location:
    weather_data = fetch_weather(location)
    if weather_data:
        st.markdown("<h2 style='color: #29B6F6;'>Current weather in {location}:</h2>".format(location=location), unsafe_allow_html=True)
        st.markdown(f"<p style='color: #FFEB3B;'><strong>Temperature</strong>: {weather_data['current']['temp_c']}°C</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #FFEB3B;'><strong>Condition</strong>: {weather_data['current']['condition']['text']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #FFEB3B;'><strong>Humidity</strong>: {weather_data['current']['humidity']}%</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #FFEB3B;'><strong>Pressure</strong>: {weather_data['current']['pressure_mb']} mb</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #FFEB3B;'><strong>Precipitation in inches</strong>: {weather_data['current']['precip_mm']} mm</p>", unsafe_allow_html=True)

# Fetch crop recommendations from the database
if st.button("Get Crop Recommendations", key="get_recommendations"):
    if location and soil_type:
        recommendations = get_crops_by_soil(soil_type)
        if recommendations:
            st.markdown("<h2 style='color: #4CAF50;'>Recommended Crops:</h2>", unsafe_allow_html=True)
            for crop in recommendations:
                st.markdown(f"<p style='color: #FFC107;'><strong>{crop}</strong></p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: #FF5722;'>No crop recommendations available for this soil type.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #FF5722;'>Please enter all required information.</p>", unsafe_allow_html=True)
