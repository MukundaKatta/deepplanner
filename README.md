# deepplanner

**Agent harness with hierarchical planning tools, filesystem backend, and autonomous subagent spawning**

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-proprietary-red)

## Install
```bash
pip install -e ".[dev]"
```

## Quick Start
```python
from src.core import Deepplanner
 instance = Deepplanner()
r = instance.decompose(input="test")
```

## CLI
```bash
python -m src status
python -m src run --input "data"
```

## API
| Method | Description |
|--------|-------------|
| `decompose()` | Decompose |
| `execute_plan()` | Execute plan |
| `spawn_subagent()` | Spawn subagent |
| `checkpoint()` | Checkpoint |
| `rollback()` | Rollback |
| `get_trace()` | Get trace |
| `get_stats()` | Get stats |
| `reset()` | Reset |

## Test
```bash
pytest tests/ -v
```

## License
(c) 2026 Officethree Technologies. All Rights Reserved.
