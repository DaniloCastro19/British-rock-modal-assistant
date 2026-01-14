import streamlit as st
from src.ui import layout, chat


def main() -> None:
    layout.display_header()
    chat.chat_interface()


if __name__ == "__main__":
    main()
