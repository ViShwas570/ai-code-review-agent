def format_markdown(results):
    markdown = "# AI Code Review Report\n\n"

    for item in results:
        markdown += f"## {item['file']}\n\n"

        for comment in item["review"]["comments"]:
            markdown += f"### Issue\n{comment['issue']}\n\n"
            markdown += f"**Severity:** {comment['severity']}\n\n"
            markdown += f"**Confidence:** {comment['confidence']}%\n\n"
            markdown += f"**Suggestion:** {comment['suggestion']}\n\n"
            markdown += "---\n\n"

    return markdown