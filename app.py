import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

# 스트림릿 앱 시작
st.title("ChatGPT 기반 챗봇")
st.write("사용자의 질문에 챗GPT 응답을 제공합니다. 원하는 질문을 입력하세요!")

# 사용자 입력 창
user_input = st.text_input("질문 또는 지시사항을 입력하세요:", "")

# 응답 표시 창
response_placeholder = st.empty()

# OpenAI API 호출 함수
def get_chat_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

# 사용자가 입력하면 응답 생성
if user_input:
    with st.spinner("챗봇이 응답을 생성 중입니다..."):
        response = get_chat_response(user_input)
    response_placeholder.markdown(f"**챗봇의 응답:**\n\n{response}")
