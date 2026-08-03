import os
from dotenv import load_dotenv
load_dotenv()
from logging_config import logger
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel,Field
from typing import TypedDict,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
import psycopg2


def llm_model_conn():

    try:
        logger.info("Model Connection Start :")
        model=AzureChatOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("api_version"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            model=os.getenv("AZURE_OPENAI_MODEL"),
            temperature=0.3
        )
        logger.info("Model Connection Successfull :")
        return model

    except Exception as e:
        logger.info("Model Connection Failed :%s",e)


    # try:
    #     logger.info("Model Connection Start :")
    #     model = ChatGoogleGenerativeAI(
    #         model="gemini-2.5-flash",
    #         google_api_key=os.getenv("google_api_key"),
    #         temperature=0
    #     )
    #     logger.info("Model Connection Successfull :")
    #     return model

    # except Exception as e:
    #     logger.info("Model Connection Failed :%s",e)



class str_model(BaseModel):
    matches:Annotated[int,Field(description="total matches",ge=1)]
    runs:Annotated[int,Field(description='Total Runs',ge=1)]
    hundreds:Annotated[int,Field(description='Total hundreds',ge=1)]
    fifties:Annotated[int,Field(description='Total fifties',ge=1)]
    fours:Annotated[int,Field(description='Total fours',ge=1)]
    sixes:Annotated[int,Field(description='Total sixes',ge=1)]
    highest_score:Annotated[int,Field(description="Highest Score ",ge=1)]

def str_model_conn():
    try:
        model=llm_model_conn()
        logger.info("Structure Model Connection Start :")
        Str_model=model.with_structured_output(str_model)

        logger.info("Structure Model Connection Successfull :")
        return Str_model

    except Exception as e:
        logger.info("Structure Model Connection Failed :%s",e)


def database_conn():

    try:
        logger.info("Database Connection Start :")
        conn=psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        logger.info("Database Connection Successfull :")
        return conn

    except Exception as e:
        logger.info("Database Connection Failed :%s",e)