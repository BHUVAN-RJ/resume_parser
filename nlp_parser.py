import text_extract
import os
import nltk
from preprocessing import preprocess
import number_extractor


# folder = '/Users/rjb/PycharmProjects/mllab/resume_parser/resume'
# preprocess(folder)


nltk.download('stopwords')
BLUE_COLLARED_SKILLS = [
    'service engineer',
    'maintenance',
    'manufacturing',
    'security',
    'qa',
    'assembly line',
    'rigger',
    'watchman',
    'driver',
    'contractor',
    'operator',
    'receptionist',
    'delivery',
    'service technician',
    'junior engineer',
    'generator assembly',
    'sub component assembly wiring',
    'drawing study',
    'dispatch preparation kitting arrangement documentary',
    'material arrangement solution finding',
    'technician',
    'cnc machine operator',
    'quality inspector',
    'supervisor',
    ''
]


def extract_skills(input_text, skills):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    # we create a setset() to keep the results in.
    found_skills = []

    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in skills:
            found_skills.append(token)

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in skills:
            found_skills.append(ngram)

    return found_skills


def extract_text_and_parse(skills, file):
    # folder_path = os.listdir(folder)
    current_doc = file
    doc_extension = current_doc.rsplit(".", 2)[1]

    # for item in folder_path:
    #     print(1)
    #     current_doc = f"{folder}/{item}"
    #     doc_extension = current_doc.rsplit(".", 2)[1]
    #
    resume_to_text = ''

    if doc_extension == 'pdf':
        resume_to_text = text_extract.extract_text_from_pdf(current_doc)
        if len(resume_to_text) < 10:
            print(f"Invalid Resume Format!:{current_doc}")
    elif doc_extension == 'docx':
        resume_to_text = text_extract.extract_text_from_docx(current_doc)
        if len(resume_to_text) < 10:
            print(f"Invalid Resume Format!:{current_doc}")
    phone_number = number_extractor.extract_phone_number(resume_to_text)
    extracted_skills = extract_skills(resume_to_text, skills)
    return phone_number,extracted_skills





