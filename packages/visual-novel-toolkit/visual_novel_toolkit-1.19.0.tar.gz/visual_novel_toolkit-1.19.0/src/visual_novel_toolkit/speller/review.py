from pathlib import Path
from re import escape
from re import sub

from typer import echo
from typer import Exit
from typer import getchar

from visual_novel_toolkit.speller.mistakes import load_mistakes
from visual_novel_toolkit.speller.words import FileWords


def review_mistakes() -> None:
    for mistake, source, suggestions in load_mistakes():
        echo("")
        echo(mistake)
        if suggestions:
            echo("")
            echo("   ".join(f"[{i}] {word}" for i, word in enumerate(suggestions)))
        echo("")
        echo("[i] Insert   [s] Skip   [q] Quit ", nl=False)
        ask_user = True
        while ask_user:
            match getchar():
                case "q":
                    echo("")
                    raise Exit(code=0)
                case "s":
                    echo("")
                    ask_user = False
                case "i":
                    echo("")

                    file_words = FileWords(Path("personal.json"))
                    dictionary = file_words.loads()
                    dictionary.append(mistake)
                    dictionary.sort()
                    file_words.dumps(dictionary)

                    ask_user = False
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" as index:
                    echo("")

                    pattern = r"\b" + escape(mistake) + r"\b"
                    suggestion = suggestions[int(index)]
                    fixed = sub(pattern, suggestion, source.read_text())
                    source.write_text(fixed)

                    ask_user = False
