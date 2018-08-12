#!/usr/bin/python36

import cgi
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tkinter 
import cookie
import subprocess as sp


form=cgi.FieldStorage()
form_query=form.getvalue('query')
form_state=form.getvalue('state')
data = pd.read_csv('data.csv' , sep="\t")
ddata = data.query("Group_Name=='Dowry Deaths'")
mdata = data.query("Group_Name=='Cruelty by Husband and Relatives'")
sddata = ddata.query("Area_Name=='Rajasthan'")
smdata = mdata.query("Area_Name=='Rajasthan'")
descdata = pd.read_csv('descdata.csv')

def print_plot(dataset):
            fig=plt.figure()
            y1 = dataset['Cases_Convicted']
            y2 = dataset['Cases_Reported']
            x = dataset['Year']
            plt.plot(x,y1, color='red')
            plt.xlabel('Year')
            plt.plot(x,y2)
            plt.ylabel('No. of cases')
            plt.legend()
            fig.savefig('../html/downloads/my.png', dpi=300)
    

def nlp(query, state):
    for law in descdata.iterrows():
        if law[1][0] in query:
            print('<h1>' + law[1][1] + "</h1><br><br>" +  law[1][2])
            print_plot(globals()[law[1][3]])



def show_body_content():


    nlp(form_query, form_state)

    print('''
                    <br>
                    <img src="../downloads/my.png" width="60%" height="70%" >




            <!-- Add socket JS library -->
            <script src="/js/socket_speech.js"></script>

            <!-- Add speech synthesizer JS library -->
            <script src="/js/say.js"></script>

            <!-- Add speech recognition JS library -->
            <script src="/js/annyang.min.js"></script>

            <!-- Add speech recognition GUI JS library -->
            <script src="/js/speechkitt.min.js"></script>

            <!-- Add speech processor JS library -->
            <script src="/js/speech.js"></script>
        </div>
        ''')


def show_start_content():
    f = open('../html/start_content.txt', 'r')
    print(f.read())
    f.close()


def show_end_content():
    f = open('../html/end_content.txt', 'r')
    print(f.read())
    f.close()


def print_headers():
    print("content-type: text/html \n")

def redirect_login():
    print("""
        <script>window.location = "/login.html";</script>
        """)


def auth_user():
    ck_usr = cookie.auth_client()
    if ck_usr == True:
        pass
    else: 
        redirect_login()


def main():
    print_headers()
    auth_user()
    show_start_content()
    show_body_content()
    show_end_content()


main()
