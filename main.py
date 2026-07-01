def analyze_job_description(job_description):
    keywords = [
        "Python",
        "SQL",
        "FastAPI",
        "AI",
        "LLM",
        "RAG",
        "Docker",
        "GitHub",
        "API",
        "Prompt Engineering"
    ]

    found_skills = []
    missing_skills = []

    for skill in keywords:
        if skill.lower() in job_description.lower():
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    return found_skills, missing_skills


def main():
    print("AI Job Assistant v1")
    print("-------------------")

    job_description = input("Paste a short job description here:\n\n")

    found, missing = analyze_job_description(job_description)

    print("\nSkills found in job description:")
    if found:
        for skill in found:
            print(f"- {skill}")
    else:
        print("- No matching skills found")

    print("\nSkills you may need to improve:")
    if missing:
        for skill in missing:
            print(f"- {skill}")
    else:
        print("- You matched all listed skills")

    print("\nSuggested next step:")
    print("Build one small project that proves 2-3 of the missing skills.")


if __name__ == "__main__":
    main()