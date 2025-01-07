from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.prompter import build_state_graph
from src.utils import is_valid_prompt
import json
import logging


class FeedbackRequest(BaseModel):
    code: str
    language: str


app = FastAPI()
prompter = build_state_graph()


@app.post("/ai-coder/feedback")
def read_root(request: FeedbackRequest):
    # Prepare input
    input = {
        "code": request.code,
        "language": request.language,
    }
    string_input = json.dumps(input)

    # Validate input
    if not is_valid_prompt(string_input):
        logging.warning(f"Malicious input detected: {string_input}")
        raise HTTPException(
            status_code=400,
            detail="Input is flagged as malicious. Please revise your content.",
        )

    # Generate feedback
    try:
        res = prompter.invoke(input)
        logging.info(f"Feedback generated successfully for input: {string_input}")
        return res["answer"]
    # Handle errors
    except Exception as e:
        logging.error(f"Error generating feedback: {str(e)}")

        # Handle Azure OpenAI content filtering
        if "content management policy" in str(e):
            raise HTTPException(
                status_code=400,
                detail="Input is flagged as malicious. Please revise your content",
            )

        # Handle other errors
        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        )
