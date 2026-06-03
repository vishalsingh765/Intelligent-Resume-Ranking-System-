from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


def get_similarity_scores(job_desc, resumes):

    documents = [job_desc] + resumes

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(
        matrix[0:1],
        matrix[1:]
    )[0]

    return scores