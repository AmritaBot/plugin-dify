from amrita.plugins.chat.API import (
    FunctionDefinitionSchema,
    FunctionParametersSchema,
    FunctionPropertySchema,
)

RAG_TOOL_DATA = FunctionDefinitionSchema(
    name="dify_search",
    description="Use this tool to search for information using Dify when users ask questions that require specific knowledge or current information. "
    + "\nAlways use this tool when you need to find specific facts, data, or information that you don't have direct access to. "
    + "\nIf the search yields no results, inform the user that no relevant information was found.",
    parameters=FunctionParametersSchema(
        type="object",
        properties={
            "query": FunctionPropertySchema(
                type="string",
                description="The search query containing specific information needs, using natural language (question sentence) or keywords.",
            )
        },
        required=["query"],
    ),
)
