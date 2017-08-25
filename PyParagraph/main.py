
import re
paragraphs=["paragraph_1.txt", "paragraph_2.txt"]
punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]

for paragraph in paragraphs:
    f = open(paragraph,"r") 
    paragraph_new=f.read()

    #Remove newline sign "\n" in some files
    paragraph_new=paragraph_new.replace("\n"," ")
    #Convert sentence ending punctuations '.\"' to ". " for easy subsequent analysis
    paragraph_new=paragraph_new.replace(".\"",". ")
    #Split paragraphs at sentence ending punctuations ".!? ".
    sentences=re.split("(?<=[.!?]) +", paragraph_new)
    sentence_count=len(sentences)
    
    word_count=0
    letter_count=0
    tokenized_paragraph =[]
    for sentence in sentences:
        for punc in punctuation:
            sentence=sentence.replace(punc, "")
        cleaned_sentence=sentence
        tokenized_sentence=cleaned_sentence.split(" ")
        tokenized_paragraph.append(tokenized_sentence)
        sentence_length=len(tokenized_sentence)
        word_count+=sentence_length
    
        sentence_letter_count=0
        for word in tokenized_sentence:
            word_letter_count=len(word)
            sentence_letter_count+=word_letter_count
        letter_count+=sentence_letter_count
    avg_sentence_length=word_count/sentence_count
    avg_letter_count=letter_count/word_count
    print("--------------------------------------")
    print("Paragraph Analysis (" + paragraph + ")")
    print("--------------------------------------")
    print("Approximate Word Count: " + str(word_count))
    print("Approximate Sentence Count: " + str(sentence_count))
    print("Average Letter Count: " + str(avg_letter_count))
    print("Approximate Sentence Length: " + str(avg_sentence_length))
    print("--------------------------------------")




