# cutest-picture-01 v1 — "Snowball Hug"
# A baby seal pup hugging a snowball: one huge round baby subject, enormous
# glossy eyes with star sparkles, a tiny pink starfish on its head, both
# flippers wrapped around a snowball. Deterministic: this program only copies
# entry.png to the output directory, so both runs write identical bytes.
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(
        os.path.join(here, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
