# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 11:09:09 2025

@author: SKYLAB
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
with st.sidebar:
    Menu = option_menu(
        "Navegação", ["Iniciar", "Estatística", "Pesquisar", "Dados"],
        menu_icon="cast",
        icons=["house", "bar-chart", "search", "graph-up-arrow"],
        default_index=0
        )

st.title ("Dannyboy App")
df=pd.DataFrame({"x":[1, 2],"y":[1, 2]})
if Menu == "Iniciar":
    st.title("Welcome, This is the Fresh One")

if Menu == "Estatística":
    st.title("Estatística Descritiva dos Dados")
    st.write(df.describe())
    
if Menu == "Pesquisar":
    st.title("Resultados")
    
    s=pd.Series([909976, 8615246, 2872086, 2273305], name="População", index=["Estocolmo", "Londres", "Roma", "Paris"])
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    s.plot (ax=axes[0], kind='line', title='linha')
    s.plot (ax=axes[1], kind='bar', title='barra')
    s.plot (ax=axes[2], kind='box', title='box')
    s.plot (ax=axes[3], kind='pie', title='circular')
    round (s.describe(), 2)
    st.pyplot(fig)

 
if Menu == "Dados":
    st.title("Gráficos")
    
    x = np.linspace(-5, 2, 100)
    y1 = x**3 + 5*x**2 + 10
    y2 = 3*x**2 + 10*x
    y3 = 6*x + 10
    fig, ax = plt.subplots ()
    ax.plot(x, y1, color="blue", label="y(x)")
    ax.plot(x, y2, color="red", label="y'(x)")
    ax.plot(x, y3, color="green", label="y''(x)")
    ax.set_xlabel ("tempo")
    ax.set_ylabel ("espaço")
    ax.legend ()
    st.pyplot(fig)
    
    
   