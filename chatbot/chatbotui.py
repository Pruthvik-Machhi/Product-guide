import streamlit as st

def chatbot_interface():
    st.title("\U0001F4AC Chatbot")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display conversation history
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    # Chat input
    if prompt := st.chat_input():
        st.session_state["messages"].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        try:
            response = chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": "pruthvik"}}
            )["answer"]
        except Exception as e:
            response = "Service unavailable"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.experimental_rerun()