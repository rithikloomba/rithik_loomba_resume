import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Rithik Loomba- Resume",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PROFESSIONAL AESTHETICS ---
st.markdown("""
<style>
    .main-title { font-size: 2.6rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0.2rem; }
    .subtitle { font-size: 1.3rem; color: #4B5563; margin-bottom: 1.5rem; }
    .section-header { font-size: 1.8rem; font-weight: 600; color: #1E3A8A; border-bottom: 2px solid #DBEAFE; padding-bottom: 0.3rem; margin-top: 1.5rem; margin-bottom: 1rem; }
    .card { background-color: #F8FAFC; padding: 1.2rem; border-radius: 8px; border-left: 5px solid #3B82F6; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .metric-box { background-color: #EFF6FF; padding: 1rem; border-radius: 8px; text-align: center; border: 1px solid #BFDBFE; }
    .metric-val { font-size: 1.8rem; font-weight: 700; color: #1E40AF; }
    .metric-lbl { font-size: 0.9rem; color: #1E3A8A; font-weight: 500; }
    .badge { background-color: #E2E8F0; color: #334155; padding: 0.25rem 0.6rem; border-radius: 50px; font-size: 0.85rem; display: inline-block; margin: 0.2rem; font-weight: 500;}
    .skill-category { font-weight: 600; color: #1E3A8A; margin-top: 0.5rem; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CONTACT & NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color: #1E3A8A; margin-bottom:0;'>Rithik Loomba</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-style: italic;'>Social Sector Professional</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Contact Info
    st.markdown("📧 [rithikloomba@gmail.com](mailto:rithikloomba@gmail.com)")
    st.markdown("📱 9899507502")
    st.markdown("🌐 [linkedin.com/in/rithikloomba](https://linkedin.com/in/rithikloomba)")
    st.markdown("📍 New Delhi, India")
    st.markdown("---")
    
    # Navigation Radio
    page = st.radio(
        "Navigate Dashboard",
        ["Overview & Metrics", "Professional Experience", "Skills & Core Expertise", "Certifications & Education"]
    )
    
    st.markdown("---")
    st.markdown("#### Languages")
    st.markdown("<span class='badge'>English</span><span class='badge'>Hindi</span><span class='badge'>Punjabi</span>", unsafe_allow_html=True)

# --- MAIN CONTENT DYNAMICS ---

if page == "Overview & Metrics":
    st.markdown("<div class='main-title'>Resume</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Monitoring & Evaluation | Digital Health | Data Analytics | Public Health | Program Management</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>UNDP | Ministry of Health & Family Welfare</div>", unsafe_allow_html=True)
    
    # Professional Summary
    st.markdown("<div class='section-header'>Executive Summary</div>", unsafe_allow_html=True)
    st.info(
        "Monitoring & Evaluation professional with 10+ years of experience designing and operating national-level M&E frameworks, "
        "results-based reporting, and data systems across multi-stakeholder public health programmes in India. Skilled in translating "
        "field-level data into decision-ready analysis for government, UN, and donor audiences."
    )
    
    # Impact Metrics Section
    st.markdown("<div class='section-header'>Key Portfolio Metrics</div>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown("<div class='metric-box'><div class='metric-val'>10+ Years</div><div class='metric-lbl'>Experience</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown("<div class='metric-box'><div class='metric-val'>5 Platforms</div><div class='metric-lbl'>National Systems managed</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown("<div class='metric-box'><div class='metric-val'>2 National</div><div class='metric-lbl'>Guidelines Published</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown("<div class='metric-box'><div class='metric-val'>12+ Global</div><div class='metric-lbl'>Professional Certs</div></div>", unsafe_allow_html=True)

    # Core Competencies Chart / Breakdown
    st.markdown("<div class='section-header'>National Platforms Overview</div>", unsafe_allow_html=True)
    platform_data = pd.DataFrame({
        'Platform/Program': ['U-WIN', 'TB-WIN', 'eVIN', 'CoWIN', 'Anemia Mukt Bharat', 'National Deworming Day', 'MAA', 'IDCF'],
        'Scope': ['National Routine Immunization', 'National TB Tracking', 'Vaccine Logistics Network', 'COVID-19 Vaccine Rollout', 'Cross-sectoral Nutrition', 'Mass Drug Administration', 'Community Awareness', 'Community Outreach'],
        'Key Level': ['National / Project Review', 'National / State Feedback', 'National Data Analytics', 'National / Emergency Response', 'National & 4 Focus States', 'National & 4 Focus States', 'National', 'National / State Feedback']
    })
    st.table(platform_data)

elif page == "Professional Experience":
    st.markdown("<div class='section-header'>Professional Experience</div>", unsafe_allow_html=True)
    
    # Job 1
    st.markdown("""
    <div class='card'>
        <h4 style='margin:0; color:#1E3A8A;'>U-WIN Coordinator – Project Review / M&E Consultant</h4>
        <p style='margin:0; font-weight:500; color:#4B5563;'>United Nations Development Programme | Jul 2024 – Present & May 2021 – Jun 2024</p>
        <ul style='margin-top:0.5rem; color:#334155;'>
            <li>Design and operate M&E frameworks for four national health data systems (eVIN, TB-WIN, CoWIN, U-WIN).</li>
            <li>Develop and implement results-based data collection systems and analytics strategies to strengthen program monitoring.</li>
            <li>Identify trends across datasets, translating findings into actionable field performance adjustments.</li>
            <li>Advise health officials and policymakers, bridging technical data analytics with high-level programmatic decision-making.</li>
            <li>Facilitate monthly results-review meetings with UNDP Programme Officers and VCCMs to drive institutional knowledge sharing.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Job 2
    st.markdown("""
    <div class='card'>
        <h4 style='margin:0; color:#1E3A8A;'>Program Associate</h4>
        <p style='margin:0; font-weight:500; color:#4B5563;'>Evidence Action | Jan 2020 – Mar 2021</p>
        <ul style='margin-top:0.5rem; color:#334155;'>
            <li>Supported planning, implementation, and MEL reporting for Anemia Mukt Bharat and National Deworming Day across 4 focus states (Rajasthan, Haryana, Madhya Pradesh, Jharkhand).</li>
            <li>Managed program and financial data sets, trend analytics, and supported the AMB Results Dashboard for the Ministry of Health & Family Welfare (MoHFW).</li>
            <li>Assisted states in developing Program Implementation Plans (PIPs), operationalizing national frameworks down to state levels.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Job 3
    st.markdown("""
    <div class='card'>
        <h4 style='margin:0; color:#1E3A8A;'>Research Analyst / Project Associate</h4>
        <p style='margin:0; font-weight:500; color:#4B5563;'>Ministry of Health & Family Welfare, Government of India | Sep 2013 – Jun 2019</p>
        <ul style='margin-top:0.5rem; color:#334155;'>
            <li>Managed a cross-sectoral portfolio spanning six national health and nutrition programmes (AMB, NDD, IYCF, MAA, IDCF, NRCs).</li>
            <li>Prepared data analysis frameworks, annual reports, and budget documentation (PIP and RoP).</li>
            <li>Contributed to formal national programme guidelines deployed globally to state-level health implementers.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "Skills & Core Expertise":
    st.markdown("<div class='section-header'>Technical Proficiency Matrix</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<p class='skill-category'>📊 Monitoring, Evaluation & Learning (MEL)</p>", unsafe_allow_html=True)
        st.markdown("<span class='badge'>M&E Framework Design</span><span class='badge'>Results-Based Management</span><span class='badge'>Results Monitoring</span><span class='badge'>Capacity Building</span>", unsafe_allow_html=True)
        
        st.markdown("<p class='skill-category'>💾 Data Management & Field Tools</p>", unsafe_allow_html=True)
        st.markdown("<span class='badge'>STATA</span><span class='badge'>KoBo Toolbox</span><span class='badge'>Google Forms</span><span class='badge'>Power BI</span><span class='badge'>Google Dashboard</span>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<p class='skill-category'>🐍 Data Science & Visualization</p>", unsafe_allow_html=True)
        st.markdown("<span class='badge'>Python</span><span class='badge'>R Language</span><span class='badge'>SQL</span><span class='badge'>Tableau</span><span class='badge'>Machine Learning</span><span class='badge'>Spatial Epidemiology</span>", unsafe_allow_html=True)
        
        st.markdown("<p class='skill-category'>📝 Knowledge & Communication</p>", unsafe_allow_html=True)
        st.markdown("<span class='badge'>Annual Status Reports</span><span class='badge'>Case Studies</span><span class='badge'>Multi-Stakeholder Coordination</span><span class='badge'>Policy Brief Notes</span>", unsafe_allow_html=True)

    # Industry Skill Focus Breakdown
    st.markdown("<div class='section-header'>Skill Domain Focus Distribution</div>", unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        'Domain Weight': [35, 25, 20, 20]},
        index=['MEL Strategy & Frameworks', 'Data Science & Languages (R/Python/SQL)', 'Dashboarding & BI tools', 'Cross-sectoral Knowledge Management']
    )
    st.bar_chart(chart_data)

elif page == "Certifications & Education":
    st.markdown("<div class='section-header'>Publications</div>", unsafe_allow_html=True)
    st.markdown("""
    * 📜 **National Guidelines on Anemia Mukt Bharat (i-NIPI) for Program Managers** – Ministry of Health and Family Welfare (Apr 2018)
    * 📜 **National Guidelines on Lactation Management Centres in Public Health Facilities** – Ministry of Health and Family Welfare (Jul 2017)
    """)
    
    st.markdown("<div class='section-header'>Education</div>", unsafe_allow_html=True)
    st.markdown("""
    * **MBA (Healthcare Management)** — Suresh Gyan Vihar University, Jaipur, India (2023)
    * **Master of Arts (English)** — Indira Gandhi National Open University, Delhi, India (2019)
    * **Bachelor of Arts** — Indira Gandhi National Open University, Delhi, India (2015)
    """)

    st.markdown("<div class='section-header'>Professional Certifications</div>", unsafe_allow_html=True)
    certs = [
        "Data Science with Python — IIT Roorkee",
        "Data Analysis and Spatial Epidemiology using R — Yenepoya University",
        "Analyzing and Visualizing Data with Microsoft Power BI — Leonardo Karpinski",
        "Data Use for Program Managers — USAID",
        "M&E Fundamentals — USAID",
        "STATA – Data Management Tools and Advanced Statistics — Lady Irwin College (UNICEF)",
        "System Thinking in Public Health — Johns Hopkins University",
        "Epidemiology: The Basic Science of Public Health — UNC at Chapel Hill",
        "COVID-19 Operational Planning & Response — World Health Organization"
    ]
    for cert in certs:
        st.markdown(f"✓ {cert}")
