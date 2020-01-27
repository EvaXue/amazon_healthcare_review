import pymysql, os, json
import mysql.connector
import glob


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val



cnn = mysql.connector.connect(
    user='root',
    password='root',
    host='127.0.0.1',
    database='Amazon_review',
    port='3307')
print ("Amazon_review connection works!")
cursor = cnn.cursor()


# read JSON file which is in the next parent folder
file = os.path.abspath('comments/Comment_full') + "/B00H34CMHU.json"
temp_path = os.path.abspath('comments/Comment_full') + "/*.json"
ALL_JSON = glob.glob(temp_path)
print (ALL_JSON)
for json_obj in ALL_JSON:
    print json_obj
    # parse json data to SQL insert
    with open(json_obj) as f:
        for i, item in enumerate(json.load(f)):
            review = validate_string(item.get("body", None))
            product_id = validate_string(item.get("product_id", None))
            rating = validate_string(item.get("rating", None))
            review_url = validate_string(item.get("review_url", None))
            review_date = validate_string(item.get("review_date", None))
            title = validate_string(item.get("title", None))
            helpful_votes = validate_string(item.get("helpful_votes", None))
            print helpful_votes
            if helpful_votes == 'One':
                helpful_votes ='1'




            cursor.execute("INSERT INTO helpful_review (review,	product_id,	rating,review_url,review_date,title,helpful_votes) VALUES (%s,%s,%s,%s,%s,%s,%s)", (review,	product_id,	rating,review_url,review_date,title,helpful_votes))
            cnn.commit()
cursor.close()