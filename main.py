# cutest-picture-01 v1 — "Snowball Hug"
# A baby seal pup hugging a snowball: one huge round baby subject, enormous
# glossy eyes with star sparkles, a tiny pink starfish on its head, both
# flippers wrapped around a snowball. Deterministic: this program only copies
# entry.png to the output directory, so both runs write identical bytes.
# Round 3: the source path falls back to entry.png in the current working
# directory when the script-relative path is missing.
import os
import shutil


def find_source():
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, "entry.png"),
        os.path.join(os.getcwd(), "entry.png"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    raise FileNotFoundError(
        "entry.png not found in any of: " + ", ".join(candidates)
    )


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        find_source(),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
