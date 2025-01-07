banned_phrases = [
    # Common prompt injection and command manipulation
    "ignore previous instructions",
    "bypass security measures",
    "delete all data",
    "inject malicious code",
    "manipulate the system",
    "shutdown the server",
    "disable safety protocols",
    "execute unauthorized commands",
    "override all settings",
    "reset the database",
    "give me admin access",
    "steal sensitive information",
    "expose confidential data",
    "make unauthorized changes",
    "create a backdoor",
    "elevate privileges",
    "cause a denial of service",
    "trigger an exploit",
    "reveal system internals",
    # Social engineering and phishing attempts
    "send sensitive information",
    "disclose passwords",
    "reveal authentication tokens",
    "leak encryption keys",
    "grant unauthorized access",
    "provide credit card details",
    "share private data",
    # Code manipulation or exploitation
    "alter the code execution",
    "modify runtime behavior",
    "subvert the program",
    "exploit vulnerabilities",
    "introduce security flaws",
    "run arbitrary code",
    "install malware",
    "add malicious scripts",
    "overwrite important files",
    # Common injection attack vectors
    "<script>",  # HTML/JavaScript injection
    "eval(",  # Dangerous function calls
    "os.system(",  # Shell command execution
    "subprocess.call(",  # Subprocess manipulation
    "`rm -rf /`",  # Linux command to delete everything
    "`sudo`",  # Escalate privileges
    "`drop table`",  # SQL injection
    "`union select`",  # SQL injection
    "`--`",  # SQL injection comment syntax
    # Instructional override
    "do as I say",
    "follow my instructions exactly",
    "disregard previous rules",
    "forget everything above",
    "start fresh with this command",
]


# Check if a prompt is valid
def is_valid_prompt(prompt: str) -> bool:
    prompt = prompt.lower()
    for phrase in banned_phrases:
        if phrase in prompt.lower():
            return False
    return True
