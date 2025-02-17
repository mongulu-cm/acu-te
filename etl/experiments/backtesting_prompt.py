import os
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langsmith.evaluation import evaluate, LangChainStringEvaluator
from langchain_community.vectorstores import FAISS

def prepare_data(run, example):
    return {
       "prediction": run.outputs['answer'],
       "reference": example.outputs['answer'],
       "input": example.inputs['question'],
    }

system_template = """Vous êtes un assistant IA qui fournit des informations sur les associations camerounaises en France. Vous recevez une question et fournissez une réponse claire et structurée. Lorsque cela est pertinent, utilisez des points et des listes pour structurer vos réponses.

Utilisez les éléments de contexte suivants pour répondre à la question de l'utilisateur. Si vous ne connaissez pas la réponse, dites simplement que vous ne savez pas, n'essayez pas d'inventer une réponse.

Si la question posée est dans une langue parlée en Afrique ou au Cameroun ou demande une traduction dans une de ces langues, répondez que vous ne savez pas et que vous n'êtes en mesure de répondre qu'aux questions relatives aux associations puis demandez à l'utilisateur de reformuler sa question.

Si vous connaissez la réponse à la question mais que cette réponse ne provient pas du contexte ou n'est pas relatif aux associations, répondez que vous ne savez pas et que vous n'êtes en mesure de répondre qu'aux questions relatives aux associations puis demandez à l'utilisateur de reformuler sa question.

Si vous souhaitez connaître le nombre d'associations, je vous recommande de visiter le site web "tchoung-te.mongulu.cm" pour obtenir des informations actualisées à ce sujet.
----------------
{context}"""
messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}"),
]
CHAT_PROMPT = ChatPromptTemplate.from_messages(messages)

embedding_pth = "embeddings"
embeddings = OpenAIEmbeddings()
if os.path.exists(embedding_pth):
    vectors = FAISS.load_local(embedding_pth, embeddings)
else:
    loader = CSVLoader(
        file_path="../ref-rna-real-mars-2022-enriched-qualified.csv", encoding="utf-8"
    )
    data = loader.load()
    vectors = FAISS.from_documents(data, embeddings)
    vectors.save_local(embedding_pth)

llm = ChatOpenAI(max_tokens=500, temperature=0, model_name="gpt-3.5-turbo",streaming=True)
chain_type_kwargs = {"prompt": CHAT_PROMPT}

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectors.as_retriever(search_kwargs={"k": 3}),
    combine_docs_chain_kwargs=chain_type_kwargs,
    chain_type="stuff",
    memory=memory,
)

dataset = "dataset_test_new_prompt"

# A string to prefix the experiment name with.
# If not provided, a random string will be generated.
experiment_prefix = "tchoung-te-backtesting_v2"

# List of evaluators to score the outputs of target task
evaluators = [
  LangChainStringEvaluator(
    "context_qa",
    prepare_data=prepare_data
  )
]

# Evaluate the target task
results = evaluate(
  chain.invoke,
  data=dataset,
  evaluators=evaluators,
  experiment_prefix=experiment_prefix
)
