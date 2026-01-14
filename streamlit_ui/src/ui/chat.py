import streamlit as st
from src.services import model_client
from src.ui.history import display_history


def chat_interface() -> None:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    display_history()

    st.header("Chat")

    # In-memory message history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):

            if message["type"] == "text":
                st.markdown(message["content"])

            elif message["type"] == "image":
                st.image(
                    message["content"],
                    caption=message.get("caption", ""),
                    use_container_width=True,
                )

    if prompt := st.chat_input(
        "Write request. (Pro tip: use '/imagine' to generate an image)",
    ):
        # Save message
        st.session_state.messages.append(
            {"role": "user", "type": "text", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            with st.spinner("Generating response..."):
                response = model_client.get_chat_response(prompt)

                if response.response_type[0].value == "text":

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "type": "text",
                            "content": response.content[0],
                        }
                    )

                    with st.chat_message("assistant"):
                        st.markdown(response.content[0])

                elif response.response_type[0].value == "image":
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "type": "image",
                            "content": response.content,
                            "caption": prompt,
                        }
                    )

                    with st.chat_message("assistant"):
                        st.image(
                            response.content, caption=prompt, use_container_width=True
                        )

                elif response.response_type[0].value == "error":
                    st.error(f"Error: {response.error_message}")

        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
