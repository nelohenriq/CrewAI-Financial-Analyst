import os
from dotenv import load_dotenv
load_dotenv()

from financial_analyst_crew.crew import FinancialAnalystCrew

def run():
    inputs = {
        'cryptocurrency_name': 'Bitcoin',
    }
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()    