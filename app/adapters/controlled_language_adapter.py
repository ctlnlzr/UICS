from openai import OpenAI
from resources.ontology import get_ontology, get_training_answer, get_training_question, get_question

client = OpenAI()


def convert_input(description):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": get_ontology()},
            {"role": "user", "content": get_training_question()},
            {"role": "assistant", "content": get_training_answer()},
            {"role": "user", "content": get_question(description)}
        ]
    )

    print(completion.choices[0].message.content)

    return completion.choices[0].message.content
