"use client";

import { useState } from "react";
import Editor, { useMonaco } from "@monaco-editor/react";
import axios from "axios";
import { useEffect } from "react";

export default function CodeEditorPage() {
  const [language, setLanguage] = useState("javascript");
  const [code, setCode] = useState("// Write your code here...");
  const [feedback, setFeedback] = useState<string | null>(null);

  const languages = ["javascript", "typescript"];

  const getFeedback = async () => {
    const response = await axios.post("/api/feedback", { code_snippet: code });
    setFeedback(response.data.feedback);
  };

  const monaco = useMonaco();

  useEffect(() => {
    if (monaco) {
      monaco.editor.defineTheme("myCustomTheme", {
        base: "vs-dark",
        inherit: true,
        rules: [
          { token: "comment", foreground: "ffa500", fontStyle: "italic" },
          { token: "keyword", foreground: "00ff00" },
          { token: "identifier", foreground: "00ffff" },
        ],
        colors: {
          "editor.background": "#1e1e1e",
        },
      });
      monaco.editor.setTheme("myCustomTheme");
    }
  }, [monaco]);

  return (
    <div>
      <div className="flex flex-col items-center justify-center min-h-40">
        <h1 className="text-4xl font-bold">Welcome to Code Feedback!</h1>
        <p className="mt-4 text-lg">
          Upload your code and get AI-generated feedback.
        </p>
      </div>
      <div className="flex flex-col lg:flex-row gap-6">
        <div className="flex-1">
          {/* Language Selector Button */}
          <label htmlFor="language-select" className="text-lg font-medium">
            Select Language:
          </label>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="p-2 border rounded-md bg-white text-gray-700 ml-2 mb-4"
          >
            {languages.map((lang) => (
              <option key={lang} value={lang}>
                {lang}
              </option>
            ))}
          </select>
          <Editor
            height="40vh"
            defaultLanguage="typescript"
            language={language}
            value={code}
            onChange={(value) => setCode(value || "")}
            options={{
              lineNumbers: "on",
              scrollBeyondLastLine: false,
              wordWrap: "on",
              tabSize: 4,
              autoIndent: "full",
              minimap: {
                enabled: false,
              },
              scrollbar: {
                verticalScrollbarSize: 8,
              },
              padding: { top: 15, bottom: 15 },
            }}
          />
          <button
            className="mt-4 px-4 py-2 bg-blue-600 text-white rounded"
            onClick={getFeedback}
          >
            Get Feedback
          </button>
        </div>
        <div className="flex-1 bg-white shadow-md rounded p-4">
          <h2 className="text-xl font-semibold">Feedback</h2>
          <p className="mt-2">{feedback || "No feedback yet"}</p>
        </div>
      </div>
    </div>
  );
}
