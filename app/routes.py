from  app import app
from flask import render_template, url_for, request
from TraceRoute import Traceroute
from IPGraph import Ipgraph
trace = Traceroute()
graph = Ipgraph()
@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html',title='Home')
@app.route('/traceIP',methods=['POST','GET'])
def traceIP():

       if request.method == 'POST':
           ip = request.form['ip']
           trace.findIps("facebook.com")
           ip_list = trace.getIpList()
           print(ip_list)
           graph.set_Graph(ip_list)
       return render_template('graph.html',title='Graph')
