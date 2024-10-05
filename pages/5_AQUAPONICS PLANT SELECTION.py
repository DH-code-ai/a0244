import streamlit as st
import time
def set_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a5c37 0%, #52c234 50%, #061700 100%);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .grow-animation {
        width: 20px;
        height: 100px;
        background: linear-gradient(to bottom, #4caf50, #1b5e20);
        margin: 0 auto;
        animation: grow 4s ease-in-out infinite;
        position: relative;
        z-index: 2;
    }
    @keyframes grow {
        0%, 100% { height: 100px; }
        50% { height: 150px; }
    }
    .leaf {
        width: 40px;
        height: 40px;
        background-color: #81c784;
        border-radius: 0 50% 50% 50%;
        transform: rotate(45deg);
        position: relative;
        left: 10px;
        top: -20px;
        z-index: 3;
    }
    .bubble {
        position: fixed;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.1);
        animation: float 8s infinite;
        z-index: 1;
    }
    @keyframes float {
        0% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
        100% { transform: translateY(0) rotate(360deg); }
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
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    </style>
    <div class="bubble" style="width: 40px; height: 40px; left: 10%; top: 20%;"></div>
    <div class="bubble" style="width: 20px; height: 20px; left: 20%; top: 80%;"></div>
    <div class="bubble" style="width: 30px; height: 30px; left: 80%; top: 15%;"></div>
    <div class="bubble" style="width: 50px; height: 50px; left: 90%; top: 50%;"></div>
    """, unsafe_allow_html=True)
def main():
    set_custom_css()  
    language = st.sidebar.selectbox("🌐 Select Language / மொழியை தேர்ந்தெடுக", ('English', 'தமிழ்'))
    if language == 'English':
        st.title("🌱 Plant Selection in Aquaponics 🐠")
        intro_text = """Welcome to the world of Plant Selection in Aquaponics! Choosing the right plants is crucial
        for a successful aquaponics system. Let's explore the factors to consider and some popular plant options."""
        factors_header = "🧐 Factors to Consider"
        factors = [
            "Nutrient Requirements 🧪",
            "pH Tolerance 📊",
            "Temperature Range 🌡",
            "Growth Rate 📈",
            "Root System 🌿",
            "Light Requirements ☀",
            "Market Demand 🛒"
        ]
        plant_header = "🌿 Popular Aquaponic Plant Categories"
        conclusion_header = "🌟 Conclusion"
        conclusion_text = """Selecting the right plants is key to a thriving aquaponics system. Consider factors like nutrient
        requirements, pH tolerance, and growth rate when making your choice. Remember, a diverse plant selection can lead to a more stable and productive aquaponics ecosystem!"""
    else:
        st.title("🌱 அக்வாபொனிக்ஸ் தாவர தேர்வு 🐠")
        intro_text = """அக்வாபொனிக்ஸ் தாவர தேர்வின் உலகத்திற்கு வரவேற்கிறோம்! சிறந்த தாவரங்களைத் தேர்ந்தெடுப்பது வெற்றிகரமான அக்வாபொனிக்ஸ்
        அமைப்புக்காக முக்கியமானது. கவனிக்க வேண்டிய காரியங்களைப் பற்றி மற்றும் பிரபலமான தாவர விருப்பங்களைப் பற்றி அறிந்துகொள்வோம்."""
        factors_header = "🧐 கவனிக்க வேண்டிய காரணிகள்"
        factors = [
            "நுண்ணுயிர் தேவைகள் 🧪",
            "pH சகிப்பு 📊",
            "வெப்பநிலை வரம்பு 🌡",
            "வளர்ச்சி வீதம் 📈",
            "வேர் அமைப்பு 🌿",
            "ஒளி தேவைகள் ☀",
            "சந்தை தேவைகள் 🛒"
        ]
        plant_header = "🌿 பிரபல அக்வாபொனிக்ஸ் தாவர வகைகள்"
        conclusion_header = "🌟 முடிவு"
        conclusion_text = """சிறந்த தாவரங்களைத் தேர்ந்தெடுப்பது துளிர்மிகு அக்வாபொனிக்ஸ் அமைப்புக்கு முக்கியமானது. நுண்ணுயிர் தேவைகள், pH சகிப்பு,
        மற்றும் வளர்ச்சி வீதம் போன்ற காரணிகளைப் பரிசீலிப்பதை மறக்காதீர்கள். பல்வேறு தாவரங்களைத் தேர்ந்தெடுப்பது அதிக நிலையான மற்றும் உற்பத்தி மிகுந்த
        அக்வாபொனிக்ஸ் அமைப்பிற்கு வழிவகுக்கும்!""" 
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.write(intro_text) 
    st.markdown('<div class="grow-animation"><div class="leaf"></div></div>', unsafe_allow_html=True) 
    st.header(factors_header)
    for factor in factors:
        st.write(f"• {factor}")
    st.header(plant_header)
    plant_categories = {
        "Leafy Greens 🥬": {
            "examples": ["Lettuce", "Spinach", "Kale", "Swiss Chard"],
            "pros": ["Fast growing", "High nutrient uptake", "Continuous harvest"],
            "cons": ["Lower market value", "Susceptible to pests"],
            "optimal_temp": "15-25°C (59-77°F)",
            "pH_range": "5.5-6.5"
        },
        "Herbs 🌿": {
            "examples": ["Basil", "Mint", "Cilantro", "Parsley"],
            "pros": ["High value crops", "Aromatic", "Compact growth"],
            "cons": ["May require frequent pruning", "Some have specific light requirements"],
            "optimal_temp": "18-30°C (64-86°F)",
            "pH_range": "5.5-6.5"
        },
        "Fruiting Plants 🍅": {
            "examples": ["Tomatoes", "Peppers", "Cucumbers", "Strawberries"],
            "pros": ["High yield", "Popular produce", "Vertical growing options"],
            "cons": ["Higher nutrient demands", "May require support structures"],
            "optimal_temp": "20-30°C (68-86°F)",
            "pH_range": "5.5-6.5"
        },
        "Root Vegetables 🥕": {
            "examples": ["Carrots", "Radishes", "Beets", "Turnips"],
            "pros": ["Utilize vertical space", "Good for media bed systems"],
            "cons": ["Longer growth cycle", "May compete with fish for nutrients"],
            "optimal_temp": "10-25°C (50-77°F)",
            "pH_range": "6.0-7.0"
        }
    }

    for category, details in plant_categories.items():
        with st.expander(category):
            st.write(f"*Examples:* {', '.join(details['examples'])}")
            st.write(f"*Optimal Temperature:* {details['optimal_temp']}")
            st.write(f"*pH Range:* {details['pH_range']}")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Pros ✅")
                for pro in details["pros"]:
                    st.write(f"• {pro}")
            with col2:
                st.subheader("Cons ❌")
                for con in details["cons"]:
                    st.write(f"• {con}")
        time.sleep(0.5)  

    st.markdown('</div>', unsafe_allow_html=True)

    
    st.header(conclusion_header)
    st.write(conclusion_text)

if __name__ == "__main__":
    main()