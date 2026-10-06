
import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Hackathon Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    );
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    color: #cbd5e1;
    font-size: 18px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    background-color: white;
    margin-bottom: 15px;
}

.metric-title {
    font-size: 14px;
    color: #64748b;
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🚀 Hackathon")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📊 Analytics",
            "🔍 Investigation",
            "⚙️ Settings"
        ]
    )

    st.markdown("---")

    st.caption("Hackathon Project")
    st.caption("Built with Python + Streamlit")


# -----------------------------
# DASHBOARD
# -----------------------------

if page == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">

    <h1>🚀 Hackathon Dashboard</h1>

    <p>
    A smart interactive platform built with Python and Streamlit.
    </p>

    </div>
    """, unsafe_allow_html=True)


    # Metrics

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Users",
            "12,540",
            "+8.2%"
        )

    with col2:
        st.metric(
            "Active Users",
            "8,421",
            "+5.4%"
        )

    with col3:
        st.metric(
            "Alerts",
            "127",
            "-12%"
        )

    with col4:
        st.metric(
            "System Score",
            "94.6%",
            "+2.1%"
        )


    st.markdown("###")


    # Main content

    left, right = st.columns([2, 1])

    with left:

        st.subheader("📊 System Overview")

        chart_data = {
            "Day": [
                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"
            ],
            "Activity": [
                420,
                510,
                480,
                620,
                710,
                650,
                780
            ]
        }

        st.line_chart(
            chart_data,
            x="Day",
            y="Activity"
        )


    with right:

        st.subheader("⚡ Quick Actions")

        if st.button(
            "🔍 Investigate",
            use_container_width=True
        ):
            st.info("Investigation module opened.")

        if st.button(
            "📊 View Analytics",
            use_container_width=True
        ):
            st.info("Analytics module opened.")

        if st.button(
            "📥 Export Report",
            use_container_width=True
        ):
            st.success("Report generation started.")


# -----------------------------
# ANALYTICS
# -----------------------------

elif page == "📊 Analytics":

    st.title("📊 Analytics")

    st.write(
        "Detailed analytics and visualizations "
        "will appear here."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Activity")

        st.bar_chart(
            {
                "Activity": [
                    120,
                    180,
                    150,
                    220,
                    300
                ]
            }
        )

    with col2:

        st.subheader("Performance")

        st.area_chart(
            {
                "Performance": [
                    60,
                    72,
                    68,
                    85,
                    94
                ]
            }
        )


# -----------------------------
# INVESTIGATION
# -----------------------------

elif page == "🔍 Investigation":

    st.title("🔍 Investigation")

    search = st.text_input(
        "Search ID"
    )

    if st.button("Search"):

        if search:

            st.success(
                f"Searching for: {search}"
            )

        else:

            st.warning(
                "Please enter an ID."
            )


# -----------------------------
# SETTINGS
# -----------------------------

elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.checkbox(
        "Enable notifications",
        value=True
    )

    st.checkbox(
        "Enable automatic updates",
        value=True
    )

    st.selectbox(
        "Theme",
        ["Light", "Dark", "System"]
    )

    st.success(
        "Settings saved."
    )