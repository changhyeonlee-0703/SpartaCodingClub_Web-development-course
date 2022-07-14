from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.210xc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 저장 - 예시
# doc = {'name':'bobby','age':21}
#db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
user = db.users.find_one({'id': '12313123', 'pw': 'asda'})

print(user)
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
#all_users = list(db.users.find({},{'_id':False}))

#print(all_users)
# 바꾸기 - 예시
#db.users.update_one({'name':'tom'},{'$set':{'age':55}})

# # 지우기 - 예시
#db.users.delete_one({'name':'bobby'})





