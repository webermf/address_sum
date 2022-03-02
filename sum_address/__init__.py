from flask import Flask, request, abort, jsonify

def create_app():
    # create and configure the app
	app = Flask(__name__)

	@app.errorhandler(400)
	def wrong_format(e):
		return jsonify(error = 400, text="Malformed query"), 400

	@app.get("/")
	def hello():
		return "Please submit your post-request to https://sumaddress.herokuapp.com/compute_sum"	

	@app.post("/compute_sum")
	def compute_address_sum():
		try:
			return {"result": sum(request.get_json()["address"]["values"])}, 200
		except:
			abort(400)

	return app

if __name__ == "__main__":
	app = create_app()
	app.run()
