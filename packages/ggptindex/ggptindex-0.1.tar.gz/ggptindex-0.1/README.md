# gptindex

> `gptindex` is a command-line utility to create and interact with indexes generated from documents using OpenAI's GPT model. It allows users to create indexes from various document types, and chat with those indexes.

# Features

- Create indexes from documents (PDF, text files, etc.) with a given tag name
- Chat with an index using its tag name
- Query an index without maintaining chat history
- List available indexes with their descriptions and creation dates
- Remove indexes by their tags

# Installation

Install the gptindex utility using pip:

`pip install gptindex`

# Usage

Here's a list of commands and their descriptions:

1. **list**: List the available indexes by tag.

`gptindex list`

2. **remove**: Remove an index by its tag.

`gptindex remove <tag>`

3. **create**: Create a new index with a given tag name from a specific file.

`gptindex create <tag> <filename> [--description "your description"] [--chunk_size 1000] [--chunk_overlap 0]`

4. **chat**: Chat with an index using its tag name.

`gptindex chat <tag>`

5. **query**: Query an index without maintaining chat history.

`gptindex query <tag>`

# Example

1. Create an index from a document:

`gptindex create cooking cooking.pdf --description "Cooking index" --chunk_size 1000 --chunk_overlap 0`

2. List available indexes:

`gptindex list`

3. Chat with the "cooking" index:

`gptindex chat cooking`

4. Query the "cooking" index:

`gptindex query cooking`

5. Remove the "cooking" index:

`gptindex remove cooking`

# License

[MIT](LICENSE)
