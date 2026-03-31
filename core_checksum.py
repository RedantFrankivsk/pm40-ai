import hashlib
import os
import sys

CORE_FILES = [
    "decision_engine.py",
    "pattern_memory.py",
]

EXPECTED_CHECKSUM = "eb224d640eac187357134c48a1e23735ac3a71984e4c4a7b90159d6c9ea84b16"


def calculate_checksum():
    h = hashlib.sha256()

    for fname in CORE_FILES:
        if not os.path.exists(fname):
            print(f"[CORE ERROR] Missing core file: {fname}")
            sys.exit(1)

        with open(fname, "rb") as f:
            h.update(f.read())

    return h.hexdigest()


def verify_core():
    checksum = calculate_checksum()

    if EXPECTED_CHECKSUM == "TO_BE_REPLACED":
        print("[CORE INIT] Checksum not initialized")
        print("Checksum:", checksum)
        sys.exit(0)

    if checksum != EXPECTED_CHECKSUM:
        print("[CORE ERROR] CORE FILES MODIFIED!")
        print("Expected:", EXPECTED_CHECKSUM)
        print("Actual:  ", checksum)
        sys.exit(1)

    print("[CORE OK] Core integrity verified")
