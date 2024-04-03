import streamlit as st

import math
from streamlit import option_menu 


st.title('Maukkan Senyawa')

option = st.selectbox('Pilih Senyawa', ('NaOH','HCl'))

st.write('Anda Memilih:', option)


