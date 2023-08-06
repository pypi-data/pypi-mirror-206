import os
import random
import sqlite3

import openai

DATABASE = os.environ.get("DATABASE", "chatbilly.db")
FINAL_PROMPT = os.environ.get(
    "FINAL_PROMPT",
    "Write with British English spellings. Don't sign off with your name.",
)


def get_messages(name):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        "SELECT message FROM messages WHERE name = ? ORDER BY RANDOM() LIMIT 50",
        (name,),
    )
    messages = c.fetchall()
    conn.close()
    return messages


def get_all_names():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT distinct name FROM messages")
    names = c.fetchall()
    conn.close()
    return [name[0] for name in names]


def combined_recent_messages_for(name):
    messages = get_messages(name)

    all_messages = []
    word_count = 0
    for msg in messages:
        words = msg[0].split()
        if word_count + len(words) <= 2000:
            all_messages.append(msg[0])
            word_count += len(words)
        else:
            remaining_words = 2000 - word_count
            all_messages.append(" ".join(words[:remaining_words]))
            break

    return "\n".join(all_messages)


def construct_prompt(messages):
    write_or_ask = (
        "Write a short message to your friends"
        if random.randrange(1, 3) == 1
        else "Ask your friends a question"
    )
    return [
        {
            "role": "system",
            "content": "You are using WhatsApp to chat with your friends.",
        },
        {
            "role": "system",
            "content": f"Here are some previous messages you've written:\n\n{messages}",
        },
        {
            "role": "system",
            "content": (
                f"{write_or_ask} in the same style and tone as those messages"
                + ", using content from those messages. Try to use the same greetings and sign-offs."
            ),
        },
        {"role": "system", "content": FINAL_PROMPT},
    ]


async def impersonate(name):
    res = combined_recent_messages_for(name)
    prompt_messages = construct_prompt(res)
    resp = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=prompt_messages,
        temperature=0.8,
    )
    return resp["choices"][0]["message"]["content"].strip()
