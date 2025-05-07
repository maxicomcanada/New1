import streamlit as st
import pandas as pd

st.title("📥 Maxicom Email Intelligence Dashboard")

# Load leads
df = pd.read_csv("leads.csv")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filter Leads")
    intent = st.multiselect("Intent", df["Intent"].dropna().unique(), default=list(df["Intent"].dropna().unique()))
    brand = st.multiselect("Brand", df["Brand"].dropna().unique(), default=list(df["Brand"].dropna().unique()))
    condition = st.multiselect("Condition", df["Condition"].dropna().unique(), default=list(df["Condition"].dropna().unique()))

# Apply filters
filtered_df = df[
    (df["Intent"].isin(intent)) &
    (df["Brand"].isin(brand)) &
    (df["Condition"].isin(condition))
]

# Search box
search = st.text_input("Search product or part number")
if search:
    filtered_df = filtered_df[filtered_df.apply(
        lambda row: search.lower() in str(row["Product"]).lower() or search.lower() in str(row["Part Number"]).lower(),
        axis=1
    )]

# Show table
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
