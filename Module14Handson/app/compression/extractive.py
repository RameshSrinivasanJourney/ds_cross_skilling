import re


STOP_WORDS = {
    "the",
    "a",
    "an",
    "is",
    "are",
    "was",
    "were",
    "to",
    "of",
    "in",
    "on",
    "for",
    "and",
    "or",
    "with",
    "that",
    "this",
}


def sentence_score(
    sentence: str,
    question: str,
) -> float:
    """Simple keyword-overlap score."""

    sentence_words = set(
        re.findall(
            r"\b[a-zA-Z0-9]+\b",
            sentence.lower(),
        )
    ) - STOP_WORDS

    question_words = set(
        re.findall(
            r"\b[a-zA-Z0-9]+\b",
            question.lower(),
        )
    ) - STOP_WORDS

    if not sentence_words:
        return 0.0

    overlap = (
        sentence_words
        & question_words
    )

    return len(overlap) / len(
        sentence_words
    )


def compress_extractive(
    text: str,
    question: str,
    keep_ratio: float = 0.5,
) -> str:
    """
    Keep the most question-relevant sentences.
    """

    sentences = [
        s.strip()
        for s in re.split(
            r"(?<=[.!?])\s+",
            text.strip(),
        )
        if s.strip()
    ]

    if not sentences:
        return ""

    keep_count = max(
        1,
        int(
            len(sentences)
            * keep_ratio
        ),
    )

    scored = [
        (
            sentence_score(
                sentence,
                question,
            ),
            index,
            sentence,
        )
        for index, sentence in enumerate(
            sentences
        )
    ]

    selected = sorted(
        scored,
        key=lambda item: (
            item[0],
            -item[1],
        ),
        reverse=True,
    )[:keep_count]

    selected_indices = sorted(
        item[1]
        for item in selected
    )

    return " ".join(
        sentences[index]
        for index in selected_indices
    )