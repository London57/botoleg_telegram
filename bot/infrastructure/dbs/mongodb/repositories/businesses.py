from infrastructure.dbs.mongodb.options.db import businesses_collection


class BusinessRepository():
	collection = businesses_collection
	
	def is_have_business(self, tg_user_id):
		data = self.collection.find_one({"tg_user_id": str(tg_user_id)})
		if data:
			return True
		
	def get_businesses_by_user_id(self, tg_user_id):
		print("запрос")
		businesses = self.collection.find({"tg_user_id": str(tg_user_id)})
		return businesses.to_list()
