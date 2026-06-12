def understand_query(query):

    query_lower = query.lower()

    result = {
        "intent": "research_search",
        "query_text": query,
        "filters": {}
    }

    # Recent papers
    if "recent" in query_lower:
        result["filters"]["year_min"] = 2023

    # Foundational papers
    if "foundational" in query_lower:
        result["filters"]["is_foundational"] = True

    # Specific years
    for year in ["2017", "2018", "2019", "2020",
                 "2021", "2022", "2023", "2024", "2025"]:
        if year in query_lower:
            result["filters"]["year"] = int(year)

    # Topic tags
    tags = []

    if "transformer" in query_lower:
        tags.append("transformers")

    if "attention" in query_lower:
        tags.append("attention")

    if "speculative decoding" in query_lower:
        tags.append("speculative_decoding")
        tags.append("inference")

    if tags:
        result["filters"]["tags"] = tags

    return result