import { NextResponse } from "next/server";
import axios from "axios";
import { AxiosError } from "axios";

interface BackendError {
  detail: string; // Matches the `detail` field from the backend
}

// const backendUrl = "http://localhost:8000/feedback";
const backendUrl = "https://srv.setsero.dev/ai-coder/feedback";

export async function POST(request: Request) {
  const body = await request.json();
  if (!body.code || typeof body.code !== "string" || !body.language) {
    return NextResponse.json("Invalid input");
  }

  try {
    // Forward the request to the backend
    const response = await axios.post(backendUrl, {
      code: body.code,
      language: body.language,
    });

    if (response.status !== 200) {
      return NextResponse.json("Backend error");
    }

    return NextResponse.json(response.data);
  } catch (err) {
    // Handle errors
    const backendError = err as AxiosError<BackendError>;
    if (backendError.response?.data?.detail) {
      return NextResponse.json(backendError.response.data.detail);
    }
    return NextResponse.json("Backend unreachable");
  }
}
