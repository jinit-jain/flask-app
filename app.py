# using flask_restful
import json
import random
import Analyze_Sentiment as analyze_sentiment
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
        a, b, c = analyze_sentiment.preprocess_data()

        for news_article in data["news"]:
            name = news_article["name"]
            url = news_article["url"]
            print(url)
            sentiment = {}
            article = """Reliance Industries-Rights Entitlement share price traded sharply higher on May 27, with more than 78 lakh shares volume.It touched an intraday high 
of Rs 209.90 and a low of Rs 163.75 after opening the session at Rs 177 on the National Stock Exchange.At 1439 hours, it was trading at Rs 197, up 8.48 percent over the previous day's close of Rs 181.60.The trading in RIL Rights Entitlement will continue till May 29, so that as per T+2 settlement, the eligibility for partly paid-up rights shares will be decided on the closing data of June 2.The person eligible for those shares on June 2 will have to pay the first instalment of Rs 314.25 on June 3, the closing date for the rights issue.After the finalisation, the partly paid-up rights shares will be allotted and credited to eligible shareholders by June 11 and the same will be listed on bourses on June 12.Mukesh Ambani-owned Reliance Industries plans to raise Rs 53,125 crore through the rights issue at a price of Rs 1,257 per share.The second instalment of Rs 314.25 will be due in May 2021 and the final instalment of Rs 628.50 in November 2021.This is the biggest ever rights issue by an Indian company, and the first by Reliance 
Industries in 30 years.Ahead of the closing of Rights Entitlement, RIL has already raised Rs 78,562 crore by selling over 17 percent stake in Jio Platforms over the last one month to Facebook, Silver Lake, Vista, General Atlantic and KKR.Disclaimer: Reliance Industries Ltd. is the sole beneficiary of Independent Media Trust which controls Network18 Media & Investments Ltd..reckoner_bx{ background-color: #F0F0F0; padding: 20px; font: 400 16px/22px 'Noto Serif',arial; border-radius: 5px; margin-bottom: 0px;}.reckoner_bx .rek_title{font: 700 18px/25px 'Fira Sans',arial; color: #0155A0; margin-bottom: 7px; text-transform: uppercase;}.reckoner_bx .btn_reck{border-radius: 20px; background-color: #135B9D; display: inline-block; font: 700 14px/19px 'Noto Serif',arial; padding: 8px 25px; color: #fff !important; text-decoration: none !important;}.reckoner_bx .rek_btnbx{ margin-top: 10px; }.reckoner_bx .bldcls{font-weight: bold;}Coronavirus Essential | Lockdown might be extended to June 15 as cases cross 1.5 lakh; India number may peak in July, experts say Copyright © e-Eighteen.com Ltd. All rights reserved. Reproduction of news articles, photos, videos or any other content in whole or in part in any form
        or medium without express writtern permission of moneycontrol.com is prohibited. Copyright © e-Eighteen.com Ltd All rights resderved. Reproduction of news articles, photos, videos or any other content in whole or in part in any form or medium without express writtern permission of moneycontrol.com is prohibited."""
            try:
                article = extract_article(url)
                print(article)
           
            except Exception as e:
                print('fuckoff')
                # return jsonify({"error": "fuck chuka hai"})
            sentiment = analyze_sentiment.find_subsector_company_sentiment_json_format(a, b, c, article)
            print(sentiment)
            response["relations"].append({"name": article,
                                          "url": url,
                                          "sentiment": sentiment,
                                          "article": article})
            
        # print(a, b, c, article)
        return jsonify(response) 
        # return jsonify({"success": "hein"})
  
# adding the defined resources along with their corresponding urls 
api.add_resource(extract_relation, '/extract-relation') 
  
# driver function 
if __name__ == '__main__': 
    app.run(debug = True)