from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval import evaluate
load_dotenv()
# -----------------------------
# Initialize Model
# -----------------------------
model = init_chat_model(
    "gpt-4.1-mini",
    temperature=0.7
)

# -----------------------------
# Prompts
# -----------------------------
system_msg = SystemMessage(content="""
You are a senior Python developer.
""")

user_input = input("Ask something: ")

messages = [
    system_msg,
    HumanMessage(content=user_input)
]

# -----------------------------
# Invoke Model
# -----------------------------
response = model.invoke(messages)
print(response)
# -----------------------------
# SAFE RESPONSE EXTRACTION
# -----------------------------
actual_output = ""

if response is not None:
    if hasattr(response, "content"):
        actual_output = str(response.content).strip()

# -----------------------------
# Validate Output
# -----------------------------
if not actual_output:
    print("\n ERROR: Model returned empty response")
    exit()

print("\n================ RESPONSE ================\n")
print(actual_output)


test_case = LLMTestCase(
    input=user_input,
    actual_output=actual_output
)

# -----------------------------
# Metric
# -----------------------------
metric = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4.1-mini",
    include_reason=True
)

results = evaluate(
    test_cases=[test_case],
    metrics=[metric]
)

print(results)
print("\n================ DEEPEVAL ================\n")

for metric_data in results.test_results[0].metrics_data:
    print(f"Metric : {metric_data.name}")
    print(f"Score  : {metric_data.score}")
    print(f"Passed : {metric_data.success}")
    print(f"Reason : {metric_data.reason}")