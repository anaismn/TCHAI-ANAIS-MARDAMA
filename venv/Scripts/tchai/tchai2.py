from flask import Flask,  redirect, url_for, request, render_template
import hashlib
import datetime
from operator import itemgetter

app = Flask(__name__)

def getDatas() :
	transactions = []
	# opening the text file
	with open('data2.txt', 'r') as file:
		# reading each line
		for line in file:
			# reading each word
			tuple = ()
			for word in line.split():
				# displaying the words
				tuple = tuple + (word,)
				#print("Show : " + word)
			transactions.append(tuple)
	return transactions
	file.close()

def getHash(tuple):
	h = hashlib.sha256()
	h.update((' '.join(tuple)).encode())
	return h.hexdigest()

def verifIntegrite(tuple):
	if getHash(itemgetter(0,1,2,3)(tuple)) == tuple[4] :
		integre = True
	else:
		integre = False
	return integre

transactions = getDatas()

@app.route('/')
def triChronologique():
	transactions.sort(key=lambda t: t[3])

	return'Transactions déjà effectuée : <ul>'+''.join(
						['<li>'+ format(n) + " "+ str(verifIntegrite(n)) + " "+ getHash(itemgetter(0,1,2,3)(n)) for n in transactions]
					) +'</ul>\n', 200


@app.route('/newTransaction')
def formTansaction():
	return render_template('newTransaction.html')

@app.route('/newTransaction', methods = ['POST', 'GET'])
def getInfoTransaction():
	if request.method == 'POST':
		P1 = request.values.get('P1')
		P2 = request.values.get('P2')
		a = request.values.get('a')
		t = request.values.get('t')

		tuple1 = (P1, P2, a, t)
		h = getHash(tuple1)

		tuple2 = (P1, P2, a, t, h)

		transactions.append(tuple2)

		with open('data2.txt', 'a') as file:
			file.write(" ".join(tuple2)+"\n")
		#tuple = tuple + datetime.today().strftime('%Y-%m-%d')
		file.close()

		return redirect(url_for('triChronologique'))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/user/<uname>')
def triPersonneChronologique(uname):
	transactionsPersonne = []
	for n in transactions :
		if uname in (n[0] , n[1]):
			transactionsPersonne.append(n)

	transactionsPersonne.sort(key=lambda t: t[3])
	return'Transactions déjà effectuée : <ul>'+''.join(
						['<li>'+ format(n) for n in transactionsPersonne]
					) +'</ul>\n', 200


@app.route('/solde/<uname>')
def solde (uname):
#on initialise le solde à o
   Solde = 0
    #Si le nom entré est egale à p1 on procéde à un a-solde et si le nom entré est egale à p2 on fait a+solde
   for n in transactions :
      if uname == n[1]:
         Solde = Solde + int(n[2])
      if uname == n[0] :
         Solde = Solde - int(n[2])

   return 'Le solde de '+uname+' est: ' .join(
			str(Solde)
		), 200



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


