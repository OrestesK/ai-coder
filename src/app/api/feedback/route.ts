import { NextResponse } from "next/server";

export async function POST(req: Request) {
    const { } = await req.json();

    const feedback = "Beautiful!";

    return NextResponse.json({ feedback });
}
