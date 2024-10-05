import streamlit as st
import time  
st.set_page_config(page_title="Aquaponics 101", page_icon="🌿", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-image: 
            linear-gradient(135deg, rgba(30,50,100,0.8) 0%, rgba(50,180,60,0.8) 100%),
            url("https://www.transparenttextures.com/patterns/paper-fibers.png");
        background-attachment: fixed;
        background-size: cover;
        color: white;
    }
    .stMarkdown a {
        color: #32CD32;  /* Keep link color */
    }
    .big-font {
        font-size: 22px;
        color: white;  /* Changed to default color */
    }
    .small-font {
        font-size: 18px;
        color: white;  /* Changed to default color */
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stImage {
        border-radius: 10px;
        border: 2px solid #32CD32;
    }
    .fade-in {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
content = {
    "english": {
        "title": "🌿 Aquaponics: The Future of Sustainable Farming 🐟",
        "definition": """
        Aquaponics is a sustainable method of farming that merges *aquaculture* (raising fish) and *hydroponics* (growing plants without soil). In this ecosystem:
        - Fish produce nutrient-rich waste.
        - Plants absorb these nutrients, cleaning the water for the fish.
        It's an amazing cycle of life! 🌱🐠
        """,
        "how_it_works": [
            "Fish release waste into the water.",
            "Bacteria convert waste into nutrients for plants.",
            "Plants filter and clean the water.",
            "Clean water is pumped back to the fish tank."
        ],
        "benefits": [
            "💧 *Water Conservation:* Uses 90% less water than traditional farming.",
            "🌱 *No Chemical Fertilizers:* Fish provide natural nutrients for plants.",
            "📆 *Year-Round Production:* Can be operated in any season with controlled environments.",
            "🔄 *Recycling:* Efficiently reuses water, reducing waste.",
            "🍽 *Dual Production:* Grows both fish and fresh produce in one system."
        ],
        "components": {
            "Fish Tank": "The tank where fish live and produce nutrient-rich waste.",
            "Grow Beds": "Beds where plants grow and absorb nutrients from fish waste.",
            "Water Pump": "Circulates water between the fish tank and grow beds.",
            "Filtration System": "Filters solid waste and aerates water for fish."
        },
        "types": {
            "1. Media-Based Aquaponics": "Utilizes a solid medium, like gravel or clay pellets, for plant roots.",
            "2. Nutrient Film Technique (NFT)": "Involves a thin film of nutrient-rich water flowing over plant roots.",
            "3. Deep Water Culture (DWC)": "Plants float on rafts in a nutrient-rich solution with their roots submerged.",
            "4. Vertical Aquaponics": "Incorporates vertical growing systems to maximize space usage.",
            "5. Hybrid Aquaponics": "Combines elements from different systems for improved efficiency."
        },
        "footer": "🌾 Join the #SustainableFarming Revolution! 🌾",
        "final_text": "📊 Your Sustainable Journey Starts Now! Tracking your progress in sustainability is important. Check how far you’ve come:"
    },
    "tamil": {
        "title": "🌿 நீர்வள வளர்ப்பு: நிலையான வேளாண்மையின் எதிர்காலம் 🐟",
        "definition": """
        நீர்வள வளர்ப்பு என்பது *மீன் வளர்ப்பு* மற்றும் *மண்ணில் இல்லாமல் தாவரங்களை வளர்ப்பது* ஆகியவற்றைப் பெற்றுள்ள நிலையான விவசாய முறை ஆகும். இந்த экосிஸ்டத்தில்:
        - மீன்கள் ஊட்டச்சத்துள்ள கழிவுகளை உற்பத்தி செய்கின்றன.
        - தாவரங்கள் இந்த ஊட்டச்சத்துகளை உறிஞ்சிக்கொண்டு, மீன்களுக்கு நீரை சுத்தம் செய்கின்றன.
        இது ஒரு அற்புதமான வாழ்க்கையின் சுற்றத்தை உருவாக்குகிறது! 🌱🐠
        """,
        "how_it_works": [
            "மீன்கள் நீலில் கழிவுகளை வெளியிடுகின்றன.",
            "பாக்டீரியா கழிவுகளை தாவரங்களுக்கு ஊட்டச்சத்துக்களாக மாற்றுகின்றன.",
            "தாவரங்கள் நீரை சுத்தம் செய்கின்றன.",
            "சுத்தமான நீர் மீன் தொட்டிக்கு மீண்டும் தள்ளப்படுகிறது."
        ],
        "benefits": [
            "💧 *நீர் சேமிப்பு:* பாரம்பரிய விவசாயத்திற்கு விட 90% குறைவான நீரை பயன்படுத்துகிறது.",
            "🌱 *ரசாயன உரங்களுக்கு தேவையில்லை:* மீன்கள் தாவரங்களுக்கு இயற்கையான ஊட்டச்சத்துக்களை வழங்குகின்றன.",
            "📆 *வருடத்தின் முழு காலத்தின் உற்பத்தி:* கட்டுப்பாட்டில் உள்ள சூழலில் எந்த பருவத்திலும் இயக்கலாம்.",
            "🔄 *மறுசுழற்சி:* நீரை திறம்பட மீண்டும் பயன்படுத்துகிறது, கழிவுகளை குறைக்கும்.",
            "🍽 *இரட்டை உற்பத்தி:* மீன்கள் மற்றும் புதிய விளைச்சல்களை ஒரே அமைப்பில் வளர்க்கிறது."
        ],
        "components": {
            "மீன் தொட்டி": "மீன்கள் வாழ்ந்து ஊட்டச்சத்துள்ள கழிவுகளை உற்பத்தி செய்யும் தொட்டி.",
            "வளர்ப்பு படுக்கைகள்": "தாவரங்கள் வளர்ந்து மீன் கழிவுகளிலிருந்து ஊட்டச்சத்துகளை உறிஞ்சும் இடங்கள்.",
            "நீர்ப்பம்ப்": "மீன் தொட்டி மற்றும் வளர்ப்பு படுக்கைகள் இடையே நீரை சுழல்த்துகிறது.",
            "மாசு நீக்குதல் முறை": "கடுமையான கழிவுகளை வடிகட்டுகிறது மற்றும் மீன்களுக்கு நீரை காற்றோட்டம் செய்கிறது."
        },
        "types": {
            "1. மிதி அடிப்படையிலான நீர்வள வளர்ப்பு": "தாவரருத்து மையமாக கற்கள் அல்லது clay பந்து போன்ற ஒரு மிதியைப் பயன்படுத்துகிறது.",
            "2. ஊட்டச்சத்துப் படலம் தொழில்நுட்பம் (NFT)": "தாவரருத்துகளில் ஊட்டச்சத்துள்ள நீர் மிதிந்த படலமாக ஓடுகிறது.",
            "3. ஆழ நீர் கலவைக் தொழில்நுட்பம் (DWC)": "தாவரங்கள் படகு வடிவில் நிற்கும் ஊட்டச்சத்துள்ள நீரின் ஆழத்தில் இருக்கின்றன.",
            "4. ஏறக்குறைய உள்ள நீர்வள வளர்ப்பு": "இடத்தை அதிகப்படியான பயனடைய புதிய மூலதனங்களைச் சேர்க்கிறது.",
            "5. கலவையான நீர்வள வளர்ப்பு": "சிறந்த செயல்திறனை முன்னேற்ற கலவையாக்கும் வகையில்."
        },
        "footer": "🌾 #நிலையானவிவசாயம் மாற்றத்தை இணைக்கவும்! 🌾",
        "final_text": "📊 உங்கள் நிலையான பயணம் இன்று தொடங்குகிறது! உங்கள் நிலைத்தன்மைக்கு முன்னேற்றத்தை கண்காணிக்க முக்கியம். நீங்கள் எவ்வளவு முன்னேறியிருக்கிறீர்கள் என்பதைப் பாருங்கள்:"
    }
}
lang = st.sidebar.radio("Select Language / மொழியைத் தேர்ந்தெடுக்கவும்", ["English", "தமிழ்"])
lang_key = 'english' if lang == 'English' else 'tamil'
st.markdown(f"<h1 class='fade-in'>{content[lang_key]['title']}</h1>", unsafe_allow_html=True)
st.header("What is Aquaponics? 🤔" if lang_key == 'english' else "நீர்வள வளர்ப்பு என்ன? 🤔")
st.markdown(content[lang_key]["definition"], unsafe_allow_html=True)
st.header("🔄 How Aquaponics Works (Animated)" if lang_key == 'english' else "🔄 நீர்வள வளர்ப்பு எவ்வாறு செயல்படுகிறது (எண்ணிக்கை)")
steps = content[lang_key]["how_it_works"]
progress_bar = st.progress(0)
step_text = st.empty()
for i, step in enumerate(steps):
    progress_bar.progress((i + 1) * 25)
    step_text.markdown(f"<p class='small-font fade-in'>{step}</p>", unsafe_allow_html=True)
    time.sleep(1)
progress_bar.empty()
step_text.markdown("<p class='small-font fade-in'>Aquaponics is a beautifully symbiotic cycle! 🌍</p>", unsafe_allow_html=True)
st.header("🌟 Benefits of Aquaponics" if lang_key == 'english' else "🌟 நீர்வள வளர்ப்பின் நன்மைகள்")
for benefit in content[lang_key]["benefits"]:
    st.markdown(f"<p class='small-font fade-in'>{benefit}</p>", unsafe_allow_html=True)
st.header("🔧 Key Components" if lang_key == 'english' else "🔧 முக்கிய கூறுகள்")
for component, description in content[lang_key]["components"].items():
    st.markdown(f"<strong>{component}</strong>: {description}", unsafe_allow_html=True)
st.header("🔍 Types of Aquaponics" if lang_key == 'english' else "🔍 நீர்வள வளர்ப்பின் வகைகள்")
for type_, description in content[lang_key]["types"].items():
    st.markdown(f"<p class='small-font fade-in'>{type_}: {description}</p>", unsafe_allow_html=True)
st.markdown(f"<h4 class='fade-in'>{content[lang_key]['footer']}</h4>", unsafe_allow_html=True)
st.markdown(f"<p class='small-font fade-in'>{content[lang_key]['final_text']}</p>", unsafe_allow_html=True)