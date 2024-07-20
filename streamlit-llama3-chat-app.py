import json
import streamlit as st
from datetime import datetime

def save_to_json(human_input, ai_output):
    data = {
        "messages": [
            {"role": "human", "content": human_input},
            {"role": "assistant", "content": ai_output}
        ]
    }
    
    filename = f"chat_data_{datetime.now().strftime('%Y%m%d')}.json"
    
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        f.write('\n')  # 각 JSON 객체를 새 줄에 추가
    
    return filename

st.title("LLaMA-3 ChatTemplate Input/Output Logger")

human_input = st.text_area("Human Input", height=200)
ai_output = st.text_area("AI Output", height=200)

if st.button("Save"):
    if human_input and ai_output:
        filename = save_to_json(human_input, ai_output)
        st.success(f"Data saved to {filename}")
    else:
        st.warning("Please enter both input and output before saving.")
