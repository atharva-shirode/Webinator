from django.http import request
from django.shortcuts import render
#from . import variables
import sys
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup  # BeautifulSoup is in bs4 package
import requests
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import random
import numpy as np
try:
  from googlesearch import search
except ImportError:
  print("No module named 'google' found")

from nltk import tokenize
from operator import itemgetter
import math
from rake_nltk import Rake
import itertools
#from .import views
import cgi

tutorials = ['geeksforgeeks', 'w3schools' ,'guru99', 'explore database','tutorialspoint','khanacademy','tutorial', 'example', 'examples', 'exercise', 'code', 'practical' ,'tutorials', 'mcq', 'beginners','sample papers', 'python programming' ,'java programming','c programming','c++ programming','mock','quiz', 'course', 'code snippet','code snippets','syllabus','machine learning' , 'certification', 'coursera' ,'data science','pseudo code','edureka','learning' , 'algorithms','algorithm' , 'conclusion' , 'introduction' ,'stackoverflow','hackerrank','leetcode','onlinegdb','codechef','freecodecamp','sololearn','sitepoint','javatpoint','c','cpp','c++','java','python','mysql','ruby','django','flask','mongodb','nodejs','sqlite']
reviews = [ 'reviews','travel','travelling','journey','place','visit','plan', 'gsmarena', 'review','box office','movie', 'rating', 'stars','collection','crores', 'imdb','bookmyshow' , 'cast' , 'entertainment', 'film','filmstar', 'films','actor','actors','actress' , 'worldwide','gross', 'release date', 'launch date' , 'questions', 'details', 'hardware', 'full specification', 'compare' , 'comparison' , 'trending' , 'price' , 'product', 'specifications' , 'specs' , 'key specifications' , 'key specs' , 'user review' , 'user reviews' , 'pricing' ,'gadgets 360','gadgets360','key','benchmarks','gpu','processor','cpu','nvidia','amd','intel','preview','camera','battery life','charging','petrol','milage','engine','gear','speed','car','carwale','cardekho']
news = ['ndtv','cnbc','news18','forbes','financialexpress','indianexpress','trending','politics','political parties','bjp','congress','prime minister','pm','topic','leaders','india','top news','news','today','timesofindia','bbc','cnn','economics time','thehindu','india','election','livemint','aljazeera','journalist','latest news','covid','vaccine','vaccination','world','quarantine','immunity','online exams','newsletter','vote','economy','market','conspiracy','crime','women safety','fake feminism','emergency','rally','et','toi','polling','politician','politicians','bse','sensex','bmc','climate change','summer','heat','temperature','global warming','the guardian','diplomat','win','draw','loose','score','hit','qualify','relegate','knock']
socialmedia = ['instagram','pinterest','facebook','linkedin','github','hashtags','twitter','post','like','likes','posts','tweet','friends','followers','following','follow','comment','comments','share','reddit','twitter']
information = ['youtube','edu','biography','britannica','quora','ieee','researchgate','springer','research','wiki','encylopedia','retanica' ,'stackoverflow','wikipedia','blog','blogs','info','information','blogpost','gov','doubt','doubts','question','questions','solution','answer','answers','solutions','data','guide','knowledge','analyze','analysis','author','writer']
shopping = ['bookmyshow','order','ordering','cart','store','irctc','transaction','payment','ticket','movie','book','booking','track','train','flght','flights','aeroplane', 'amazon', 'flipkart', 'snapdeal', 'myntra', 'shoppersstop', 'alibaba','best','under','price','filter','discount','sale','stock','buy','sell','rent','delivery','for sale','not available','out of stock','mart','ebay','paytm','google pay','gpay','nike','adidas','puma','brand','shoes','mobile','laptop','bike','bikes','category','ebay','shopclues','shop','shopping','ecommerce','e-commerce']


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

#urls
def searcher(request):

  return render(request,'search.html')



def home(request):
  #query = requests.NullHandler
  #form = cgi.FieldStorage()
  #query =  form.getvalue('searchbox')
  query=request.POST.get('searchbox')
  print(query)




  connect = {

    'q1' : query

  }
  global tut
  global rev
  global info
  global social
  global sh
  global ot
  global n
  tut = []  #tutorials
  rev = []  #reviews
  info = [] #information
  social = [] #socialmedia
  sh = [] #shopping
  ot = [] #others
  n = [] #news

  my_dict = {}
  temp_dict = {}
  categories = {}
  for j in search(str(query),tld='com',start=0, num=10,stop=40,pause=2):
    try:
      print(j)
      URL = j
      content = requests.get(URL)
      soup = BeautifulSoup(content.text, 'html.parser')
      temp = []
      #print("------1------")
      #res = URL.split('/')[3:]
      res = re.split('/|-|_', URL)
      #print(res)
      domain = urlparse(URL).netloc
      #print("The base URL is : " + domain)
      temp.append(res)

      domain = domain.split('.')
      temp.append(domain)
      #print("------2------")
      #print("TITLE tag")
      row1 = soup.find_all('title')
      for row in row1:  # Print all occurrences
        r = Rake()
        # print(row.get_text())
        r.extract_keywords_from_text(row.get_text())
        temp.append(r.get_ranked_phrases()[0:])
      #print("------3------")
      #print("H1 Tag")
      row2 = soup.find_all('h1')
      for row in row2:  # Print all occurrences
        r = Rake()
        # print(row.get_text())
        r.extract_keywords_from_text(row.get_text())
        temp.append(r.get_ranked_phrases()[0:])
        # print(row.get_text())
      #print("------4------")
      #print("H2 Tag")
      row3 = soup.find_all('h2')
      for row in row3:  # Print all occurrences
        r = Rake()
        #print(row.get_text())
        r.extract_keywords_from_text(row.get_text())
        temp.append(r.get_ranked_phrases()[0:])
        # print(row.get_text())
      #print("------5------")
      #print("H3 Tag")
      row4 = soup.find_all('h3')
      for row in row4:  # Print all occurrences
        r = Rake()
        #print(row.get_text())
        r.extract_keywords_from_text(row.get_text())
        temp.append(r.get_ranked_phrases()[0:])
        # print(row.get_text())
      #print("------6------")

      temp1 = []
      [temp1.extend(el) for el in temp]
      temp1 = list(set(temp1))

      # print("Category for " + URL + "is \n")
      temp_dict['tutorials'] = len(intersection(temp1,tutorials))
      # print(len(intersection(temp1,tutorials)))
      # print(intersection(temp1,tutorials))
      temp_dict['reviews'] = len(intersection(temp1, reviews))
      # print(len(intersection(temp1, reviews)))
      # print(intersection(temp1, reviews))
      temp_dict['news'] = len(intersection(temp1, news))
      # print(len(intersection(temp1, news)))
      # print(intersection(temp1, news))
      temp_dict['socialmedia'] = len(intersection(temp1, socialmedia))
      # print(len(intersection(temp1, socialmedia)))
      # print(intersection(temp1, socialmedia))
      temp_dict['information'] = len(intersection(temp1, information))
      # print(len(intersection(temp1, information)))
      # print(intersection(temp1, information))
      temp_dict['shopping'] = len(intersection(temp1, shopping))
      # print(len(intersection(temp1, shopping_business)))
      # print(intersection(temp1, shopping_business))

      keymax = max(temp_dict, key=temp_dict.get)

      #print("------7------")

      if temp_dict[keymax] == 0:
        keymax = "others"
        #print(keymax)

      key = keymax
      categories.setdefault(key, [])
      categories[key].append(URL)
      # print("-------")
      # print(categories)
      my_dict[j] = temp1

    except:

      continue


  global labels
  labels = []
  global values
  values = []
  global query_name
  query_name = str(query).split(" ")

  for i in categories :
    x= categories[i]
    labels.append(i)
    values.append(len(categories[i]))

    if i == 'tutorials':
      for j in x:
        tut.append(j)

    if i == 'reviews':
      for j in x:
        rev.append(j)

    if  i == 'information':
      for j in x:
        info.append(j)

    if i == 'socialmedia':
      for j in x:
        social.append(j)

    if i == 'shopping':
      for j in x:
        sh.append(j)

    if i == 'news':
      for j in x:
          n.append(j)

    if i == 'other':
      for j in x:
          ot.append(j)


  print(categories)
  print ("Dict key-value are : ")
  for i in categories :
    print(i)
    print(categories[i])
    print("\n")

  print("Connect")
  print(connect)


  connect = {
    'q1' : query,
    'tutorials': tut,
    'reviews': rev,
    'information': info,
    'socialmedia': social,
    'shopping': sh,
    'news': n,
    'other': ot
  }
  query = None
  print("The query is updated to  ", query)
  return render(request,'home.html',connect)


def piechart(request):
  # Creating plot
  print(values)
  #print(labels)

  
  # fig = plt.figure(figsize=(10, 7))
  plt.pie(values, labels=labels)
  path = query_name[0]
  plt.savefig(path, dpi=100)
  c = {
  'source' : "D:/Experiments/MP/Mp-2/aptwebinator/media"+path+".png"
  }
  return render(request, 'piechart.html',c)
