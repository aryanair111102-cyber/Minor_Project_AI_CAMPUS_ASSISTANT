import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Campus Assistant",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🎓 Campus Assistant")
page = st.sidebar.radio("Navigate", ["💬 Chat", "📂 Admin Panel"])

# -----------------------------
# SESSION STATE (Chat Storage)
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# DUMMY AI RESPONSE FUNCTION
# -----------------------------
def get_ai_response(user_input):
    if "exam" in user_input.lower():
        return "📅 Exam registration starts from 20th May."
    elif "fees" in user_input.lower():
        return "💰 Fees last date is 25th May."
    elif "time table" in user_input.lower():
        return "📘 Timetable is available on the official portal."
    else:
        return "🤖 This is a demo response. Backend will generate real answers."

# -----------------------------
# CHAT PAGE
# -----------------------------
if page == "💬 Chat":

    # ✅ Title Branding
    st.markdown("# 🎓 AI Campus Assistant")
    st.write("Ask your campus-related questions easily!")

    # ✅ Clear Chat Button
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User input
    user_input = st.chat_input("Type your question here...")

    if user_input:
        # Show user message
        st.chat_message("user").write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # ✅ Loading Spinner
        with st.spinner("Thinking..."):
            response = get_ai_response(user_input)

        # Show AI message
        st.chat_message("assistant").write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# -----------------------------
# ADMIN PANEL
# -----------------------------
elif page == "📂 Admin Panel":

    st.title("📂 Admin Document Upload")
    st.write("Upload campus documents (PDF, TXT, DOCX)")

    uploaded_files = st.file_uploader(
        "Upload Files",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            st.success(f"✅ Uploaded: {file.name}")

    st.info("⚠️ Note: Files are not stored yet (backend needed).")

    st.subheader("📋 Uploaded Files (Demo)")
    st.write("- syllabus.pdf")
    st.write("- timetable.pdf")
    st.write("- exam_notice.pdf")
    st.markdown("---")
    st.caption("AI Campus Assistant • Demo Frontend")
