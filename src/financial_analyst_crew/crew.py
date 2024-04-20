from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
# ollama_mixtral = Ollama(model="mixtral", base_url="https://11434-01ht0mvyjesyha3xfdnzha3w8p.cloudspaces.litng.ai")

@CrewBase
class FinancialAnalystCrew():
	"""FinancialAnalystCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self) -> None:
		self.groq_llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")
		# self.groq_llm = ollama_mixtral

	@agent
	def cryptocurrency_researcher(self) -> Agent:
		return Agent(
			config = self.agents_config['cryptocurrency_researcher'],
			llm = self.groq_llm
		)

	@agent
	def cryptocurrency_analyst(self) -> Agent:
		return Agent(
			config = self.agents_config['cryptocurrency_analyst'],
			llm = self.groq_llm
		)

	@task
	def research_cryptocurrency_task(self) -> Task:
		return Task(
			config = self.tasks_config['research_cryptocurrency_task'],
			agent = self.cryptocurrency_researcher()
		)

	@task
	def analyze_cryptocurrency_task(self) -> Task:
		return Task(
			config = self.tasks_config['analyze_cryptocurrency_task'],
			agent = self.cryptocurrency_analyst()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FinancialAnalystCrew crew"""
		return Crew(
			agents =  self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = 2
		)