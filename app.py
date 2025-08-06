import pandas as pd
import streamlit as st

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_excel("online_course_recommendation_v2.xlsx")

df = load_data()

# Title
st.title("🎓 Online Course Recommender")

# Sidebar for extra options
st.sidebar.header("🔧 Filter Options")
show_top_n = st.sidebar.slider("How many top courses to show?", min_value=5, max_value=20, value=10)
sort_by = st.sidebar.selectbox("Sort courses by:", ["rating", "feedback_score", "enrollment_numbers"])

# User Input
keyword = st.text_input("🔍 Enter your area of interest (e.g., Python, AI, Data)").lower()
difficulty = st.selectbox("🎚️ Select your preferred difficulty level", ["Beginner", "Intermediate", "Advanced"])
show_instructor = st.checkbox("Show instructor details", value=True)
show_feedback = st.checkbox("Show feedback score", value=True)

# Filter logic
if keyword:
    filtered = df[df['course_name'].str.lower().str.contains(keyword, na=False)]
    filtered = filtered.sort_values(by=[sort_by, 'rating', 'feedback_score', 'enrollment_numbers'], ascending=False).head(show_top_n)

    if not filtered.empty:
        result = filtered[filtered['difficulty_level'] == difficulty]

        if not result.empty:
            st.subheader(f"🎯 Recommended {difficulty} Courses for '{keyword.title()}':")
            display_cols = ['course_name', 'difficulty_level']
            if show_instructor:
                display_cols.append('instructor')
            display_cols.append('rating')
            if show_feedback:
                display_cols.append('feedback_score')
            st.dataframe(result[display_cols])
            # Download option
            csv = result[display_cols].to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download recommendations as CSV",
                data=csv,
                file_name='recommended_courses.csv',
                mime='text/csv',
            )
        else:
            st.warning(f"No {difficulty} level courses found in top results.")
    else:
        st.error("❌ No matching courses found. Try a different keyword.")

# Show all courses option
if st.checkbox("Show all available courses"):
    st.write(df.head(50))