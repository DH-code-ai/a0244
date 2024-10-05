import streamlit as st
import time
def set_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #001f3f, #1e3799);
        background-attachment: fixed;
    }
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .swim-animation {
        width: 100px;
        height: 50px;
        background: linear-gradient(to right, #4fc3f7, #b388ff);
        clip-path: polygon(0% 50%, 25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%);
        animation: swim 5s ease-in-out infinite;
    }
    @keyframes swim {
        0%, 100% { transform: translateX(0) rotateY(0deg); }
        25% { transform: translateX(50px) rotateY(0deg); }
        50% { transform: translateX(100px) rotateY(180deg); }
        75% { transform: translateX(50px) rotateY(180deg); }
    }
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    .streamlit-expanderContent {
        background-color: rgba(0, 0, 0, 0.2) !important;
        color: white !important;
    }
    h1, h2, h3, p {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
def main():
    set_custom_css() 
    language = st.sidebar.selectbox("🌐 Select Language", ["English", "தமிழ்"]) 
    if language == "English":
        st.title("🐠 Aquaponic Fish Selection 🌿")
    else:
        st.title("🐠 அக்வாபொனிக் மீன் தேர்வு 🌿")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    if language == "English":
        st.write("""
        Welcome to the world of Aquaponic Fish Selection! Choosing the right fish species is crucial
        for a successful aquaponics system. Let's dive into the factors to consider and some popular fish options.
        """)
    else:
        st.write("""
        அக்வாபொனிக் மீன் தேர்வு உலகிற்கு வரவேற்கின்றோம்! உங்கள் அக்வாபொனிக் அமைப்பில் வெற்றியை உறுதிப்படுத்த சரியான மீன் வகையைத் தேர்ந்தெடுப்பது மிக முக்கியம். கவனிக்க வேண்டிய காரணிகள் மற்றும் சில பிரபலமான மீன் விருப்பங்களைப் பார்ப்போம்.
        """)
    st.markdown('<div class="swim-animation"></div>', unsafe_allow_html=True)
    if language == "English":
        st.header("🧐 Factors to Consider")
        factors = [
            "Water Temperature 🌡",
            "pH Levels 📊",
            "Space Requirements 📏",
            "Oxygen Needs 💨",
            "Growth Rate 📈",
            "Market Demand 🛒"
        ]
    else:
        st.header("🧐 கவனிக்க வேண்டிய காரணிகள்")
        factors = [
            "நீரின் வெப்பநிலை 🌡",
            "pH நிலைகள் 📊",
            "இடத்திற்கான தேவைகள் 📏",
            "ஆக்ஸிஜன் தேவைகள் 💨",
            "வளர்ச்சி விகிதம் 📈",
            "சந்தை தேவைகள் 🛒"
        ]
    for factor in factors:
        st.write(f"• {factor}")
    if language == "English":
        st.header("🐟 Popular Aquaponic Fish Species")
    else:
        st.header("🐟 பிரபல அக்வாபொனிக் மீன் வகைகள்")
    fish_species = {
        "Tilapia 🐠": {
            "scientific_name": "Oreochromis niloticus",
            "pros_en": ["Adaptable to various conditions", "Fast growth rate", "Disease resistant"],
            "pros_ta": ["பல்வேறு நிலைகளுக்கு ஏற்ப உட்புகும்", "வேகமான வளர்ச்சி", "நோய்களுக்கு எதிர்ப்பு"],
            "cons_en": ["May require heating in cooler climates", "Can be aggressive"],
            "cons_ta": ["குளிரான காலநிலைகளில் சூடாக்கம் தேவை", "ஆக்கிரமிப்பு நடத்தை இருக்கலாம்"],
            "optimal_temp": "20-30°C (68-86°F)",
            "pH_range": "6.5-8.5"
        },
        "Trout 🎣": {
            "scientific_name": "Oncorhynchus mykiss",
            "pros_en": ["Thrive in cooler water", "High-value fish", "Efficient feed conversion"],
            "pros_ta": ["குளிர்ந்த நீரில் சிறப்பாக வளர்கின்றன", "மிக அதிக மதிப்புள்ள மீன்", "சிறப்பான உணவு மாற்றம்"],
            "cons_en": ["Require high oxygen levels", "Sensitive to water quality"],
            "cons_ta": ["உயர் ஆக்ஸிஜன் நிலைகள் தேவை", "நீர் தரத்திற்கு மிக நுணுக்கமானது"],
            "optimal_temp": "10-18°C (50-64°F)",
            "pH_range": "6.5-8.5"
        },
    }
    for species, details in fish_species.items():
        with st.expander(species):
            if language == "English":
                st.write(f"*Scientific Name:* {details['scientific_name']}")
                st.write(f"*Optimal Temperature:* {details['optimal_temp']}")
                st.write(f"*pH Range:* {details['pH_range']}")
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Pros ✅")
                    for pro in details["pros_en"]:
                        st.write(f"• {pro}")
                with col2:
                    st.subheader("Cons ❌")
                    for con in details["cons_en"]:
                        st.write(f"• {con}")
            else:
                st.write(f"*அறிவியல் பெயர்:* {details['scientific_name']}")
                st.write(f"*சிறந்த வெப்பநிலை:* {details['optimal_temp']}")
                st.write(f"*pH வரம்பு:* {details['pH_range']}")
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("நன்மைகள் ✅")
                    for pro in details["pros_ta"]:
                        st.write(f"• {pro}")
                with col2:
                    st.subheader("பயன்கள் ❌")
                    for con in details["cons_ta"]:
                        st.write(f"• {con}")
            time.sleep(0.5)   
    st.markdown('</div>', unsafe_allow_html=True)
    if language == "English":
        st.header("🌟 Conclusion")
        st.write("""
        Selecting the right fish species is crucial for the success of your aquaponics system. Consider
        factors like water temperature, pH levels, and space requirements when making your choice.
        Remember, a thriving fish population leads to healthy plants and a productive aquaponics ecosystem!
        """)
    else:
        st.header("🌟 முடிவுரை")
        st.write("""
        சரியான மீன் வகையைத் தேர்ந்தெடுப்பது உங்கள் அக்வாபொனிக் அமைப்பின் வெற்றிக்கு மிக முக்கியம். 
        நீரின் வெப்பநிலை, pH நிலைகள், மற்றும் இடவசதியை அடிப்படையாகக் கொண்டு உங்கள் தேர்வுகளை செய்யுங்கள்.
        நல்ல ஆரோக்கியமான மீன் தொகை மகிழ்ச்சியான தாவர வளர்ச்சிக்கு வழி வகுக்கும்!
        """)
if __name__ == "__main__":
    main()