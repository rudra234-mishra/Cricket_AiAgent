from graph_state import Total
from langgraph.graph import START,END,StateGraph
from model import llm_model_conn,str_model_conn
from logging_config import logger

def summary(state:Total):
    name=state["Name"]
    prompt=f'Based On The Player {name} write A Summary About 100 words'

    model=llm_model_conn()
    summary=model.invoke(prompt).content
    return {"Summary":summary}

def odi(state:Total):
    name=state["Name"]
    prompt=f'Give Me The ODI Statictis For The Player {name}'
    model=str_model_conn()
    matches=model.invoke(prompt).matches
    runs=model.invoke(prompt).runs

    hundreds=model.invoke(prompt).hundreds
    fifties=model.invoke(prompt).fifties
    fours=model.invoke(prompt).fours
    sixes=model.invoke(prompt).sixes
    highest_score=model.invoke(prompt).highest_score

    return {
    "ODI": {
        "matches":matches,
        "runs": runs,
        "hundreads": hundreds,
        "fifties": fifties,
        "fours": fours,
        "sixes": sixes,
        "highest_score":highest_score
    }
}

def t20(state:Total):
    name=state["Name"]
    prompt=f'Give Me The T20 Statictis For The Player {name}'
    model=str_model_conn()
    matches=model.invoke(prompt).matches
    runs=model.invoke(prompt).runs

    hundreds=model.invoke(prompt).hundreds
    fifties=model.invoke(prompt).fifties
    fours=model.invoke(prompt).fours
    sixes=model.invoke(prompt).sixes
    highest_score=model.invoke(prompt).highest_score

    return {
    "T20": {
        "matches":matches,
        "runs": runs,
        "hundreads": hundreds,
        "fifties": fifties,
        "fours": fours,
        "sixes": sixes,
        "highest_score":highest_score
    }
}

def test(state:Total):
    name=state["Name"]
    prompt=f'Give Me The Test Statictis For The Player {name}'
    model=str_model_conn()
    matches=model.invoke(prompt).matches
    runs=model.invoke(prompt).runs

    hundreds=model.invoke(prompt).hundreds
    fifties=model.invoke(prompt).fifties
    fours=model.invoke(prompt).fours
    sixes=model.invoke(prompt).sixes
    highest_score=model.invoke(prompt).highest_score

    return {
    "TEST": {
        "matches":matches,
        "runs": runs,
        "hundreads": hundreds,
        "fifties": fifties,
        "fours": fours,
        "sixes": sixes,
        "highest_score":highest_score
    }
}

def ipl(state:Total):
    name=state["Name"]
    prompt=f'Give Me The IPL Statictis For The Player {name}'
    model=str_model_conn()
    matches=model.invoke(prompt).matches
    runs=model.invoke(prompt).runs

    hundreds=model.invoke(prompt).hundreds
    fifties=model.invoke(prompt).fifties
    fours=model.invoke(prompt).fours
    sixes=model.invoke(prompt).sixes
    highest_score=model.invoke(prompt).highest_score

    return {
    "IPL": {
        "matches":matches,
        "runs": runs,
        "hundreads": hundreds,
        "fifties": fifties,
        "fours": fours,
        "sixes": sixes,
        "highest_score":highest_score
    }
}


def build_graph():

    logger.info("Graph Building Start :")
    graph=StateGraph(Total)
    graph.add_node("summary",summary)
    graph.add_node("odi",odi)
    graph.add_node("t20",t20)
    graph.add_node("test",test)
    graph.add_node("ipl",ipl)

    logger.info("Edge Building Start :")
    graph.add_edge(START,"summary")
    graph.add_edge(START,"odi")
    graph.add_edge(START,"t20")
    graph.add_edge(START,"test")
    graph.add_edge(START,"ipl")
    graph.add_edge("summary",END)
    graph.add_edge("odi",END)
    graph.add_edge("t20",END)
    graph.add_edge("test",END)
    graph.add_edge("ipl",END)


    return graph.compile()