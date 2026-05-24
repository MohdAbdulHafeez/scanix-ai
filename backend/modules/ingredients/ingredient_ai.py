async def generate_summary(
    rows,
    score,
):

    if score >= 85:

        return (
            "Overall ingredient profile looks healthy."
        )


    if score >= 65:

        return (
            "Moderately processed. Consume mindfully."
        )


    return (
        "Contains ingredients worth limiting."
    )