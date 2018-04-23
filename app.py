from flask import Flask, url_for, render_template, request, abort
app=Flask(__name__)

@app.route('/')
def inicio():
	return render_template("inicio.html")


@app.route('/operar',methods=["POST"])
def operar():
	try:
		num1=int(request.form["num1"])
		num2=int(request.form["num2"])
	except:
		abort(404)
	op=request.form["op"]
	if op == 'sumar':
		resultado = num1+num2
		signo = '+'
	elif op == 'restar':
		resultado = num1-num2
		signo = '-'
	elif op == 'multiplicar':
		resultado = num1*num2
		signo = 'x'
	elif op == 'dividir' and num2 != 0:
		resultado = num1/num2
		signo = '/'
	else:
		abort(404)
	return render_template("operar.html",num1=num1,num2=num2,op=op,signo=signo,resultado=resultado)


#@app.route("/calculadora",methods=["GET","POST"])
#def calculadora():
#	if request.method=="GET":
#		return render_template("inicio.html")
#	else:
#		try:
#			num1=int(request.form["num1"])
#			num2=int(request.form["num2"])
#		except:
#			abort(404)
#		op=request.form["op"]
#		if op == 'sumar':
#			resultado = num1+num2
#			signo = '+'
#		elif op == 'restar':
#			resultado = num1-num2
#			signo = '-'
#		elif op == 'multiplicar':
#			resultado = num1*num2
#			signo = 'x'
#		elif op == 'dividir' and num2 != 0:
#			resultado = num1/num2
#			signo = '/'
#		else:
#			abort(404)
#		return render_template("operar.html",num1=num1,num2=num2,op=op,signo=signo,resultado=resultado)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port))
