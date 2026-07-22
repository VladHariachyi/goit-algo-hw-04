from typing import Callable
from time import perf_counter
from data import CASES


def meassure_execution_time(
   scneario: str,
   callback: Callable[[list[float]], None],
   data: list[float]
) -> None:
    start = perf_counter()
    print(f"\nCase execution started --- '{scneario}'")
    print("Processing...")

    callback(data)

    end = perf_counter() - start
    print(f"Case execution ended (time {end:.4f} sec) --- '{scneario}'\n")



if __name__ == "__main__":
    for case in CASES:
        meassure_execution_time(
            case["scenario"],
            case["sort_fn"],
            case["data"][:]
        )