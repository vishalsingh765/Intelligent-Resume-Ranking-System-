import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.pdf_reader import extract_text_from_pdf
from utils.preprocess import clean_text
from utils.similarity import get_similarity_scores
from utils.skills import extract_skills

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ResumeIQ ATS",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

div[data-testid="metric-container"] {
    background-color: #1C1F26;
    border: 1px solid #00C896;
    padding: 15px;
    border-radius: 15px;
}

.stButton > button {
    background-color: #00C896;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.title("🚀 ResumeIQ")
st.subheader(
    "AI-Powered ATS Resume Screening & Candidate Ranking Platform"
)

st.markdown("---")

# ==========================================
# INPUTS
# ==========================================

col1, col2 = st.columns(2)

with col1:

    job_description = st.text_area(
        "📋 Paste Job Description",
        height=250
    )

with col2:

    resume_files = st.file_uploader(
        "📄 Upload Resume PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

# ==========================================
# ANALYZE BUTTON
# ==========================================

if st.button("🚀 Analyze Resumes"):

    if not job_description:

        st.warning(
            "Please enter Job Description."
        )

    elif not resume_files:

        st.warning(
            "Please upload resumes."
        )

    else:

        # ==========================================
        # JOB DESCRIPTION
        # ==========================================

        cleaned_jd = clean_text(
            job_description
        )

        jd_skills = extract_skills(
            cleaned_jd
        )

        # ==========================================
        # RESUME PROCESSING
        # ==========================================

        resume_texts = []

        candidate_names = []

        resume_data = []

        for file in resume_files:

            text = extract_text_from_pdf(
                file
            )

            cleaned_resume = clean_text(
                text
            )

            candidate_name = (
                file.name.replace(
                    ".pdf",
                    ""
                )
            )

            resume_texts.append(
                cleaned_resume
            )

            candidate_names.append(
                candidate_name
            )

            resume_data.append(
                {
                    "name": candidate_name,
                    "text": cleaned_resume
                }
            )

        # ==========================================
        # SIMILARITY
        # ==========================================

        scores = get_similarity_scores(
            cleaned_jd,
            resume_texts
        )

        # ==========================================
        # DATAFRAME
        # ==========================================

        results = []

        for name, score in zip(
            candidate_names,
            scores
        ):

            results.append(
                {
                    "Candidate": name,
                    "Match Score (%)":
                    round(score * 100, 2)
                }
            )

        df = pd.DataFrame(
            results
        )

        df = df.sort_values(
            by="Match Score (%)",
            ascending=False
        )

        df["Rank"] = range(
            1,
            len(df) + 1
        )

        # ==========================================
        # JOB DESCRIPTION OVERVIEW
        # ==========================================

        st.markdown("---")

        st.header(
            "📋 Job Description Overview"
        )

        if jd_skills:

            st.success(
                "Required Skills: "
                + ", ".join(jd_skills)
            )

        # ==========================================
        # DASHBOARD
        # ==========================================

        st.markdown("---")

        st.header(
            "📊 Recruiter Dashboard"
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Candidates",
            len(df)
        )

        col2.metric(
            "Top Score",
            f"{df['Match Score (%)'].max()}%"
        )

        col3.metric(
            "Average Score",
            f"{round(df['Match Score (%)'].mean(),2)}%"
        )

        qualified = len(
            df[
                df["Match Score (%)"] >= 70
            ]
        )

        col4.metric(
            "Qualified",
            qualified
        )

        # ==========================================
        # TOP CANDIDATE
        # ==========================================

        st.markdown("---")

        best = df.iloc[0]

        st.success(
            f"""
🏆 TOP CANDIDATE

Candidate: {best['Candidate']}

ATS Match Score:
{best['Match Score (%)']}%
"""
        )

        # ==========================================
        # RANKING TABLE
        # ==========================================

        st.markdown("---")

        st.header(
            "🏆 Candidate Rankings"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        # ==========================================
        # BAR CHART
        # ==========================================

        st.markdown("---")

        st.header(
            "📈 Candidate Comparison"
        )

        fig, ax = plt.subplots()

        ax.bar(
            df["Candidate"],
            df["Match Score (%)"]
        )

        ax.set_xlabel(
            "Candidates"
        )

        ax.set_ylabel(
            "Match Score (%)"
        )

        st.pyplot(fig)

        # ==========================================
        # CANDIDATE ANALYSIS
        # ==========================================

        st.markdown("---")

        st.header(
            "👨‍💼 Candidate Analysis Dashboard"
        )

        for resume in resume_data:

            candidate_name = (
                resume["name"]
            )

            candidate_row = df[
                df["Candidate"]
                ==
                candidate_name
            ]

            score = float(
                candidate_row[
                    "Match Score (%)"
                ].values[0]
            )

            resume_skills = (
                extract_skills(
                    resume["text"]
                )
            )

            matched = list(
                set(jd_skills)
                &
                set(resume_skills)
            )

            missing = list(
                set(jd_skills)
                -
                set(resume_skills)
            )

            st.markdown("---")

            st.subheader(
                f"👤 {candidate_name}"
            )

            st.write(
                f"🎯 ATS Score: {score}%"
            )

            st.progress(
                score / 100
            )

            col1, col2 = st.columns(2)

            with col1:

                st.success(
                    "Matched Skills"
                )

                for skill in matched:

                    st.write(
                        f"✅ {skill}"
                    )

            with col2:

                st.error(
                    "Missing Skills"
                )

                for skill in missing:

                    st.write(
                        f"❌ {skill}"
                    )

            if score >= 80:

                st.success(
                    "Excellent candidate."
                )

            elif score >= 60:

                st.warning(
                    "Good candidate."
                )

            else:

                st.error(
                    "Needs improvement."
                )

            with st.expander(
                f"📄 Resume Preview - {candidate_name}"
            ):

                st.text(
                    resume["text"][:1500]
                )

        # ==========================================
        # SCORE DISTRIBUTION
        # ==========================================

        st.markdown("---")

        st.header(
            "📊 Score Distribution"
        )

        fig2, ax2 = plt.subplots()

        ax2.hist(
            df["Match Score (%)"],
            bins=5
        )

        ax2.set_xlabel(
            "Match Score"
        )

        ax2.set_ylabel(
            "Candidates"
        )

        st.pyplot(fig2)

        # ==========================================
        # HIRING SUMMARY
        # ==========================================

        st.markdown("---")

        st.header(
            "📌 Hiring Summary"
        )

        selected = len(
            df[
                df["Match Score (%)"] >= 70
            ]
        )

        review = len(
            df[
                (df["Match Score (%)"] >= 50)
                &
                (df["Match Score (%)"] < 70)
            ]
        )

        rejected = len(
            df[
                df["Match Score (%)"] < 50
            ]
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.success(
                f"Selected\n\n{selected}"
            )

        with col2:
            st.warning(
                f"Review\n\n{review}"
            )

        with col3:
            st.error(
                f"Rejected\n\n{rejected}"
            )

        # ==========================================
        # DOWNLOAD CSV
        # ==========================================

        st.markdown("---")

        csv = df.to_csv(
            index=False
        )

        st.download_button(
            "📥 Download CSV",
            csv,
            "resume_ranking.csv",
            "text/csv"
        )

        # ==========================================
        # FOOTER
        # ==========================================

        st.markdown("---")

        st.caption(
            "ResumeIQ ATS Dashboard | Built with Python, NLP & Streamlit"
        )