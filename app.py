import streamlit as st
from pathlib import Path

# --- PAGE SETTINGS ---
st.set_page_config(
    page_title="Visualizing Student Performance: Patterns and Correlations",
    page_icon="🎓",
    layout="wide"
)

# --- STYLE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
html, body, [class*="css"] { font-family: 'Poppins', sans-serif; background-color: #fffaf6; color: #222; }

/* Header */
.header { text-align:center; padding:10px 0; }
.title { font-size:36px; color:#8b2b63; margin-bottom:6px; font-weight:700; }

/* Objective heading */
.objective { font-size:20px; color:#7a2a57; font-weight:700; margin:14px 0; }

/* Card & figure */
.card { background:#fff; border-radius:12px; padding:18px; box-shadow:0 6px 18px rgba(0,0,0,0.06); margin-bottom:18px; }
.figure-title { color:#7a2b57; font-weight:700; font-size:18px; margin-bottom:8px; }
.figure-text { color:#333; font-size:16px; line-height:1.9; text-align:justify; white-space: pre-wrap; margin-top:10px; }

/* Image */
.imgwrap { display:flex; justify-content:center; }
img { border-radius:10px; box-shadow: 0 6px 20px rgba(0,0,0,0.08); display:block; margin-left:auto; margin-right:auto; }

/* Footer */
.footer { text-align:center; color:#6b4a5a; padding-top:18px; font-size:13px; }

/* small note */
.small-note { font-size:12px; color:#6b4a5a; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="header">', unsafe_allow_html=True)
st.markdown('<div class="title">🎓 Visualizing Student Performance: Patterns and Correlations</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
page = st.sidebar.selectbox(
    "Navigate Pages",
    [
        "Objective 1: To analyze the distribution of academic and non-academic factors affecting students' performance.",
        "Objective 2: To explore the relationship between students' study patterns, attendance, and CGPA.",
        "Objective 3: To identify correlations among key factors influencing overall academic success."
    ],
)

# Helper to render a figure, text and download button (uses exact filenames you provided)
def render_block(fig_file, fig_title, full_text):
    path = Path(fig_file)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # render the figure title (plain text, styled by CSS)
    st.markdown(f'<div class="figure-title">{fig_title}</div>', unsafe_allow_html=True)
    if path.exists():
        st.image(str(path), use_column_width=True)
        # download button: read bytes
        with open(path, "rb") as f:
            st.download_button(
                label="Download this image",
                data=f,
                file_name=path.name,
                mime="image/png"
            )
    else:
        st.warning(f"Image not found: {fig_file}  — make sure this file exists in the same folder as app.py.")
    st.markdown(f'<div class="figure-text">{full_text}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ===========================
# PAGE 1 - Objective 1
# ===========================
if page.startswith("Objective 1"):
    st.markdown('<div class="objective">🎯 Objective 1: To analyze the distribution of academic and non-academic factors affecting students\' performance.</div>', unsafe_allow_html=True)

    # Figure 1
    render_block(
        "Obj1_F1.png",
        "1. Distribution of CGPA According to Gender",
        ("This visualization shows the distribution of CGPA of students according to gender. The findings demonstrate "
         "that male and female students have a similar academic range and, therefore, there are not significant gender "
         "performance differences. The median CGPA is a little higher among female students indicating more stability "
         "in academic performance whereas it is more varied among the male students. Generally, the visualization shows "
         "that gender does not play a big role in determining the academic performance of students. This observation highlights "
         "the fact that attendance and other behavioral factors like study habits are more significant in defining success. "
         "The equal balance of both genders serves to emphasize that there might be no difference in the level of academic opportunities "
         "and motivation among the students and this is in favor of inclusivity in the learning process.")
    )

    # Figure 2
    render_block(
        "Obj1_F2.png",
        "2. Daily Study Hours vs Current CGPA by Gender",
        ("This visualization examines the relationship between students' daily study hours and current CGPA, categorized by gender. "
         "It has a clear positive relationship with higher CGPA marks being recorded with students who study more hours. The performance "
         "patterns of both the male and female students are similar indicating that study patterns have a greater influence on academic performance "
         "than gender differences. This tendency is confirmed by the regression line, which states that regular studying enhances academic performance. "
         "This means that time management and good learning habits play a significant role in determining the success of the students. It may be beneficial "
         "to encourage students to devise a regular study period that will increase overall academic performance and decrease the differences in performance "
         "between people.")
    )

    # Figure 3
    render_block(
        "Obj1_F3.png",
        "3. Effect of Class Attendance on CGPA",
        ("The figure analyzes the effect of class attendance on CGPA of students in various age groups. It is always found that students who attend school "
         "regularly perform positively on their academic performances meaning that classroom attendance is a significant contributor towards learning performance. "
         "Younger students of the age group 18-20 have slightly different values of CGPA, which may be caused by more attention to school during early years. "
         "Conversely, older students are more varied, which may represent external obligations or time pressure. In summation, the graphic illustration underlines "
         "that attendance is not only more fruitful with regard to understanding and retention; it also has a direct positive influence on academic performance. "
         "Irrespective of age, active learners participate in classroom activities and thus are more likely to sustain an excellent CGPA performance and academic excellence.")
    )

# ===========================
# PAGE 2 - Objective 2
# ===========================
elif page.startswith("Objective 2"):
    st.markdown('<div class="objective">🎯 Objective 2: To explore the relationship between students\' study patterns, attendance, and CGPA.</div>', unsafe_allow_html=True)

    render_block(
        "Obj2_F1.png",
        "1. Daily Study Hours vs Current CGPA",
        ("The visualization examines the correlation between the number of hours the students study per day and the present CGPA. "
         "There is a positive correlation with students who have more time in studying having higher academic performance. These trends are present for both genders, indicating that good study habits are relevant across the population. "
         "The correlation line shows that regular study habits result in gradual academic improvement. This observation highlights the essence of time management and consistent study schedules in improving learning outcomes. Overall, greater study engagement is associated with better academic performance.")
    )

    render_block(
        "Obj2_F2.png",
        "2. Attendance vs CGPA",
        ("The figure examines how the level of attendance to classes impacts the CGPA of the students. The boxplot indicates that higher attendance is associated with better CGPA values and therefore indicates a strong correlation between class participation and academic success. Individuals who have poor attendance show more variability in performance, implying lack of consistent engagement in learning. Frequent attendance enables students to understand concepts well, keep track of coursework and perform better in assessments. This trend underscores attendance as a key academic behaviour that determines learning continuity and outcomes.")
    )

    render_block(
        "Obj2_F3.png",
        "3. Study Sessions per Day vs Current CGPA",
        ("The visualization studies the relationship between the number of study sessions per day and the academic performance of the students. The trend line shows a moderate positive correlation indicating that students who study more than once a day tend to have higher average CGPA. The pattern suggests that regular short study sessions are more effective than irregular long sessions. Gender does not significantly alter this pattern; disciplined study routines benefit all learners. The figure highlights the importance of distributed learning habits, where repeated engagement improves understanding and retention.")
    )

# ===========================
# PAGE 3 - Objective 3
# ===========================
elif page.startswith("Objective 3"):
    st.markdown('<div class="objective">🎯 Objective 3: To identify correlations among key factors influencing overall academic success.</div>', unsafe_allow_html=True)

    render_block(
        "Obj3_F1.png",
        "1. Correlation Between Academic and Behavioral Factors",
        ("In this correlation heatmap, it was possible to find the relationship between academic and behavioral variables, including study hours, social media time, previous SGPA, and current CGPA. There is a positive relationship between past SGPA and current CGPA, indicating students who previously performed well tend to sustain good performance. Study hours show a moderate positive correlation with CGPA, while social media use has a weak negative correlation, suggesting excessive use may slightly reduce academic outcomes. Family income and age appear to have minimal direct impact. Overall, academic habits and prior performance are stronger predictors of success than socioeconomic or demographic factors.")
    )

    render_block(
        "Obj3_F2.png",
        "2. Family Income vs Current CGPA",
        ("The current CGPA is plotted against monthly family income in this scatter plot. The trendline indicates a weak positive correlation, implying students from low- and high-income families show similar CGPA distributions. Financial status does not strongly determine academic performance; motivation, study habits, and self-discipline are more decisive. The presence of high performers across income groups reinforces that focused effort and consistent habits drive success regardless of economic background.")
    )

    render_block(
        "Obj3_F3.png",
        "3. Scholarship Status vs CGPA",
        ("This figure compares CGPA between students who receive scholarships and those who do not. Scholarship holders generally display higher and more consistent CGPA values, reflecting strong academic discipline. Non-scholarship students show a wider range of CGPA, but also include high performers who may become eligible for awards in the future. The visualization highlights how recognition programmes such as scholarships can reward and encourage continued effort and achievement.")
    )

# Footer / credit
st.markdown('<div class="footer">By Sharmini — Data source: Students Academic Performance Evaluation Dataset (Mendeley)</div>', unsafe_allow_html=True)
