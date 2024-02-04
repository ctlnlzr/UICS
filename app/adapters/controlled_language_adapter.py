from openai import OpenAI
from resources.ontology import get_ontology, get_training_answer_1, get_training_question_1, get_training_answer_2, get_training_question_2, get_question

client = OpenAI()


def convert_input(description):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": get_ontology()},
            {"role": "user", "content": get_training_question_1()},
            {"role": "assistant", "content": get_training_answer_1()},
            {"role": "user", "content": get_training_question_2()},
            {"role": "assistant", "content": get_training_answer_2()},
            {"role": "user", "content": get_question(description)}
        ]
    )

    print(completion.choices[0].message.content)

    return completion.choices[0].message.content
