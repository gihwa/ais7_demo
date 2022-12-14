

# π
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib


st.set_page_config(
    page_title="Likelion AI School μλμ°¨ μ°λΉ App",
    page_icon="π",
    layout="wide",
)

st.markdown("# μλμ°¨ μ°λΉ π")
st.sidebar.markdown("# μλμ°¨ μ°λΉ π")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
data = load_data(url)
data_load_state.text("Done! (using st.cache)")


st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

if selected_year > 0 :
   data = data[data.model_year == selected_year]



# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if len(selected_origin) > 0:
   data = data[data.origin.isin(selected_origin)]


st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])


fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=data, x="origin").set_title("μ§μ­λ³ μλμ°¨ μ°λΉ λ°μ΄ν° μ")
st.pyplot(fig)

pxh = px.histogram(data, x="origin", title="μ§μ­λ³ μλμ°¨ μ°λΉ λ°μ΄ν° μ")
st.plotly_chart(pxh)

bb = px.histogram(data, x="cylinders", title="νλ λ κ·Έλ¦¬κΈ°")
st.plotly_chart(bb)

cc = px.histogram(data, x="origin", y="horsepower", title="λλ² κ·Έλ¦¬κΈ°")
st.plotly_chart(cc)

# μ§κΈν λ³μ₯μ΄μ¬λͺ¨ λ°λΌνκΈ°
aa = sns.lmplot(data=data, x="mpg", y="weight", hue="origin")
st.pyplot(aa)
