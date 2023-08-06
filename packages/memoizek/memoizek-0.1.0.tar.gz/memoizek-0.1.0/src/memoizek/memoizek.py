from typing import Any


def list_find(list: list, to_find: Any):
    try:
        index = list.index(to_find)
        return index
    except ValueError:
        return -1


class MemoizeK:
    """A custom-sized cache for functions in Python."""
    def __init__(self, func, k):
        self.function = func
        self.K = k
        self.size = 0
        self.cached_results = []
        self.cached_args = []

    def _move_cache_item_to_front(self, index: int):
        self.cached_args.insert(0, self.cached_args.pop(index))
        self.cached_results.insert(0, self.cached_results.pop(index))

    def _push_to_cache(self, args: Any, results: Any):
        self.cached_args.insert(0, args)
        self.cached_results.insert(0, results)
        self.size += 1

    def _pop_from_cache(self):
        self.cached_args.pop(len(self.cached_args) - 1)
        self.cached_results.pop(len(self.cached_results) - 1)
        self.size -= 1

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        cache_ptr = list_find(list=self.cached_args, to_find=args)
        if cache_ptr != -1:
            if cache_ptr > 0:
                self._move_cache_item_to_front(index=cache_ptr)

            return self.cached_results[0]

        if self.size == self.K:
            self._pop_from_cache()

        self._push_to_cache(args=args, results=self.function(*args))
        return self.cached_results[0]
