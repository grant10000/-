# Part of case-study #6: Text analysis
# Developers: Smorodina A., Nazarenko V.
#
from textblob import TextBlob
from googletrans import Translator
import re
import ru_local as ru
def detect_language(text):
    """
    Detect the language of the text based on the presence of Russian letters.
    :param text: Input string for language detection
    :return: String identifier ('russian' or 'english')
    """
    text_lower = text.lower()
    for char in text_lower:
        if char in ru.RUSSIAN_LETTERS:
            return 'russian'
    return 'english'
def translate_to_en(text):
    """
    Translate text from Russian to English.
    :param text: Russian language input string
    :return: English language equivalent translation
    """
    translator = Translator()
    translation = translator.translate(text, src='ru', dest='en')
    return translation.text
def count_sentences(text):
    """
    Count the number of sentences in the text.
    :param text: Input textual content for analysis
    :return: Integer representing quantity of sentences
    """
    sentences = re.split(r'[.!?]+(?:\s+|$)', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return max(1, len(sentences))
def count_words(text):
    """
    Count the number of words in the text.
    :param text: Input string for lexical analysis
    :return: Integer count of words
    """
    return len(text.split())
def count_syllables(text):
    """
    Count the number of syllables in the text.
    :param text: Input string for phonological examination
    :return: Total count of syllabic nuclei
    """
    vowels = 'aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in text if char in vowels)
def main(text):
    """
    Execute comprehensive textual analysis.
    :param text: Primary textual input for multidimensional analysis
    :return: Console output of analytical results
    """
    language = detect_language(text)
    
    if language == 'russian':
        translated_text = translate_to_en(text)
        blob = TextBlob(translated_text)
    else:
        blob = TextBlob(text)
    
    sentences = count_sentences(text)
    words = count_words(text)
    syllables = count_syllables(text)
    
    average_sentence_length = words / sentences
    average_word_length = syllables / words
    flesch_index_en = 206.835 - (1.015 * average_sentence_length) - (84.6 * average_word_length)
    flesch_index_ru = 206.835 - (1.52 * average_sentence_length) - (65.14 * average_word_length)
    if language == 'russian':
        flesch_index = flesch_index_ru
    else:
        flesch_index = flesch_index_en
    
    if flesch_index >= 80:
        interpretation = ru.VERY_EASY
    elif flesch_index >= 50:
        interpretation = ru.EASY
    elif flesch_index >= 25:
        interpretation = ru.MEDIUM
    else:
        interpretation = ru.HARD
    sentiment = blob.sentiment.polarity
    if sentiment <= -0.33:
        tonality_of_the_text = ru.NEGATIVE
    elif sentiment >= 0.66:
        tonality_of_the_text = ru.POSITIVE
    else:
        tonality_of_the_text = ru.NEUTRAL
    objectivity = (1 - blob.sentiment.subjectivity) * 100
    print(ru.SENTENCES_COUNT, sentences)
    print(ru.WORDS_COUNT, words)
    print(ru.SYLLABLES_COUNT, syllables)
    print(ru.AVG_SENTENCE_LENGTH, average_sentence_length)
    print(ru.AVG_WORD_LENGTH, average_word_length)
    print(ru.FLESCH_INDEX, flesch_index)
    print(interpretation)
    print(ru.TEXT_TONALITY, tonality_of_the_text)
    print(ru.OBJECTIVITY, str(objectivity) + '%')
    
user_text = input(ru.INPUT_PROMPT)
main(user_text)
