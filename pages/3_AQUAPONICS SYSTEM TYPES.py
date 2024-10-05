import streamlit as st
import time
def set_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e88e5, #43a047);
        background-attachment: fixed;
    }
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .water-animation {
        width: 100%;
        height: 100px;
        background: linear-gradient(to right, #81d4fa, #a5d6a7);
        animation: wave 5s ease-in-out infinite;
    }
    @keyframes wave {
        0%, 100% { clip-path: polygon(0% 50%, 16% 45%, 33% 50%, 50% 60%, 66% 65%, 83% 60%, 100% 50%, 100% 100%, 0% 100%); }
        50% { clip-path: polygon(0% 60%, 16% 65%, 33% 60%, 50% 50%, 66% 45%, 83% 50%, 100% 55%, 100% 100%, 0% 100%); }
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
    if 'language' not in st.session_state:
        st.session_state.language = 'English'  
    def toggle_language():
        st.session_state.language = 'Tamil' if st.session_state.language == 'English' else 'English'
    st.sidebar.checkbox("தமிழ்", value=(st.session_state.language == 'Tamil'), on_change=toggle_language) 
    content = {
        'title': {
            'English': "Aquaponics System Types",
            'Tamil': "அகுவாப்பொனிக்ஸ் அமைப்பு வகைகள்"
        },
        'header': {
            'English': "Explore Different Aquaponics Systems",
            'Tamil': "வேறுபட்ட அகுவாப்பொனிக்ஸ் அமைப்புகளை ஆராயுங்கள்"
        },
        'systems': {
            "Media-based Systems": {
                'English': "Uses a grow medium like gravel or clay pebbles to support plant roots.",
                'Tamil': "மணல் அல்லது களிமண் பேபிள்கள் போன்ற வளர்ப்பு மையத்தைக் கையாள்கிறது."
            },
            "Deep Water Culture (DWC)": {
                'English': "Plants float on water with their roots submerged.",
                'Tamil': "மூலிகைகள் நீரில் மிதக்கின்றன, அவற்றின் மூலங்கள் நீரில் மிதக்கின்றன."
            },
            "Nutrient Film Technique (NFT)": {
                'English': "A thin film of water flows over plant roots in channels.",
                'Tamil': "ஒரு வெளியில் பாயும் தண்ணீரின் பருத்தி செடியின் மூலங்களில் ஓடியும்."
            },
            "Vertical Systems": {
                'English': "Utilize vertical space for growing plants, often in towers or stacked layers.",
                'Tamil': "செடிகள் வளர்க்க உன்னதமாக இருக்கும் இடத்தை பயன்படுத்துகிறது, பெரும்பாலும் கோபுரங்கள் அல்லது அடுக்குகளின் அடிப்படையில்."
            }
        },
        'benefits_header': {
            'English': "Benefits of Aquaponics",
            'Tamil': "அகுவாப்பொனிக்ஸ் நன்மைகள்"
        },
        'benefits': {
            'English': [
                "Water conservation",
                "Organic food production",
                "Space efficiency",
                "Year-round growing"
            ],
            'Tamil': [
                "நீர் மிச்சம்",
                "உள்நாட்டு உணவு உற்பத்தி",
                "இடம் திறன்",
                "வருடம் முழுவதும் வளர்ச்சி"
            ]
        }
    }
    st.title(content['title'][st.session_state.language])  
    st.markdown('<div class="water-animation"></div>', unsafe_allow_html=True)
    st.header(content['header'][st.session_state.language])   
    for system, descriptions in content['systems'].items():
        with st.expander(system):
            st.write(descriptions[st.session_state.language])
            time.sleep(0.5)  
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.subheader(content['benefits_header'][st.session_state.language])
    st.write("\n".join(content['benefits'][st.session_state.language]))
    st.markdown('</div>', unsafe_allow_html=True)
if __name__ == "__main__":
    main()