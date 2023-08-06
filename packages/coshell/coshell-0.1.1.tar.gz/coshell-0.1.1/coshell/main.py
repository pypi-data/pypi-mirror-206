import os
import platform
import re
import subprocess
import sys

import pyperclip

from coshell.internal.chat import Chat


def main():
    chat = Chat()
    language = os.path.basename(os.environ.get('SHELL'))
    chat.add_message((
        f"Platform is {platform.system()}. "
        f"Translate the following natural language instructions to {language}. "
        "Provide any non-code text as comments. "
    ))
    user_message = sys.argv[1]
    while user_message:
        response_message = chat.send_message(user_message)
        print(response_message)
        print()
        user_message = input(":")
        if user_message in ("", "q", "c", "e", "r"):
            break
        print()

    # copy code to clipboard
    content = chat.messages[-1].content
    code_block_regex = r'```(.+?)```'
    match = re.search(code_block_regex, content, flags=re.DOTALL)
    if match:
        code = match.group(1).strip()
    else:
        code = content.strip()

    if user_message == "c":
        pyperclip.copy(code)
        print("The code has been copied to your clipboard.")
    elif user_message == "r":
        print("")
        subprocess.run(code, check=True, shell=True)
    elif user_message == "e":
        # TODO: implement editing
        raise NotImplementedError


if __name__ == '__main__':
    main()
