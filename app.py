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
.header { text-align:center; padding:8px 0; }
.title { font-size:28px; color:#8b2b63; margin-bottom:4px; }
.subtitle { font-size:13px; color:#6e4a57; margin-top:2px; margin-bottom:16px; }
.card { background:#fff; border-radius:12px; padding:14px; box-shadow:0 6px 18px rgba(0,0,0,0.06); margin-bottom:18px; }
.figure-title { color:#7a2a57; font-weight:600; margin-bottom:6px; }
.figure-text { color:#333; font-size:14px; line-height:1.6; white-space: pre-wrap; }
.imgwrap { display:flex; justify-content:center; }
.small-note { font-size:12px; color:#6b4a5a; }
.footer { text-align:center; color:#6b4a5a; padding-top:18px; font-size:13px; }
.download-row { display:flex; gap:8px; align-items:center; justify-content:center; margin-top:8px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="header">', unsafe_allow_html=True)
st.markdown('<div class="title">🎓 Visualizing Student Performance: Patterns and Correlations</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">An interactive presentation of academic and behavioural factors that influence student CGPA.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
page = st.sidebar.selectbox(
    "Navigate Pages",
    [
        "Objective 1: To analyze the distribution of academic and non-academic factors affecting students’ performance.",
        "Objective 2: To explore the relationship between students’ study patterns, attendance, and CGPA.",
        "Objective 3: To identify correlations among key factors influencing overall academic success."
    ],
)

# Helper to render a figure, text and download button (uses exact filenames you provided)
def render_block(fig_file, fig_title, full_text):
    path = Path(fig_file)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="figure-title">#### {fig_title}</div>', unsafe_allow_html=True)
    if path.exists():
        st.image(str(path), use_column_width=True)
        # download button: read bytes
        with open(path, "rb") as f:
            btn = st.download_button(
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
    st.markdown("🎯 Objective 1: To analyze the distribution of academic and non-academic factors affecting students’ performance.")
    # Figure 1
    render_block(
        "Obj1_F1.png",
        "1. Distribution of CGPA According to Gender",
        ("This visualization shows the distribution of CGPA of student’s according to gender. The findings demonstrate "
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
        ("This visualization examines the relationship between students’ daily study hours and current CGPA, categorized by gender. "
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
         "Younger students of the age group 18–20 have slightly different values of CGPA, which may be caused by more attention to school during childhood. "
         "Conversely, older students are more varied, which may represent external obligations or time pressure. In summation, the graphic illustration underlines "
         "that the attendance is not only more fruitful with regard to the understanding and retention; it also has a direct positive influence on the academic performance. "
         "Irrespective of the age, active learners participate in classroom activities and thus are more likely to sustain an excellent CGPA performance and academic excellence.")
    )

# ===========================
# PAGE 2 - Objective 2
# ===========================
elif page.startswith("Objective 2"):
    st.markdown("🎯 Objective 2: To explore the relationship between students’ study patterns, attendance, and CGPA.")
    render_block(
        "Obj2_F1.png",
        "1. Daily Study Hours vs Current CGPA",
        ("The visualization examines the correlation between the number of hours the students study per day and the present CGPA. "
         "There is a positive correlation with students who have more time in studying having higher academic performance. These trends are not just in the male students where both genders follow a similar pattern indicating that good study habits are relevant in both genders. "
         "The correlation line shows that regular study habits result in a slow academic growth. This observation highlights the essence of time management and constant schedules of studying in improving the level of learning. Altogether, the number is in favor of the idea that the greater the study participation, the better academic performance of the students.")
    )

    render_block(
        "Obj2_F2.png",
        "2. Attendance vs CGPA",
        ("The figure examines how the level of attendance to classes impacts the CGPA of the students. The boxplot indicates the percentage of attendance of students with CGPA values also takes better values and therefore indicates that there is a very strong correlation between class participation and academic success. Individuals who have poor attendance show more variability of performance implying lack of consistent engagement in learning. Frequent attendance can enable the student to understand concepts well, keep track of course work and excel in exams. This trend underscores attendance as a key academic behavior, which determines the learning outcome and continuity. In short, attending classes actively can be discussed as a critical contributor to the increase in academic performance.")
    )

    render_block(
        "Obj2_F3.png",
        "3. Study Sessions per Day vs Current CGPA",
        ("The visualization studies the relationship between the number of study sessions per day and the academic performance of the students. The trend line shows that there is a moderate positive correlation which shows that students studying more than once a day have higher average CGPA. The trend indicates that regular short study sessions are better than unregular long study sessions. Gender also does not seem to play a significant role in this pattern, that is, teaching habits have the same benefits to all students. The figure highlights the importance of distributed learning habits, in which the recurrence of engagement with learning improves the understanding and retention. This observation is consistent with academic studies that indicate that regular study sessions enhance concentration, decrease exhaustion and determine excellent scholarly outcomes.")
    )

# ===========================
# PAGE 3 - Objective 3
# ===========================
elif page.startswith("Objective 3"):
    st.markdown("🎯 Objective 3: To identify correlations among key factors influencing overall academic success.")
    render_block(
        "Obj3_F1.png",
        "1. Correlation Between Academic and Behavioral Factors",
        ("In this correlation heatmap, it was possible to find the relationship between academic and behavioral variables, including study hours, social media time, previous SGPA, and current CGPA. There is a positive relationship between past SGPA and current CGPA, which is strong and positive in nature, meaning that students who used to achieve good performance, are able to sustain good performance. The hours studying are positively correlated with CGPA with a moderate correlation, with social media having a weak negative correlation, meaning that excessive use of social media can have a slight negative impact on academic performance. There is a minimal impact on family income and age. In general, the heatmap depicts that the academic habits and previous performance are more efficient predictors of success compared to socioeconomic and demographic.")
    )

    render_block(
        "Obj3_F2.png",
        "2. Family Income vs Current CGPA",
        ("The current CGPA is plotted against monthly family income in this scatter plot. The trendline indicates a low positive correlation, which implies that the students of the low- and high-income families are not different. Monetary position does not seem to have a significant impact on academic performance, which means that the motivation, study habits, and self-discipline are more decisive than income level. The existence of top performers in all the income distributions confirm the perception that learning behavior and hard work make people successful. In general, the visualization makes it clear that education is equal regardless of financial status academic greatness can be attained with the help of focused commitment.")
    )

    render_block(
        "Obj3_F3.png",
        "3. Scholarship Status vs CGPA",
        ("This figure compares CGPA between students who receive scholarships and those who do not. The values of CGPA and the variation of performance in scholarship holders are usually less and smaller in value, as there is a high degree of academic discipline and steady performance. The non-scholarship students are distributed more widely in their score line with some having high performance which can later make them eligible to receive awards. The findings explain how recognition schemes such as scholarships are not only rewarding but also encouragement of more efforts. The trend supports a vicious cycle between performance and achievement and academic rewards, namely students who succeed are more likely to continue succeeding because of more opportunities and motivation.")
    )

# Footer / credit
st.markdown('<div class="footer">By Sharmini  — Data source: Students Academic Performance Evaluation Dataset (Mendeley)</div>', unsafe_allow_html=True)
