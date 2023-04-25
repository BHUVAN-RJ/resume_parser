import text_extract
import os
import nltk
from googletrans import Translator
from preprocessing import preprocess

translator = Translator()

folder = '/Users/rjb/PycharmProjects/mllab/resume_parser/resume'
preprocess(folder)


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
SKILLS_DB = [

    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English',
]


def extract_skills(input_text):
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
        if token.lower() in BLUE_COLLARED_SKILLS:
            found_skills.append(token)

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in BLUE_COLLARED_SKILLS:
            found_skills.append(ngram)

    return found_skills

folder_path = os.listdir(folder)


for item in folder_path:
    current_doc = f"{folder}/{item}"
    doc_extension = current_doc.rsplit(".", 2)[1]

    resume_to_text = ''

    if doc_extension == 'pdf':
        resume_to_text = text_extract.extract_text_from_pdf(current_doc)
        if len(resume_to_text) < 10:
            print("Invalid Resume Format!")
            continue
    elif doc_extension == 'docx':
        resume_to_text = text_extract.extract_text_from_docx(current_doc)
        if len(resume_to_text) < 10:
            print("Invalid Resume Format!")
            continue
    # resume_lang = translator.detect(resume_to_text)
    # if resume_lang.lang != 'en':
    #     resume_to_text = translator.translate(resume_to_text)
    #     print(resume_to_text)
    # skills = extract_skills(resume_to_text)
    # print(skills)





