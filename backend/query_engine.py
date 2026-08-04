from data_loader import get_dataframe
from llm import ask_llm

def answer_question(question: str):

    df = get_dataframe()

    if df is None:
        return {"answer": "Please upload a CSV first."}

    prompt = f"""
You are a CSV analysis assistant.

Available columns:
{list(df.columns)}

User Question:
{question}

Reply with ONLY ONE keyword from this list:

TOTAL_SALES
AVERAGE_SALES
HIGHEST_SALES
SHOW_PRODUCTS
TOTAL_ROWS

Do not explain anything.
"""

    intent = ask_llm(prompt).strip().upper()

    if intent == "TOTAL_SALES":
        return {
            "question": question,
            "answer": int(df["Sales"].sum())
        }

    elif intent == "AVERAGE_SALES":
        return {
            "question": question,
            "answer": float(df["Sales"].mean())
        }

    elif intent == "HIGHEST_SALES":

        row = df.loc[df["Sales"].idxmax()]

        return {
            "Region": row["Region"],
            "Product": row["Product"],
            "Sales": int(row["Sales"])
        }

    elif intent == "SHOW_PRODUCTS":

        return {
            "Products": df["Product"].tolist()
        }

    elif intent == "TOTAL_ROWS":

        return {
            "Rows": len(df)
        }

    else:
        return {
            "answer": "Sorry, I couldn't understand the question."
        }