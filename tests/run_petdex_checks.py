"""Run the targeted collection checks without loading a real Chatbook profile."""

import json
import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


def main() -> int:
    with TemporaryDirectory(prefix="petdex-skill-tests-") as directory:
        root = Path(directory).resolve()
        data = root / "data"
        data.mkdir(mode=0o700)
        config = root / "config.toml"
        config.write_text("[paths]\ndata_dir = " + json.dumps(str(data)) + "\n")
        config.chmod(0o600)
        previous = os.environ.get("TLDW_CONFIG_PATH")
        os.environ["TLDW_CONFIG_PATH"] = str(config)
        try:
            suite = unittest.defaultTestLoader.discover(
                str(Path(__file__).parent), pattern="test_petdex*.py"
            )
            result = unittest.TextTestRunner(verbosity=2).run(suite)
            return 0 if result.wasSuccessful() else 1
        finally:
            if previous is None:
                os.environ.pop("TLDW_CONFIG_PATH", None)
            else:
                os.environ["TLDW_CONFIG_PATH"] = previous


if __name__ == "__main__":
    raise SystemExit(main())
