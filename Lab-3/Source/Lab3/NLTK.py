import nltk
nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
from nltk import ngrams

#read the sample document
Doc = open('sample', 'r', encoding="utf-8")
txt = Doc.read();
lemma = nltk.WordNetLemmatizer()
wrds = word_tokenize(txt)
sents=sent_tokenize(txt)

#lemmatization
print("\n After Lemmatization the result is")
le = []
for word in wrds:
  L=lemma.lemmatize(word, pos='v')
  le.append(L)
print(le)

#BI-gram
print("\n Required Bigram are : \n")
wrds = word_tokenize(txt)
bi=[]
#give the esult with 2 words for the text
X = ngrams(wrds, 2)
for a in X:
    bi.append(a)
print(bi)

#frequent words finding
print("\n Required Freq in a Bigram are : \n")
freqD = nltk.FreqDist(bi)
rep_words = freqD.most_common()
#extracting top 5 words
top5_rep = freqD.most_common(5)
print(rep_words)
print("\n Required Top 5 Freq in a Bigram are : \n")
print(top5_rep)

#extracting the sentence with top 5 bigrams.
sentc_1 = sent_tokenize(txt)
rept_sentc1 = []
for senti1 in sentc_1:
    for word, wrds in bi:
        for ((p,q), l) in top5_rep:
            if (word, wrds == p,q):
                rept_sentc1.append(senti1)  # concatenation the sentenses.
print ("\n Sentences with top 5 Bigrams after concatenation are: ")
print(max(rept_sentc1, key=len))



