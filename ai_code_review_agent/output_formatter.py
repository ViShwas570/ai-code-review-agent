
def generate_markdown(results):
    md = "# AI Code Review Report\\n\\n"

    for file_result in results:
        md += f"## {file_result['file']}\\n\\n"

        for comment in file_result["review"]["comments"]:
            verify = "⚠️ VERIFY THIS" if comment["confidence"] < 60 else ""

            md += f"""
- **Issue:** {comment['issue']}
- **Severity:** {comment['severity']}
- **Confidence:** {comment['confidence']}%
- **Suggestion:** {comment['suggestion']}
{verify}

"""

    return md
