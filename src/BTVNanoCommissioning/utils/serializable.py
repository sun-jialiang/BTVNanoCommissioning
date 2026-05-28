from BTVNanoCommissioning.utils.correction import load_SF, load_lumi


_RUNTIME_STATE_CACHE = {}


class CorrectionCacheSerializableMixin:
    """Keep heavy correction objects out of pickled task payloads."""

    _SERIALIZATION_CACHE_FIELDS = ("SF_map", "lumiMask")

    def _cached_runtime_state(self):
        key = (getattr(self, "_year", None), getattr(self, "_campaign", None))
        if key not in _RUNTIME_STATE_CACHE:
            year, campaign = key
            _RUNTIME_STATE_CACHE[key] = {
                "SF_map": load_SF(year, campaign),
                "lumiMask": load_lumi(campaign),
            }
        return _RUNTIME_STATE_CACHE[key]

    def __getstate__(self):
        state = self.__dict__.copy()
        for field in self._SERIALIZATION_CACHE_FIELDS:
            state.pop(field, None)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        runtime_state = self._cached_runtime_state()
        self.SF_map = runtime_state["SF_map"]
        self.lumiMask = runtime_state["lumiMask"]
