from data_loader import get_dataframe

def answer_question(question: str):

    df = get_dataframe()

    if df is None:
        return {"answer": "Please upload a CSV first."}

    q = question.lower()

    if "total sales" in q:
        return {
            "answer": int(df["Sales"].sum())
        }

    elif "average sales" in q:
        return {
            "answer": float(df["Sales"].mean())
        }

    elif "highest sales" in q:

        row = df.loc[df["Sales"].idxmax()]

        return {
            "Region": row["Region"],
            "Product": row["Product"],
            "Sales": int(row["Sales"])
        }

    elif "show products" in q:

        return {
            "Products": df["Product"].tolist()
        }

    else:
        return {
            "answer": "Question not supported yet."
        }