import streamlit as st 
import pandas as pd 
import requests 
import json 
import pandas as pd 
from data_collect import load_data

def main():
    result = load_data()
    st.data_editor(result)
    SGG_NM = st.selectbox("지역구를 선택하세요", sorted(list(result['SGG_NM'].unique())))
    st.write(SGG_NM)

    st.data_editor(result.loc[result['SGG_NM'] == SGG_NM, :])
    st.title("완성")

    # 샘플 코드 
    st.subheader("테스트")

if __name__ == "__main__":
    main()