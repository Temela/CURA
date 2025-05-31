
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="CURA Health Monitor", layout="wide")

st.title("🧓 CURA: Compassion-Driven Health Monitor for Elderly Clergy")

st.markdown("Track health trends, mood, and reflection insights across elderly clergy in a human-centered, ethical system.")

# Load data
df = pd.read_csv("cura_45_elderly_health_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Sidebar filters
st.sidebar.header("Filters")
selected_user = st.sidebar.selectbox("Select User ID", sorted(df["user_id"].unique()))
user_df = df[df["user_id"] == selected_user]

# Line chart: heart rate over time
st.subheader(f"Heart Rate Over Time for User {selected_user}")
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=user_df, x="date", y="heart_rate", ax=ax1, marker="o", color="red")
ax1.set_ylabel("Heart Rate (bpm)")
ax1.set_xlabel("Date")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Mood distribution
st.subheader(f"Mood Frequency for User {selected_user}")
fig2, ax2 = plt.subplots(figsize=(6, 3))
sns.countplot(data=user_df, x="mood", order=user_df["mood"].value_counts().index, palette="Set2", ax=ax2)
ax2.set_ylabel("Count")
ax2.set_xlabel("Mood")
st.pyplot(fig2)

# Reflection summary
st.subheader(f"Spiritual Reflections for User {selected_user}")
st.dataframe(user_df[["date", "spiritual_reflection"]].sort_values("date", ascending=False).reset_index(drop=True))
