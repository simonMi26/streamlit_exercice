import streamlit as st
import pandas as pd
st.title("Exercices")

st.header("Veuillez installer streamlit et pandas")
st.code("""
import streamlit as st
import pandas as pd
""")

# exercice 1
st.header("Afficher le Dataset")
df=pd.read_csv("Dataset_exercice.csv")
st.dataframe(df)

st.write("À vous de trouver les fonctions manquantes :")

st.code("""
*****("Afficher le Dataset")
df=pd.read_csv("Dataset_exercice.csv")
*********(df)""")


# exercice 2
st.header("Créer un filtre année")
filtre_annee=sorted(df["Annee_voiture"].unique())
annee=st.selectbox("Filtre année",filtre_annee)
st.dataframe(df.loc[df["Annee_voiture"]==annee])

st.write("À vous de trouver les fonctions manquantes :")
st.code("""
filtre_annee=sorted(df["Annee_voiture"].unique())
annee=*******("Filtre années",filtre_annee)
********(df.loc[df["Annee_voiture"]==annee])""")
    

# Exercice 3
st.header("Afficher un graphique :")
df_ex3=df["marque_voiture"].value_counts()
st.bar_chart(df_ex3)

st.write("À vous de trouver les fonctions manquantes :")
st.code(""" 
df_ex3=df["marque_voiture"].value_counts()
*********(df_ex3)
""")

df_ex4=df["Annee_voiture"].value_counts()
st.line_chart(df_ex4)

st.code(""" 
df_ex4=df["Annee_voiture"].value_counts()
*********(df_ex4)
""")


#Exercice 4
st.header("Utiliser des colonnes")

marque_voiture=df["marque_voiture"].unique()
annee=df["Annee_voiture"].unique()
col1, col2=st.columns(2)
col1.line_chart(df_ex4,use_container_width=True)
col2.bar_chart(df_ex3)

st.write("À vous de trouver les fonctions manquantes :")
st.code(""" 
marque_voiture=df["marque_voiture"].unique()
annee=df["Annee_voiture"].unique()
***********************
******.line_chart(df_ex4)
******.bar_chart(df_ex3)
""")


st.header("Afficher une carte")
carte=df[["latitude","longitude"]]
st.map(carte)

st.code("""
carte=df[["latitude","longitude"]]
********(carte)
""")


st.header("Prenez-vous en photo puis envoyer là sur Slack")
picture = st.camera_input("camera")
if picture:
    st.image(picture)
    st.balloons()
    st.snow()




