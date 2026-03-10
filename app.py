import streamlit as st
import pandas as pd
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Male' Price Tracker",
    page_icon="🇲🇻",
    layout="centered"
)

# --- APP STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_headers=True)

# --- HEADER ---
st.title("🇲🇻 Male' Price Finder")
st.subheader("Compare grocery prices in Malé")

# --- SEARCH INTERFACE ---
query = st.text_input("What are you looking for?", placeholder="e.g., Tuna, Eggs, Rice, Milk")

# --- DATA LOGIC ---
def get_prices(item):
    item = item.lower()
    
    # Representative data for Malé retailers
    data = [
        {"Store": "STO People's Choice", "Item": f"{item.capitalize()}", "Price": 14.50, "Category": "Essential"},
        {"Store": "Redwave", "Item": f"{item.capitalize()}", "Price": 16.00, "Category": "Retail"},
        {"Store": "Villa Mart", "Item": f"{item.capitalize()}", "Price": 15.75, "Category": "Retail"},
        {"Store": "Local Market", "Item": f"{item.capitalize()} (Local)", "Price": 12.00, "Category": "Fresh"},
        {"Store": "GannaMart", "Item": f"{item.capitalize()}", "Price": 17.00, "Category": "Online"},
    ]
    
    # Simulating real-world price variations
    for entry in data:
        entry["Price"] += round(random.uniform(-1.0, 2.0), 2)
        
    return pd.DataFrame(data).sort_values(by="Price")

# --- RESULTS DISPLAY ---
if query:
    with st.spinner(f"Searching Malé stores for {query}..."):
        df = get_prices(query)
        
        # Best Deal Highlight
        best_price = df.iloc[0]
        st.success(f"🏆 **Cheapest Option:** {best_price['Price']} MVR at **{best_price['Store']}**")
        
        # Comparison Table
        st.dataframe(df, use_container_width=True, hide_index=True)

# --- EXTERNAL LINKS ---
st.divider()
st.info("💡 **Tip:** Check **Agu Magu** for government-verified essential prices.")

col1, col2 = st.columns(2)
with col1:
    st.link_button("Agu Magu Portal", "https://agumagu.trade.gov.mv")
with col2:
    st.link_button("STO eSTOre", "https://sto.mv/eSTOre")

st.caption("Note: Prices are estimates. Please check the store for exact rates.")
