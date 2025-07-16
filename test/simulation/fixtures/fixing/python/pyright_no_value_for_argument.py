from __future__ import annotations

import textwrap
import traceback


class MultiError(Exception):

    def __init__(self, msg, *args, errors=()):
        if errors:
            types = set(type(e).__name__ for e in errors)
            msg = f'{msg}; {len(errors)} sub errors: ({", ".join(types)})'
            for er in errors:
                self.get_error_types()
                exc_fmt = traceback.format_exception(er)
                msg += f"\n + {exc_fmt[0]}"
                er_tb = "".join(exc_fmt[1:])
                er_tb = textwrap.indent(er_tb, " | ", lambda _: True)
                msg += f"{er_tb}\n"
        super().__init__(msg, *args)
        self.__errors__ = tuple(errors)

    def get_error_types(self, error_message: str):
        print("error : " + error_message)
        return {type(e) for e in self.__errors__}
