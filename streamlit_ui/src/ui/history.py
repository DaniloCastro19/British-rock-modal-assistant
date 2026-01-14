from typing import Any
import streamlit as st
import base64
from src.services import model_client


def display_history() -> Any:

    with st.sidebar:
        st.header("Conversation History")

        if st.button("Load complete history", use_container_width=True):

            try:
                st.session_state.full_history = model_client.get_chat_history()
            except Exception as e:
                st.error(f"Error loading history: {e}")

        if "full_history" in st.session_state:
            st.subheader("All interactions")
            for entry in st.session_state.full_history:
                with st.expander(f"{entry['timestamp']}: {entry['prompt'][:50]}..."):
                    st.write(f"Prompt: {entry['prompt']}")
                    if entry["response_type"] == "text":
                        st.write(f"Answer: {entry['response']}")

                    else:
                        try:
                            image_bytes = base64.b64decode(entry["response"])
                            st.image(
                                image_bytes,
                                caption=entry["prompt"],
                                use_container_width=True,
                            )

                        except:
                            st.error("Error showing history image")
