from flask import *
import datetime
import operator

app = Flask(__name__)
transactions = []
#
# class Transaction:
# 	def __init__(self, P1, P2, a, t):
# 		self.P1 = P1	# Personne 1
# 		self.P2 = P2	# Personne 2
# 		self.a = a	# somme d'agent transféré
# 		self.t = t	# moment t
#
# tuple1 = ("abc", 34, True, 40, "male")


# opening the text file
with open('data.txt', 'r') as file:
	# reading each line
	for line in file:
		# reading each word
		tuple = ()
		for word in line.split():
			# displaying the words
			tuple = tuple + (word,)
			#print("Show : " + word)
		transactions.append(tuple)
file.close()

@app.route('/')
def triChronologique():
	transactions.sort(key=lambda t: t[3] )
	return'Transactions déjà effectuée : <ul>'+''.join(
						['<li>'+ format(n) for n in transactions]
					) +'</ul>\n', 200

@app.route('/newTransaction', methods = ['POST'])
def add ():
	user = request.form['P1']
	return render_template("newTransaction.html")

	P1 = request.args.get('P1')
	# P2 = request.args['p2']
	# a = request.args['a']
	# #t = request.args['t']
	# tuple = (P1, P2, a, datetime.today().strftime('%Y-%m-%d'))
	#
	# transactions.append(tuple)
	# with open('data.txt', 'a') as file:
	# 	file.write(tuple+"\n")
	# #tuple = tuple + datetime.today().strftime('%Y-%m-%d')
	# file.close()
	# return'User'+ tuple +'added.\n', 201

@app.route('/user/<uname>', methods=['DELETE'])
def rem (uname):
	if uname not in transactions:
		return'User'+ uname +'does not exists.\n',404
	transactions.remove(uname)
	# opening the text file
	with open('data.txt', 'w+') as file:
		# reading each line
		for line in file:
			for word in line.split():
				if word is uname:
					print("line = " +line)
				line = line.replace(uname, "")
			file.write(line)
	file.close()
	return'User '+ uname +' removed.\n', 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)


