from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
# Create your views here.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob 
import re
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import wordcounteSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import wordcounterModel
import pickle
import json
from django.views import View
import re
import os
import sys
import json
import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
#from textblob import TextBlob
import en_core_web_sm
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
# from scipy.sparse.linalg import lsqr as sparse_lsqr
nlp = en_core_web_sm.load()

#from app.views import temp_view 
@api_view(['GET'])
def api_index_view(request):
    return HttpResponse("Works")


# def ratereview(request,review):

#     a1 = SentimentIntensityAnalyzer()
#     vs=a1.polarity_scores(review)

#     if vs['neu']==1:
#         a2=TextBlob(review)
#         if a2.sentiment.polarity==0:
#             rating=1
#             return HttpResponse(str(rating))
#     if vs['compound'] < 0 and vs['neg']>0.3 and vs['pos']==0:
#         rating = 1
#         return HttpResponse(str(rating))
#     if vs['compound'] > 0 and vs['pos']>0.3 and vs['neg']==0:
#         rating = 5
#         return HttpResponse(str(rating))
#     if vs['neg']>vs['pos'] and vs['neg']>0.5 and vs['pos']!=0 :
#         rating = 2
#         return HttpResponse(str(rating))
#     if vs['neg']==vs['pos'] :
#         rating=2.5
#         return HttpResponse(str(rating))
#     if vs['neg']<vs['pos'] and vs['pos']>0.5 and vs['neg']!=0 :
#         rating = 4    
#         return HttpResponse(str(rating))
#     else:
#         rating = 3
#         return HttpResponse(str(rating))
# cnt1=0
# sentence1=""



# def _get_wordcounts(x):
#         length = len(str(x).split())
#         return length

# def _get_charcounts(x):
#         s = x.split()
#         x = ''.join(s)
#         return len(x)
# def _get_avg_wordlength(x):
#         count = _get_charcounts(x)/_get_wordcounts(x)
#         return count

# def _get_stopwords_counts(x):
#         l = len([t for t in x.split() if t in stopwords])
#         return l

# def _get_hashtag_counts(x):
#         l = len([t for t in x.split() if t.startswith('#')])
#         return l

# def _get_mentions_counts(x):
#         l = len([t for t in x.split() if t.startswith('@')])
#         return l
# def _get_digit_counts(x):
#         digits = re.findall(r'[0-9,.]+', x)
#         return len(digits)

# def _get_uppercase_counts(x):
#         return len([t for t in x.split() if t.isupper()])

# def _cont_exp(x):
#         abb = json.load(open("app/abbr.json"))
    
#         if type(x) is str:
#             for key in abb:
#                 value = abb[key]
#                 x = x.replace(key, value)
#             return x
#         else:
#             return x


# def _get_emails(x):
#         emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', x)
#         counts = len(emails)

#         return counts, emails


# def _remove_emails(x):
#         return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

# def _get_urls(x):
#         urls = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)
#         counts = len(urls)

#         return counts, urls

# def _remove_urls(x):
#         return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

# def _remove_rt(x):
#         return re.sub(r'\brt\b', '', x).strip()

# def _remove_special_chars(x):
#         x = re.sub(r'[^\w ]+', "", x)
#         x = ' '.join(x.split())
#         return x

# def _remove_html_tags(x):
#         return BeautifulSoup(x, 'lxml').get_text().strip()

# def _remove_accented_chars(x):
#         x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
#         return x

# def _remove_stopwords(x):
#         return ' '.join([t for t in x.split() if t not in stopwords])	

# def _make_base(x):
#         x = str(x)
#         x_list = []
#         doc = nlp(x)
        
#         for token in doc:
#             lemma = token.lemma_
#             if lemma == '-PRON-' or lemma == 'be':
#                 lemma = token.text

#             x_list.append(lemma)
#         return ' '.join(x_list)

# def _get_value_counts(df, col):
#         text = ' '.join(df[col])
#         text = text.split()
#         freq = pd.Series(text).value_counts()
#         return freq

# def _remove_common_words(x, freq, n=20):
#         fn = freq[:n]
#         x = ' '.join([t for t in x.split() if t not in fn])
#         return x

# def _remove_rarewords(x, freq, n=20):
#         fn = freq.tail(n)
#         x = ' '.join([t for t in x.split() if t not in fn])
#         return x

# def _remove_dups_char(x):
#         x = re.sub("(.)\\1{2,}", "\\1", x)
#         return x

# def _get_basic_features(df):
#         if type(df) == pd.core.frame.DataFrame:
#             df['char_counts'] = df['text'].apply(lambda x: _get_charcounts(x))
#             df['word_counts'] = df['text'].apply(lambda x: _get_wordcounts(x))
#             df['avg_wordlength'] = df['text'].apply(lambda x: _get_avg_wordlength(x))
#             df['stopwords_counts'] = df['text'].apply(lambda x: _get_stopwords_counts(x))
#             df['hashtag_counts'] = df['text'].apply(lambda x: _get_hashtag_counts(x))
#             df['mentions_counts'] = df['text'].apply(lambda x: _get_mentions_counts(x))
#             df['digits_counts'] = df['text'].apply(lambda x: _get_digit_counts(x))
#             df['uppercase_counts'] = df['text'].apply(lambda x: _get_uppercase_counts(x))
#         else:
#             print('ERROR: This function takes only Pandas DataFrame')
            
#         return df


# def _get_ngram(df, col, ngram_range):
#         vectorizer = CountVectorizer(ngram_range=(ngram_range, ngram_range))
#         vectorizer.fit_transform(df[col])
#         ngram = vectorizer.vocabulary_
#         ngram = sorted(ngram.items(), key = lambda x: x[1], reverse=True)

#         return ngram

   
# def get_clean(x):
#         x = str(x).lower().replace('\\', '').replace('_', ' ')
#         x = _cont_exp(x)
#         x = _remove_emails(x)
#         x = _remove_urls(x)
#         x = _remove_html_tags(x)
#         x = _remove_accented_chars(x)
#         x = _remove_special_chars(x)
#         x = re.sub("(.)\\1{2,}", "\\1", x)
#         return x

    # df= pd.read_csv("app/reviews.csv",usecols=["reviewText","overall"])

    # df["reviewText"]=df["reviewText"].apply(lambda x:get_clean(x))



    # tfidf = TfidfVectorizer(max_features=20000,ngram_range=(1,5),analyzer='char')
    # x= tfidf.fit_transform(df["reviewText"])
    # y=df["overall"]
    # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
    # clf= LinearSVC(C=20, class_weight="balanced")
    # clf.fit(x_train,y_train)
    # y_pred = clf.predict(x_test)
@api_view(['GET'])
def ratereview(request,review):
    def _get_wordcounts(x):
        length = len(str(x).split())
        return length

    def _get_charcounts(x):
            s = x.split()
            x = ''.join(s)
            return len(x)
    def _get_avg_wordlength(x):
            count = _get_charcounts(x)/_get_wordcounts(x)
            return count

    def _get_stopwords_counts(x):
            l = len([t for t in x.split() if t in stopwords])
            return l

    def _get_hashtag_counts(x):
            l = len([t for t in x.split() if t.startswith('#')])
            return l

    def _get_mentions_counts(x):
            l = len([t for t in x.split() if t.startswith('@')])
            return l
    def _get_digit_counts(x):
            digits = re.findall(r'[0-9,.]+', x)
            return len(digits)

    def _get_uppercase_counts(x):
            return len([t for t in x.split() if t.isupper()])

    def _cont_exp(x):
            abb = json.load(open("app/abbr.json"))
        
            if type(x) is str:
                for key in abb:
                    value = abb[key]
                    x = x.replace(key, value)
                return x
            else:
                return x


    def _get_emails(x):
            emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', x)
            counts = len(emails)

            return counts, emails


    def _remove_emails(x):
            return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

    def _get_urls(x):
            urls = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)
            counts = len(urls)

            return counts, urls

    def _remove_urls(x):
            return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

    def _remove_rt(x):
            return re.sub(r'\brt\b', '', x).strip()

    def _remove_special_chars(x):
            x = re.sub(r'[^\w ]+', "", x)
            x = ' '.join(x.split())
            return x

    def _remove_html_tags(x):
            return BeautifulSoup(x, 'lxml').get_text().strip()

    def _remove_accented_chars(x):
            x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            return x

    def _remove_stopwords(x):
            return ' '.join([t for t in x.split() if t not in stopwords])	

    def _make_base(x):
            x = str(x)
            x_list = []
            doc = nlp(x)
            
            for token in doc:
                lemma = token.lemma_
                if lemma == '-PRON-' or lemma == 'be':
                    lemma = token.text

                x_list.append(lemma)
            return ' '.join(x_list)

    def _get_value_counts(df, col):
            text = ' '.join(df[col])
            text = text.split()
            freq = pd.Series(text).value_counts()
            return freq

    def _remove_common_words(x, freq, n=20):
            fn = freq[:n]
            x = ' '.join([t for t in x.split() if t not in fn])
            return x

    def _remove_rarewords(x, freq, n=20):
            fn = freq.tail(n)
            x = ' '.join([t for t in x.split() if t not in fn])
            return x

    def _remove_dups_char(x):
            x = re.sub("(.)\\1{2,}", "\\1", x)
            return x

    def _get_basic_features(df):
            if type(df) == pd.core.frame.DataFrame:
                df['char_counts'] = df['text'].apply(lambda x: _get_charcounts(x))
                df['word_counts'] = df['text'].apply(lambda x: _get_wordcounts(x))
                df['avg_wordlength'] = df['text'].apply(lambda x: _get_avg_wordlength(x))
                df['stopwords_counts'] = df['text'].apply(lambda x: _get_stopwords_counts(x))
                df['hashtag_counts'] = df['text'].apply(lambda x: _get_hashtag_counts(x))
                df['mentions_counts'] = df['text'].apply(lambda x: _get_mentions_counts(x))
                df['digits_counts'] = df['text'].apply(lambda x: _get_digit_counts(x))
                df['uppercase_counts'] = df['text'].apply(lambda x: _get_uppercase_counts(x))
            else:
                print('ERROR: This function takes only Pandas DataFrame')
                
            return df


    def _get_ngram(df, col, ngram_range):
            vectorizer = CountVectorizer(ngram_range=(ngram_range, ngram_range))
            vectorizer.fit_transform(df[col])
            ngram = vectorizer.vocabulary_
            ngram = sorted(ngram.items(), key = lambda x: x[1], reverse=True)

            return ngram

    
    def get_clean(x):
            x = str(x).lower().replace('\\', '').replace('_', ' ')
            x = _cont_exp(x)
            x = _remove_emails(x)
            x = _remove_urls(x)
            x = _remove_html_tags(x)
            x = _remove_accented_chars(x)
            x = _remove_special_chars(x)
            x = re.sub("(.)\\1{2,}", "\\1", x)
            return x

    review=get_clean(review)
    model = pickle.load(open("./api/model.sav", "rb"))
    scaled = pickle.load(open("./api/scaler.sav", "rb"))
    prediction = model.predict(scaled.transform([review]))
    return HttpResponse(str(prediction[0]))


@api_view(['GET'])
def wordcounter(request,sentence): 
    sentence=sentence.replace('#','')  
    sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
    wordlist=sentence.split()
    for word in wordlist:
        if chr(35) in word:
            continue
    cnt=len(wordlist)
    cnt1=cnt
    sentence1=sentence
    word_count = wordcounterModel.objects.create(sentence=sentence1, count=cnt1).save()
    return HttpResponse(str(cnt))
    
@api_view(http_method_names=['GET','POST'])
def wordcounterView(request):
    if request.method=='GET':
        return wordcounterget(request)
    elif request.method=='POST':
        return wordcounterpost(request)

def wordcounterget(request):
    try:
        data= wordcounterModel.objects.all()
        serializer= wordcounteSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
#temp=temp_view()
def wordcounterpost(request):
    hdata = wordcounterModel()
    word_count = wordcounterModel.objects.all()
    serializer=wordcounteSerializer(hdata,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
