"""Runs a built BiaPy-GUI binary in self-test mode and checks it starts cleanly.

Used by the release workflows (create_windows_binary.yml, create_macos_binary.yml,
create_linux_binary.yml) to catch frozen-binary issues -- e.g. a PyInstaller data
file missing from the bundle -- before the artifact is uploaded to Google Drive.

The binary is launched with BIAPY_GUI_SELFTEST=1, which makes main.py exercise its
full import chain and main window construction headlessly (via Qt's offscreen
platform plugin) and then exit, instead of entering the event loop.
"""

import argparse
import os
import subprocess
import sys

SENTINEL = "BIAPY_GUI_SELFTEST_OK"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("binary", help="Path to the built BiaPy binary/executable")
    parser.add_argument("--timeout", type=int, default=120, help="Seconds to wait before treating the binary as hung")
    args = parser.parse_args()

    if not os.path.exists(args.binary):
        print(f"Binary not found: {args.binary}")
        return 1

    env = os.environ.copy()
    env["BIAPY_GUI_SELFTEST"] = "1"
    env.setdefault("QT_QPA_PLATFORM", "offscreen")

    print(f"Running smoke test: {args.binary} (timeout={args.timeout}s)")
    try:
        result = subprocess.run(
            [args.binary],
            env=env,
            capture_output=True,
            text=True,
            timeout=args.timeout,
        )
    except subprocess.TimeoutExpired as exc:
        print("== stdout ==")
        print(exc.stdout or "")
        print("== stderr ==")
        print(exc.stderr or "")
        print(f"FAILED: binary did not exit within {args.timeout}s (looks hung)")
        return 1

    print("== stdout ==")
    print(result.stdout)
    print("== stderr ==")
    print(result.stderr)

    if result.returncode != 0:
        print(f"FAILED: binary exited with code {result.returncode}")
        return 1

    if SENTINEL not in result.stdout:
        print(f"FAILED: expected sentinel '{SENTINEL}' not found in stdout")
        return 1

    print("Smoke test passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
