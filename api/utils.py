def req_response(response):
	resp = int(str(response)[11:14])
	code = [200, 400, 401, 403, 404, 405, 409]
	mean = ['OK', 'Bad Request', 'Unauthorized', 'Forbidden', 'Not Found', 'Method Not Allowed', 'Conflict',  'Internal Server Error']
	descript = ['Everything works as expected', 
				'Any case where a parameter is invalid, or a required parameter is missing.',
				'Invalid request token',
				'The requested information is restricted',
				'Endpoint does not exist.',
				'Attempting to use POST with a GET-only endpoint, or vice-versa.',
				'The request could not be completed as it is. Use the information included in the response to modify the request and retry.',
				"Foursquare's servers are unhappy. There is either a bug on our side or there is an outage. The request is probably valid but needs to be retried later."]
	for i in range(len(code)):
		if resp == code[i]:
			print(f"Request Response : {resp} {mean[i]} ({descript[i]})")
		#else:
			#print("Something is going wrong | check your request")