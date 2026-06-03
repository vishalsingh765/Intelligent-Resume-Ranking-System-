SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pandas",
    "numpy",
    "excel",
    "power bi",
    "tableau",
    "java",
    "spring boot",
    "c++",
    "aws",
    "docker"
]


def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill in text:

            found_skills.append(skill)

    return found_skills