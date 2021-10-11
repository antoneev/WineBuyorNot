import streamlit as st
import numpy as np
import pickle
import pandas as pd

class Dashboard:
    def __init__(self):
        self.model = pickle.load(open('files/wineQualityModel.pkl', 'rb'))
        datasetMixMax = pd.read_csv('files/dataframeMixMaxValues.csv')
        self.fixedAcidity = 0
        self.volatileAcidity = 0
        self.citricAcid = 0
        self.residualSugar = 0
        self.chlorides = 0
        self.freeSulfurDioxide = 0
        self.totalSulfurDioxide = 0
        self.density = 0
        self.pH = 0
        self.sulphates = 0
        self.alcohol = 0
        self.wineQuality = 0
        self.pageTile = 0
        self.predictedYes = 0
        self.predictedNo = 0
        self.fixedAcidityMin = datasetMixMax.iloc[0][1]
        self.fixedAcidityMax = datasetMixMax.iloc[0][2]
        self.volatileAcidityMin = datasetMixMax.iloc[1][1]
        self.volatileAcidityMax = datasetMixMax.iloc[1][2]
        self.citricAcidMin = datasetMixMax.iloc[2][1]
        self.citricAcidMax = datasetMixMax.iloc[2][2]
        self.residualSugarMin = datasetMixMax.iloc[3][1]
        self.residualSugarMax = datasetMixMax.iloc[3][2]
        self.chloridesMin = datasetMixMax.iloc[4][1]
        self.chloridesMax = datasetMixMax.iloc[4][2]
        self.freeSulfurDioxideMin = datasetMixMax.iloc[5][1]
        self.freeSulfurDioxideMax = datasetMixMax.iloc[5][2]
        self.totalSulfurDioxideMin = datasetMixMax.iloc[6][1]
        self.totalSulfurDioxideMax = datasetMixMax.iloc[6][2]
        self.densityMin = datasetMixMax.iloc[7][1]
        self.densityMax = datasetMixMax.iloc[7][2]
        self.pHMin = datasetMixMax.iloc[8][1]
        self.pHMax = datasetMixMax.iloc[8][2]
        self.sulphatesMin = datasetMixMax.iloc[9][1]
        self.sulphatesMax = datasetMixMax.iloc[9][2]
        self.alcoholMin = datasetMixMax.iloc[10][1]
        self.alcoholMax = datasetMixMax.iloc[10][2]

    def inputFields(self):
        self.fixedAcidity = st.number_input('Input Fixed Acidity', min_value=self.fixedAcidityMin, max_value=self.fixedAcidityMax)
        self.volatileAcidity = st.number_input('Input Volatile Acidity', min_value=self.volatileAcidityMin, max_value=self.volatileAcidityMax)
        self.citricAcid = st.number_input('Input Citric Acid', min_value=self.citricAcidMin, max_value=self.citricAcidMax)
        self.residualSugar = st.number_input('Input Residual Sugar', min_value=self.residualSugarMin, max_value=self.residualSugarMax)
        self.chlorides = st.number_input('Input Chlorides', min_value=self.chloridesMin, max_value=self.chloridesMax)
        self.freeSulfurDioxide = st.number_input('Input Free Sulfur Dioxide', min_value=self.freeSulfurDioxideMin, max_value=self.freeSulfurDioxideMax)
        self.totalSulfurDioxide = st.number_input('Input Total Sulfur Dioxide', min_value=self.totalSulfurDioxideMin, max_value=self.totalSulfurDioxideMax)
        self.density = st.number_input('Input Density', min_value=self.densityMin, max_value=self.densityMax)
        self.pH = st.number_input('Input pH', min_value=self.pHMin, max_value=self.pHMax)
        self.sulphates = st.number_input('Input Sulphates', min_value=self.sulphatesMin, max_value=self.sulphatesMax)
        self.alcohol = st.number_input('Input Alcohol', min_value=self.alcoholMin, max_value=self.alcoholMax)

    def predict(self):
            x = np.zeros(11)
            x[0] = self.fixedAcidity
            x[1] = self.volatileAcidity
            x[2] = self.citricAcid
            x[3] = self.residualSugar
            x[4] = self.chlorides
            x[5] = self.freeSulfurDioxide
            x[6] = self.totalSulfurDioxide
            x[7] = self.density
            x[8] = self.pH
            x[9] = self.sulphates
            x[10] = self.alcohol
            self.pred = self.model.predict([x])[0]

    def pageConfig(self):
        self.config = st.set_page_config(
            page_title="Wine Quality Prediction",
            page_icon="🍷",
            layout="centered",
            initial_sidebar_state="expanded",
        )

    def customHTML(self):
        self.pageTile = """
        <div style="background:#025246 ;padding:10px">
            <h2 style="color:white;text-align:center;">Wine Quality Prediction 🍷</h2>
            <h3 style="color:white;text-align:center;">GitHub Repo 
            <a target="_blank" href="https://github.com/antoneev/WineQuality">Click Here</a></h3>
        </div>
        """

        self.predictedYes = """  
        <div style="background-color:#025246; padding:10px">
            <h2 style="color:white; text-align:center; font-weight:bold;"> Buy? Yes 👍 </h2>
        </div>
        """

        self.predictedNo = """  
        <div style="background-color:#ff0000; padding:10px">
            <h2 style="color:white; text-align:center; font-weight:bold;"> Buy? No 👎 </h2>
        </div>
        """

dashboard = Dashboard()
dashboard.pageConfig()
dashboard.customHTML()
st.markdown(dashboard.pageTile, unsafe_allow_html = True)
dashboard.inputFields()

if st.button('Predict'):
    dashboard.predict()
    pred = dashboard.pred

    if pred == 0:
        st.markdown(dashboard.predictedNo, unsafe_allow_html=True)
    elif pred == 1:
        st.markdown(dashboard.predictedYes, unsafe_allow_html=True)
    else:
        st.error('Sorry, it seems to be an error. Please re-run the algorithm.')