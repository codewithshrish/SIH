import streamlit as Streamlit

# Title
Streamlit.subheader("Stay Ahead of Crop Diseases with Cutting-Edge AI Technology!")

#navigation
Streamlit.sidebar.markdown("### Navigation")
Streamlit.sidebar.markdown("Home")
Streamlit.sidebar.markdown("About Us")

# Services section in the sidebar
Streamlit.sidebar.markdown("### Services")
with Streamlit.sidebar.expander("Select a Service"):
    user_choice = Streamlit.selectbox("", ["Disease Detection", "Crop Management", "AI Analytics"])
    Streamlit.write(f"You selected: {user_choice}")

Streamlit.sidebar.markdown("Resources")
Streamlit.sidebar.markdown("Contact Us")

# Main page
if user_choice == "Disease Detection":
    Streamlit.markdown("🦠 *AI-Powered Disease Detection*")
    Streamlit.write("Our cutting-edge technology helps in early detection and management of crop diseases.")
elif user_choice == "Crop Management":
    Streamlit.markdown("🚜 *Comprehensive Crop Management*")
    Streamlit.write("Optimize your crop management with our advanced tools and insights.")
elif user_choice == "AI Analytics":
    Streamlit.markdown("📊 *Advanced AI Analytics*")
    Streamlit.write("Leverage AI-driven analytics for better decision-making and higher yields.")

# Footer
Streamlit.markdown("---")
Streamlit.write("© 2024 AI-Crop. All rights reserved.")