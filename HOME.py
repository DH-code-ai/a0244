import streamlit as st

PAGE_TITLE = "Aquaponics: The Future of Sustainable Farming"
PAGE_ICON = "🌱"
AQUAPONICS_ASSOCIATION_URL = "https://aquaponicsassociation.org/"

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
body {
    font-family: 'Poppins', sans-serif;
    background-color: #4169E1; /* Royal Blue */
    color: #ffffff;
}
h1, h2, h3 {
    font-weight: 600;
}
p, li {
    font-weight: 300;
    line-height: 1.6;
}
.stButton>button {
    color: #ffffff;
    background-color: #4CAF50;
    border-radius: 20px;
    padding: 10px 24px;
    font-size: 16px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}
.stApp {
    background-color: transparent;
    padding: 20px;
}
@keyframes fadeIn { 
    0% { opacity: 0; } 
    100% { opacity: 1; }
}
.fade-in {
    animation: fadeIn 1.5s;
}
</style>
"""

# Tamil translations for the content
tamil_translations = {
    "Welcome to the World of Aquaponics!": "அக்வாபொனிக்ஸின் உலகத்திற்கு வரவேற்கிறோம்!",
    "Cultivating Sustainability, One Fish at a Time": "ஒவ்வொரு மீனும், நுண்ணிய சந்துல் வளர்க்கும்",
    "In the circle of life, every drop nurtures growth:Where fish and plants dance in harmony.":"வாழ்க்கையின் வட்டத்தில், ஒவ்வொரு துளியும் வளர்ச்சியை வளர்க்கிறது.அக்வாபோனிக்ஸ்: மீன் மற்றும் தாவரங்கள் இணக்கமாக நடனமாடும் இடம்",

    "The Aquaponics Revolution": "அக்வாபொனிக்ஸ் புரட்சி",
    "Aquaponics is more than just a farming technique; it's a philosophy of sustainable living.": "அக்வாபொனிக்ஸ் என்பது ஒரு வேளாண் தொழில்நுட்பத்தை விட அதிகம்; இது நிலைத்திருக்கும் வாழ்வின் தத்துவம்.",
    "Why Aquaponics Matters": "ஏன் அக்வாபொனிக்ஸ் முக்கியம்",
    "Conserves water": "நீரை பாதுகாக்கிறது",
    "Produces organic food": "உலகசந்தைப்படுத்தப்பட்ட உணவு உற்பத்தி",
    "Supports local ecosystems": "உள்ளூர் உயிரியல் அமைப்புகளுக்கு ஆதரவளிக்கிறது",
    "Perfect for urban farming": "நகர்ப்புற வேளாண் சிறந்தது",
    "Reduces carbon footprint": "கார்பன் கால் அச்சு குறைக்கிறது",
    "Promotes sustainable living": "நிலையான வாழ்க்கையை ஊக்குவிக்கிறது",
    "Join the Movement!": "இயக்கத்தில் இணையுங்கள்!",
    "Ready to dive into the world of aquaponics?": "அக்வாபொனிக்ஸ் உலகத்தில் மூழ்கத் தயார்?",
    "Created with 💚 by Aquaponics Enthusiasts": "அக்வாபொனிக்ஸ் ஆர்வலர்களால் 💚 உடன் உருவாக்கப்பட்டது"
}

def load_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

def toggle_tamil_mode():
    st.session_state.tamil_mode = not st.session_state.tamil_mode

def get_mode_button_text():
    return "Dark Mode" if not st.session_state.dark_mode else "Bright Mode"

def get_language_button_text():
    return "தமிழ்" if not st.session_state.tamil_mode else "English"

def render_header():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    if st.session_state.tamil_mode:
        st.title("🌱 " + tamil_translations["Welcome to the World of Aquaponics!"])
        st.subheader(tamil_translations["Cultivating Sustainability, One Fish at a Time"])
    else:
        st.title("🌱 Welcome to the World of Aquaponics!")
        st.subheader("Cultivating Sustainability, One Fish at a Time")
    st.markdown('</div>', unsafe_allow_html=True)

def render_inspirational_quote():
    st.markdown(
        """
        <div class="fade-in" style='padding: 20px; background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; text-align: center;'>
            <h3>"In the circle of life, every drop nurtures growth.<br>Aquaponics: Where fish and plants dance in harmony."</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_aquaponics_revolution():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    if st.session_state.tamil_mode:
        st.markdown(f"## 🌊 {tamil_translations['The Aquaponics Revolution']}")
        st.write(tamil_translations["Aquaponics is more than just a farming technique; it's a philosophy of sustainable living."])
    else:
        st.markdown("## 🌊 The Aquaponics Revolution")
        st.write(
            "Aquaponics is more than just a farming technique; it's a philosophy of sustainable living. "
            "By combining aquaculture (raising fish) and hydroponics (growing plants in water), we create "
            "a symbiotic ecosystem that mimics nature's perfect balance."
        )
    st.markdown('</div>', unsafe_allow_html=True)

def render_why_aquaponics_matters():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    if st.session_state.tamil_mode:
        st.markdown(f"## 🐠 {tamil_translations['Why Aquaponics Matters']}")
    else:
        st.markdown("## 🐠 Why Aquaponics Matters")

    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.tamil_mode:
            st.markdown(f"- 🌍 {tamil_translations['Conserves water']}")
            st.markdown(f"- 🌱 {tamil_translations['Produces organic food']}")
            st.markdown(f"- 🐟 {tamil_translations['Supports local ecosystems']}")
        else:
            st.markdown(
                """
                - 🌍 Conserves water
                - 🌱 Produces organic food
                - 🐟 Supports local ecosystems
                """
            )
    with col2:
        if st.session_state.tamil_mode:
            st.markdown(f"- 🏙️ {tamil_translations['Perfect for urban farming']}")
            st.markdown(f"- 🌿 {tamil_translations['Reduces carbon footprint']}")
            st.markdown(f"- 💚 {tamil_translations['Promotes sustainable living']}")
        else:
            st.markdown(
                """
                - 🏙️ Perfect for urban farming
                - 🌿 Reduces carbon footprint
                - 💚 Promotes sustainable living
                """
            )
    st.markdown('</div>', unsafe_allow_html=True)

def render_call_to_action():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    if st.session_state.tamil_mode:
        st.markdown(f"## 🌟 {tamil_translations['Join the Movement!']}")
        st.write(tamil_translations["Ready to dive into the world of aquaponics?"])
    else:
        st.markdown("## 🌟 Join the Movement!")
        st.write(
            "Ready to dive into the world of aquaponics? Start your journey today and be part of the solution "
            "for a greener, more sustainable future!"
        )
    st.markdown(f'<a href="{AQUAPONICS_ASSOCIATION_URL}" target="_blank"><button style="color: #ffffff; background-color: #4CAF50; border-radius: 20px; padding: 10px 24px; border: none; cursor: pointer;">Join Community</button></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_footer():
    st.markdown(
        """
        <div class="fade-in" style='text-align: center; padding: 20px;'>
            <p>Created with 💚 by Aquaponics Enthusiasts</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def set_background_color():
    if st.session_state.dark_mode:
        st.markdown(
            """
            <style>
            body { background-color: #000000; }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            body { background-color: #4169E1; }
            </style>
            """,
            unsafe_allow_html=True
        )

def main():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

    # Initialize session state
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    if 'tamil_mode' not in st.session_state:
        st.session_state.tamil_mode = False

    load_css()
    set_background_color()

    # Sidebar
    with st.sidebar:
        st.button(get_mode_button_text(), on_click=toggle_dark_mode, key="dark_mode_button")
        st.button(get_language_button_text(), on_click=toggle_tamil_mode, key="tamil_mode_button")

    # Main content
    render_header()
    render_inspirational_quote()
    render_aquaponics_revolution()
    render_why_aquaponics_matters()
    render_call_to_action()
    render_footer()

if __name__ == "__main__":
    main()


    import streamlit as st

# ... (previous code remains the same)

# Add the Tamil translation for the quote to the tamil_translations dictionary
tamil_translations = {
    # ... (previous translations)
    "In the circle of life, every drop nurtures growth. Aquaponics: Where fish and plants dance in harmony.": "வாழ்க்கை வட்டத்தில், ஒவ்வொரு துளியும் வளர்ச்சியை வளர்க்கிறது. அக்வாபோனிக்ஸ்: மீன்களும் தாவரங்களும் இணக்கமாக நடனமாடும் இடம்."
}

# ... (other functions remain the same)

def render_inspirational_quote():
    quote = "In the circle of life, every drop nurtures growth. Aquaponics: Where fish and plants dance in harmony."
    translated_quote = tamil_translations[quote] if st.session_state.tamil_mode else quote
    
    st.markdown(
        f"""
        <div class="fade-in" style='padding: 20px; background-color: rgba(255, 255, 255, 0.1); border-radius: 10px; text-align: center;'>
            <h3>"{translated_quote}"</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# ... (rest of the code remains the same)