# using flask_restful
import json
import random
import Analyze_Sentiment as analyze_sentiment
import Analyze_Sentiment_Exhaustive as analyze_sentiment_exhaustive
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api
from flask_cors import CORS
from scrapping_modules.news_scrapper import extract_article 

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app)
CORS(app) 
  
# extract relation between different entities 
class extract_relation(Resource): 

    def post(self):
        data = request.get_json()
        response = {"relations" : []}
        analyze_sentiment.preprocess_data()

        for news_article in data["news"]:
            name = news_article["name"]
            url = news_article["url"]
            print(url)
            sentiment = {}
            article = "My name is khan"
            try:
                article = extract_article(url)
                #print(article)
           
            except Exception as e:
                print('fuckoff')
                # return jsonify({"error": "fuck chuka hai"})
            sentiment = analyze_sentiment.find_subsector_company_sentiment_json_format(article)
            print(sentiment)
            response["relations"].append({"name": name,
                                          "url": url,
                                          "sentiment": sentiment,
                                          "article": article})
            
        # print(a, b, c, article)
        return jsonify(response) 
        # return jsonify({"success": "hein"})

# extract relation between different entities 
class extract_relations(Resource): 

    def post(self):
        data = request.get_json()
        response = {"relations" : []}
        analyze_sentiment_exhaustive.preprocess_data()

        for news_article in data["news"]:
            name = news_article["name"]
            url = news_article["url"]
            print(url)
            sentiment = {}
            article = "My name is khan"
            try:
                article = extract_article(url)
                #print(article)
           
            except Exception as e:
                print('fuckoff')
                # return jsonify({"error": "fuck chuka hai"})
            sentiment = analyze_sentiment_exhaustive.find_subsector_company_sentiment_json_format(article)
            print(sentiment)
            response["relations"].append({"name": name,
                                          "url": url,
                                          "sentiment": sentiment,
                                          "article": article})
            
        # print(a, b, c, article)
        return jsonify(response) 
        # return jsonify({"success": "hein"})
  
# adding the defined resources along with their corresponding urls 
api.add_resource(extract_relation, '/extract-relation') 
api.add_resource(extract_relations, '/extract-relations') 
  
# driver function 
if __name__ == '__main__': 
    app.run(debug = True)