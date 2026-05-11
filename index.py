import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="CGPA Calculator",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""

<style>

.main {
    background-color: #0f172a;
}

h1, h2, h3 {
    color: #38bdf8;
}

.stNumberInput input {
    background-color: #1e293b;
    color: white;
}

.grade-box {
    background: #1e293b;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-top: 20px;
}

</style>

""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.title("🎓 Professional CGPA & GPA Calculator")

st.write("Academic Analytics Dashboard")

st.divider()

# ==========================================
# GPA INPUTS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    sem1 = st.number_input("Semester 1 GPA", 0.0, 10.0, 8.5)
    sem2 = st.number_input("Semester 2 GPA", 0.0, 10.0, 8.7)

with col2:
    sem3 = st.number_input("Semester 3 GPA", 0.0, 10.0, 8.9)
    sem4 = st.number_input("Semester 4 GPA", 0.0, 10.0, 9.1)

with col3:
    sem5 = st.number_input("Semester 5 GPA", 0.0, 10.0, 9.0)
    sem6 = st.number_input("Semester 6 GPA", 0.0, 10.0, 9.2)

with col4:
    sem7 = st.number_input("Semester 7 GPA", 0.0, 10.0, 9.3)
    sem8 = st.number_input("Semester 8 GPA", 0.0, 10.0, 9.4)

gpas = [
    sem1, sem2, sem3, sem4,
    sem5, sem6, sem7, sem8
]

# ==========================================
# CALCULATE
# ==========================================

if st.button("Calculate CGPA"):

    total = sum(gpas)

    cgpa = total / len(gpas)

    percentage = cgpa * 9.5

    highest = max(gpas)

    # ======================================
    # GRADE
    # ======================================

    if cgpa >= 9:
        grade = "O"
        performance = "Outstanding"

    elif cgpa >= 8:
        grade = "A+"
        performance = "Excellent"

    elif cgpa >= 7:
        grade = "A"
        performance = "Very Good"

    elif cgpa >= 6:
        grade = "B"
        performance = "Good"

    else:
        grade = "C"
        performance = "Needs Improvement"

    # ======================================
    # METRICS
    # ======================================

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total GPA", f"{total:.2f}")

    c2.metric("CGPA", f"{cgpa:.2f}")

    c3.metric("Percentage", f"{percentage:.2f}%")

    c4.metric("Highest GPA", highest)

    # ======================================
    # GRADE BOX
    # ======================================

    st.markdown(f"""

    <div class="grade-box">

    <h1>{grade}</h1>

    <h3>{performance}</h3>

    </div>

    """, unsafe_allow_html=True)

    # ======================================
    # TABLE
    # ======================================

    st.subheader("📊 Semester Performance")

    semester_data = {
        "Semester": [
            "Semester 1",
            "Semester 2",
            "Semester 3",
            "Semester 4",
            "Semester 5",
            "Semester 6",
            "Semester 7",
            "Semester 8"
        ],
        "GPA": gpas
    }

    st.table(semester_data)

    # ======================================
    # PROGRESS BAR
    # ======================================

    st.subheader("🎯 CGPA Progress")

    st.progress(min(cgpa / 10, 1.0))

    # ======================================
    # STATUS
    # ======================================

    if cgpa >= 9:

        st.success("Outstanding academic performance!")

    elif cgpa >= 8:

        st.info("Excellent performance!")

    elif cgpa >= 7:

        st.warning("Good performance. Keep improving!")

    else:

        st.error("Needs improvement!")

st.divider()

st.caption("Professional CGPA Calculator • Streamlit + Python")
