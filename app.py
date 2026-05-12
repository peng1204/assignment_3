import streamlit as st

st.title("텍스트 분석기")

st.info("""
텍스트를 입력하고 버튼을 누르면 분석 결과를 보여줍니다.  
""")

st.divider()

text = st.text_area("분석할 텍스트를 입력하세요", placeholder="여기에 텍스트를 입력하세요")

if st.button("분석하기"):
    if not text.strip():
        st.warning("텍스트를 입력해 주세요!")
    else:
        result = {
            "chars": len(text.replace(" ", "").replace("\n", "")),
            "words": len(text.split()),
            "sentences": len([s for s in text.replace("?","!").replace(".","!").split("!") if s.strip()])
        }

        st.success("분석 완료!")
        c1, c2, c3 = st.columns(3)
        c1.metric("글자 수", result["chars"])
        c2.metric("단어 수", result["words"])
        c3.metric("문장 수", result["sentences"])

st.divider()