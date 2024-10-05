import streamlit as st
import pandas as pd
import altair as alt
st.set_page_config(page_title="Aquaponics Implementation & Climate", page_icon="🌡", layout="wide")
if 'language' not in st.session_state:
    st.session_state.language = 'English'  
def toggle_language():
    st.session_state.language = 'Tamil' if st.session_state.language == 'English' else 'English'
st.sidebar.checkbox(" தமிழ்", value=(st.session_state.language == 'Tamil'), on_change=toggle_language)
content = {
    'title': {
        'English': "🌡 Aquaponics Implementation: Scientific Data & Climate Considerations",
        'Tamil': "🌡 அகுவாப்பொனிக்ஸ் செயலாக்கம்: அறிவியல் தரவுகள் மற்றும் வானிலை கருதுகோள்கள்"
    },
    'introduction': {
        'English': """Aquaponics is a sustainable food production system that combines aquaculture with hydroponics. 
        This page provides scientific data for implementation and explores how different climates and regions 
        affect aquaponics systems.""",
        'Tamil': """அகுவாப்பொனிக்ஸ் என்பது மீன் வளர்ச்சி மற்றும் நீர் மண்ணில் பயிர் வளர்ப்பை இணைக்கும் 
        ஒரு நிலையான உணவு உற்பத்தி முறை. இந்த பக்கம் செயலாக்கத்திற்கான அறிவியல் தரவுகளை 
        வழங்குகிறது மற்றும் வானிலை மற்றும் மண்டலங்கள் அகுவாப்பொனிக்ஸ் அமைப்புகளை எப்படி 
        பாதிக்குமென்று ஆராய்கிறது."""  
    },
    'system_design': {
        'header': {
            'English': "System Design",
            'Tamil': "அமைப்பு வடிவமைப்பு"
        },
        'ratio_subheader': {
            'English': "Ratio of Fish Tank to Grow Bed",
            'Tamil': "மீன் கிணற்றின் அளவு மற்றும் வளர்ப்பு மேசையின் உறவு"
        },
        'water_quality_header': {
            'English': "Water Quality Parameters",
            'Tamil': "நீர் தரம் அளவுகோல்கள்"
        },
        'climate_header': {
            'English': "Climate and Regional Considerations",
            'Tamil': "வானிலை மற்றும் மண்டல அடிப்படையில் கருத்துகள்"
        },
        'energy_header': {
            'English': "Energy Efficiency by Climate",
            'Tamil': "வானிலையால் ஆற்றல் திறன்"
        },
        'plant_selection_header': {
            'English': "Plant Selection by Climate",
            'Tamil': "வானிலை அடிப்படையில் செடிகள் தேர்வு"
        },
        'conclusion': {
            'English': """Implementing an aquaponics system requires careful consideration of scientific parameters and local climate conditions. 
            By adapting the system design to your specific region and climate, you can create a productive and sustainable food 
            production system almost anywhere in the world.""",
            'Tamil': """அகுவாப்பொனிக்ஸ் அமைப்பை செயல்படுத்துவது அறிவியல் அளவுகோல்கள் மற்றும் உள்ளூர் வானிலை 
            நிலைகள் ஆகியவற்றை கவனமாக பரிசீலிக்க வேண்டும். உங்கள் குறிப்பிட்ட மண்டலம் மற்றும் வானிலைக்கு 
            அமைப்பின் வடிவமைப்பை பொருந்தவைக்கக் கூடியால், நீங்கள் உலகின் எங்கும் உள்ள உற்பத்தி மற்றும் 
            நிலையான உணவு உற்பத்தி அமைப்பை உருவாக்கலாம்."""   
        }
    }
}
st.title(content['title'][st.session_state.language])
st.header(content['system_design']['header'][st.session_state.language])
st.write(content['introduction'][st.session_state.language])
st.subheader(content['system_design']['ratio_subheader'][st.session_state.language])
ratio_data = pd.DataFrame({
    'Ratio': ['1:1', '1:2', '1:3', '1:4'],
    'Efficiency': [75, 85, 95, 100]
})
chart = alt.Chart(ratio_data).mark_bar().encode(
    x=alt.X('Ratio:O', title='Ratio (Fish:Grow)'),
    y=alt.Y('Efficiency:Q', title='Efficiency (%)'),
    color=alt.value('#9370DB')
).properties(
    title='System Efficiency by Fish:Grow Ratio'
)
st.altair_chart(chart, use_container_width=True)
st.header(content['system_design']['water_quality_header'][st.session_state.language])
parameters = pd.DataFrame({
    'Parameter': ['pH', 'Ammonia (NH3)', 'Nitrite (NO2)', 'Nitrate (NO3)', 'Dissolved Oxygen', 'Temperature'],
    'Optimal Range': ['6.8-7.0', '< 1 mg/L', '< 1 mg/L', '5-150 mg/L', '> 5 mg/L', '18-30°C (64-86°F)'],
    'Critical Value': ['< 6.0 or > 8.0', '> 2 mg/L', '> 2 mg/L', '> 300 mg/L', '< 3 mg/L', '< 10°C or > 35°C']
})
st.table(parameters)
st.header(content['system_design']['climate_header'][st.session_state.language])
st.write("""Aquaponics can be implemented in various climates, but system design may need to be adapted based on local conditions.""")
climate_data = pd.DataFrame({
    'Climate Type': ['Tropical', 'Arid', 'Temperate', 'Continental', 'Polar'],
    'Temperature Range (°C)': ['20-30', '10-40', '5-25', '-20-30', '-40-10'],
    'Humidity (%)': ['70-100', '10-30', '60-70', '40-60', '40-80'],
    'Challenges': ['High humidity', 'Water scarcity', 'Seasonal variations', 'Extreme temperature swings', 'Limited growing season'],
    'Adaptations': ['Shade structures, ventilation', 'Water conservation, indoor systems', 'Greenhouses, temperature control', 'Insulation, heating systems', 'Indoor systems, artificial lighting']
})
st.dataframe(climate_data)
st.header(content['system_design']['energy_header'][st.session_state.language])
st.write("""Energy use in aquaponics systems varies based on climate. Here's a comparison of relative energy needs:""")
energy_data = pd.DataFrame({
    'Climate': ['Tropical', 'Arid', 'Temperate', 'Continental', 'Polar'],
    'Heating': [10, 30, 50, 70, 90],
    'Cooling': [60, 80, 40, 20, 10],
    'Lighting': [20, 30, 40, 50, 80]
})
energy_chart = alt.Chart(energy_data.melt('Climate', var_name='Energy Type', value_name='Energy Need')).mark_bar().encode(
    x='Climate:N',
    y='Energy Need:Q',
    color=alt.Color('Energy Type:N', scale=alt.Scale(scheme='purples')),
    tooltip=['Climate', 'Energy Type', 'Energy Need']
).properties(
    title='Relative Energy Needs by Climate'
)
st.altair_chart(energy_chart, use_container_width=True)
st.header(content['system_design']['plant_selection_header'][st.session_state.language])
st.write("""Different climates are better suited for certain types of plants in aquaponics systems. Here's a general guide:""")
plant_data = pd.DataFrame({
    'Climate': ['Tropical', 'Arid', 'Temperate', 'Continental', 'Polar'],
    'Leafy Greens': ['High', 'Medium', 'High', 'Medium', 'Low'],
    'Fruiting Vegetables': ['High', 'High', 'Medium', 'Low', 'Very Low'],
    'Herbs': ['High', 'High', 'High', 'Medium', 'Low'],
    'Root Vegetables': ['Medium', 'Low', 'High', 'High', 'Medium']
})
st.table(plant_data)
st.header(content['system_design']['climate_header'][st.session_state.language])  
st.write(content['system_design']['conclusion'][st.session_state.language])
st.write("🌱 Sustainable farming for a better future, in every climate! 🌍")