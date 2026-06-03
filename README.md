Intelligent Resume Ranking System

An AI-powered Resume Screening and Candidate Ranking application that helps recruiters efficiently identify the most suitable candidates by comparing resumes with job descriptions using Natural Language Processing (NLP).

🚀 Features
📄 Upload multiple resumes (PDF format)
🎯 Match resumes against a job description
🤖 NLP-based resume analysis
📊 Calculate candidate match scores
🏆 Automatic candidate ranking
📈 Interactive hiring dashboard
🔍 Candidate filtering and search
📋 Hiring recommendations:
Selected (≥70%)
Review (50–69%)
Rejected (<50%)
📥 Export results to CSV
🛠️ Tech Stack
Python
Streamlit
Pandas
Scikit-learn
TF-IDF Vectorization
Cosine Similarity
PDF Processing (PyPDF2/pdfplumber)
📂 Project Structure
Intelligent-Resume-Ranking-System/
│
├── app.py
├── requirements.txt
├── resumes/
├── data/
├── utils/
├── assets/
└── README.md
⚙️ Installation
1. Clone the Repository
git clone https://github.com/your-username/intelligent-resume-ranking-system.git

cd intelligent-resume-ranking-system
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py

The application will open in your browser automatically.

📋 How It Works
Upload candidate resumes.
Enter or paste the job description.
The system extracts text from resumes.
TF-IDF vectorization converts text into numerical features.
Cosine Similarity calculates resume-job description relevance.
Match scores are generated.
Candidates are ranked automatically.
Hiring recommendations are displayed.
📊 Evaluation Criteria
Match Score	Recommendation
70% - 100%	Selected
50% - 69%	Review
Below 50%	Rejected
🎯 Use Cases
HR Recruitment
Campus Hiring
Internship Selection
Resume Shortlisting
Talent Acquisition
📸 Key Dashboard Components
Resume Ranking Table
Match Score Visualization
Hiring Summary Cards
Candidate Recommendation Categories
CSV Export Functionality
