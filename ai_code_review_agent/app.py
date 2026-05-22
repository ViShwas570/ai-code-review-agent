
import streamlit as st
from repo_handler import clone_repo
from parser_utils import extract_python_data
from reviewer import review_code
from output_formatter import generate_markdown

st.set_page_config(page_title="AI Code Review Agent")

st.title("🤖 AI Code Review Agent")

repo_url = st.text_input("Enter GitHub Repository URL")

if st.button("Analyze Repository"):
    if repo_url:
        with st.spinner("Cloning repository..."):
            repo_path = clone_repo(repo_url)

        with st.spinner("Parsing files..."):
            parsed_files = extract_python_data(repo_path)

        results = []

        with st.spinner("Reviewing code with AI..."):
            for item in parsed_files:
                review = review_code(item["code"])

                results.append({
                    "file": item["file"],
                    "review": review
                })

        st.success("Analysis Completed")

        for result in results:
            st.subheader(result["file"])

            for comment in result["review"]["comments"]:
                st.write(f"### {comment['issue']}")
                st.write(f"Severity: {comment['severity']}")
                st.write(f"Confidence: {comment['confidence']}%")
                st.write(f"Suggestion: {comment['suggestion']}")

                if comment["confidence"] < 60:
                    st.warning("VERIFY THIS")

        markdown_report = generate_markdown(results)

        st.download_button(
            label="Download Markdown Report",
            data=markdown_report,
            file_name="review_report.md",
            mime="text/markdown"
        )
