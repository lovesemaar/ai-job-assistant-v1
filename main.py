skill_categories = {
    "Programming": ["Python", "JavaScript", "SQL"],
    "AI/GenAI": ["AI", "LLM", "RAG", "Prompt Engineering", "Embeddings"],
    "Backend": ["FastAPI", "API", "REST"],
    "DevOps": ["Docker", "GitHub", "CI/CD"],
    "Automation": ["n8n", "Make", "Zapier", "Workflow Automation"]
}


def analyze_job_description(job_description):
    found_skills = []
    missing_skills = []

    for category, skills in skill_categories.items():
        for skill in skills:
            if skill.lower() in job_description.lower():
                found_skills.append((category, skill))
            else:
                missing_skills.append((category, skill))

    return found_skills, missing_skills


def recommend_project(missing_skills):
    missing_skill_names = [skill for category, skill in missing_skills]

    if "RAG" in missing_skill_names or "Embeddings" in missing_skill_names:
        return "Build a PDF RAG chatbot that answers questions from uploaded documents."

    if "FastAPI" in missing_skill_names or "REST" in missing_skill_names:
        return "Build a FastAPI backend that analyzes job descriptions through an API endpoint."

    if "Docker" in missing_skill_names:
        return "Dockerize this Python project and document how to run it in a container."

    if "n8n" in missing_skill_names or "Workflow Automation" in missing_skill_names:
        return "Build an automation workflow that sends job analysis results to Google Sheets or email."

    return "Improve this project by adding better skill detection and a simple web interface."


def main():
    print("AI Job Assistant v2")
    print("-------------------")

    job_description = input("Paste a short job description here:\n\n")

    found, missing = analyze_job_description(job_description)

    print("\nSkills found in job description:")
    if found:
        for category, skill in found:
            print(f"- {skill} ({category})")
    else:
        print("- No matching skills found")

    print("\nSkills you may need to improve:")
    if missing:
        for category, skill in missing:
            print(f"- {skill} ({category})")
    else:
        print("- You matched all listed skills")

    print("\nRecommended project idea:")
    print(recommend_project(missing))

    print("\nSuggested next step:")
    print("Choose one missing skill and build a small project that proves it.")


if __name__ == "__main__":
    main()