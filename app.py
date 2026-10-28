import streamlit as st
import pandas as pd
from datetime import datetime, date

st.set_page_config(
    page_title="AI Smart Time Assistant",
    page_icon="⏰",
    layout="wide"
)

st.title("⏰ AI Smart Time Assistant")
st.write("Manage your tasks, deadlines, and priorities.")

# Current Date and Time
now = datetime.now()

st.subheader("Current Date & Time")
st.write(now.strftime("%A, %d %B %Y | %I:%M:%S %p"))

st.divider()

# Task Input
st.subheader("Add a Task")

task_name = st.text_input("Enter Task Name")

deadline = st.date_input(
    "Select Deadline",
    min_value=date.today()
)

importance = st.selectbox(
    "Select Importance",
    ["High", "Medium", "Low"]
)

# Analyze Task
if st.button("Analyze Task"):

    if task_name.strip():

        days_left = (deadline - date.today()).days

        # Determine Urgency
        if days_left == 0:
            urgency = "Due Today"
        elif days_left <= 2:
            urgency = "Urgent"
        else:
            urgency = "Upcoming"

        # Determine Priority
        if importance == "High" or days_left <= 2:
            priority = "High"
        elif importance == "Medium":
            priority = "Medium"
        else:
            priority = "Low"

        # Display Results
        st.success("Task analyzed successfully!")

        col1, col2, col3 = st.columns(3)

        col1.metric("Days Remaining", days_left)
        col2.metric("Urgency", urgency)
        col3.metric("Priority", priority)

        st.write("### Task Details")
        st.write("**Task Name:**", task_name)
        st.write("**Deadline:**", deadline.strftime("%d-%m-%Y"))
        st.write("**Importance:**", importance)

        # Recommendation
        st.write("### Recommendation")

        if priority == "High":
            st.warning("Complete this task first!")
        elif priority == "Medium":
            st.info("Schedule this task soon.")
        else:
            st.success("You can complete this task later.")

    else:
        st.error("Please enter a task name.")

st.divider()

st.caption(
    "Built with Python, Streamlit, Pandas, and datetime."
)

