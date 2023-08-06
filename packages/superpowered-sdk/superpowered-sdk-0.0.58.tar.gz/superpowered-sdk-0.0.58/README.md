# Superpowered AI Python SDK

This Python SDK provides an interface to interact with Superpowered AI, a knowledge base as a service for LLM applications. The SDK allows you to create, update, and delete knowledge bases, as well as directly query a knowledge base. You can also create and delete documents in a knowledge base.

### Installation

To install the Superpowered AI Python SDK you can use pip

```bash
pip install superpowered-sdk
```

### Setup

Set the following environmental variables in a terminal
```bash
export SUPERPOWERED_API_KEY_ID="INSERT_API_KEY_ID_HERE"
export SUPERPOWERED_API_KEY_SECRET="INSERT_API_KEY_SECRET_HERE"
```

Import all from superpowered
```python
from superpowered import *
```

### Creating a Knowledge Base

To create a new knowledge base, use the `create_knowledge_base()` function:

```python
create_knowledge_base(title="My Knowledge Base", supp_id="123", description="A sample knowledge base")
```

### Listing Knowledge Bases

To list all knowledge bases in your account, use the `list_knowledge_bases()` function:

```python
list_knowledge_bases(verbose=True)
```

### Adding a Document to a Knowledge Base

To add a document to a knowledge base, use the `add_document_to_kb()` function. Note that for this function your document needs to already be converted to a string. If your content is in a file type that we support (pdf, txt, docx, or md), you can directly upload the file using `add_file_to_kb()` instead of converting it to a string first.

```python
add_document_to_kb(kb_title="My Knowledge Base", content="This is a sample document.", title="Sample Document")
```

Also note that you can't have duplicate documents (content or title) in the same knowledge base, as doing so would lead to suboptimal querying performance.

### Adding a File to a Knowledge Base

To add a file (pdf, txt, docx, or md) to a knowledge base, use the `add_file_to_kb()` function:

```python
add_file_to_kb(kb_title="My Knowledge Base", file_path="path/to/your/file.pdf")
```

### Adding All Files in a Directory to a Knowledge Base

To add all supported files in a directory to a knowledge base, use the `add_directory_to_kb()` function:

```python
add_directory_to_kb(kb_title="My Knowledge Base", directory_path="path/to/your/directory")
```

### Adding the Contents of a Web Page to a Knowledge Base

To scrape the text from a web page and upload it to a Knowledge Base, you can use the `add_url_to_kb()` function:

```python
add_url_to_kb(kb_title="My Knowledge Base", url="https://example.com")
```

Note that this function will not scrape any text that requires Javascript rendering, and it also won't work for any web page that requires a login.

### Querying a Knowledge Base

To query a knowledge base, use the `query()` function. The function accepts several parameters to customize the query:

- `query`: The query string you want to search for in the knowledge bases.
- `kb_titles`: A list of knowledge base titles to search in. This allows you to search in specific knowledge bases by providing their titles.
- `kb_ids`: A list of knowledge base IDs to search in. This allows you to search in specific knowledge bases by providing their IDs.
- `retriever_top_k`: The number of top documents to retrieve in the first stage of the retrieval pipeline. This parameter controls how many documents are initially retrieved before reranking.
- `reranker_top_k`: The number of documents to return from the reranking step. This must be less than or equal to the retriever_top_k.
- `extract_and_summarize`: A boolean value indicating whether to extract and summarize the results. If set to True, the API will return LLM-summarized results from the top documents.

Here's an example of querying a knowledge base with all the available parameters:

```python
results = query(
    query="What is the capital of France?",
    kb_titles=["My Knowledge Base"],
    retriever_top_k=50,
    reranker_top_k=10,
    extract_and_summarize=True
)

# print the summary - only works if `extract_and_summarize` is set to `True`
print (results["summary"])

# print the top results
print ([result["content"] for result in results["ranked_results"]])
```

You can also query multiple knowledge bases by providing a list of knowledge base titles or IDs:

```python
results = query(
    query="What is the capital of France?",
    kb_titles=["My Knowledge Base", "Another Knowledge Base"],
    retriever_top_k=50,
    reranker_top_k=10,
    extract_and_summarize=True
)
```

### KnowledgeBase and KnowledgeBaseDocument classes

In addition to the convenience functions, you can also use the `KnowledgeBase` and `KnowledgeBaseDocument` classes for more advanced usage. For example, you can create a `KnowledgeBase` object and then add documents to it:

```python
kb = KnowledgeBase(title="My Knowledge Base")
kb.create()
kb.add_document(content="This is a sample document.", title="Sample Document")
```

You can also delete a knowledge base or a document using the `delete()` method:

```python
kb.delete()
document.delete()
```

For more information on the available methods and properties, please refer to the SDK code.
