import streamlit as st 
import pandas as pd 
import openpyxl
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandarScaler
from sklearn.cluster import KMeans
import plotly.express as px

#Titulo para el app
st.title("K-Means Clustering con Streamlit")

#Subir archivo de excel
upload_file = st.file_uploader('Sube un archivo Excel',type=['xlsx'])

if upload_file is not None:
    try: 
        #Leer archivo excel
        df = pd.read_excel(upload_file)

        st.write('### Vista previa de los datos')
        st.write(df.head())

        #Seleccionar columnas categoricas
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

        if categorical_columns:
            st.write('### Columnas categoricas indentificadas')
            st.write(categorical_columns)

            #Convertir columnas categoricas a dummies
            df = pd.get_dummies(df,columns=categorical_columns)
            st.write('### Datos despues de la conversion a dummies')
            st.write(df.head())
        else:
            st.write('No se encontraron columnas categoricas en los datos')

        #Normalizar los datos
        scaler = StandarScaler()
        df_scaled = scaler.fit_transform(df)

        #Seleccion del numero de clusters
        st.write('### Selecciona el numero de clusters')
        num_clusters = st.slider('Numero de cluster',min_value=2,max_value=10,value=3) # 3 por defecto

        #Aplicando el K-Means
        kmeans = kmeans(num_clusters=num_clusters, random_state=42)
        clusters = kmeans.fit_predict(df_scaled)
 

    except Exception as e:
        st.error(f'Error al leer archivo excel: {e}')