from talon import Module, Context
from typing import List
import logging

mod = Module()
ctx = Context()

@mod.capture(rule="(all|no trap|no siphon|no flow)+")
def interpretation_sequence(m: List[str]) -> List[List[str]]:
    "Separates a interpretation sequence"
    M = list(reversed(list(m)))
    l = [["trap"], ["sattrap"], ["siphon"], ["satsiphon"], ["flow"]]
    while M:
        current = M.pop()
        if current == "no":
            current = current + M.pop()
        if current == "all":
            l.append(["trap", "siphon", "flow"])
            l.append(["sattrap", "satsiphon", "flow"])
        elif current == "notrap":
            l.append(["siphon", "flow"])
            l.append(["satsiphon", "flow"])
        elif current == "nosiphon":
            l.append(["trap", "flow"])
            l.append(["sattrap", "flow"])
        elif current == "noflow":
            l.append(["trap", "siphon"])
            l.append(["sattrap", "satsiphon"])
    logging.info("after match")
    return l

interpretations_map = {
        "trap": "\\trap",
        "siphon": "\\siphon",
        "flow": "\\flow",
        "sattrap": "\\trap^{*}",
        "satsiphon": "\\siphon^{*}",
}

def make_first(m: List[List[str]]) -> str:
    if not m:
        return ""
    result = []
    result.append(
            r"\multirow{-1}{=}{NAME} & \multirow{-1}{*}{\footnotesize $INITIAL$} & \multirow{-1}{*}{\footnotesize $TRANSITION$} & \multirow{-1}{*}{\footnotesize $ALPHABET$} & \multirow{-1}{*}{\footnotesize TOPOLOGY} & \multirow{" + str(2*len(m)) + r"}{=}{\footnotesize DESCRIPTION} & \multirow{" + str(2*len(m)) + r"}{*}{\footnotesize $PROPERTYSIZE$} & \multirow{2}{*}{\footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], m[0])) + r"$} & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
    result.append(
            r"&&&&&&&& \footnotesize \texttt{adaptive} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $(INSTANCES/GENERALIZATIONS)$ \\")
    result[-1] += r"\cline{8-14}"
    for i, e in enumerate(m[1:]):
        result.append(
                r"&&&&&&& \multirow{2}{*}{\footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], e)) + r"$} & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
        result.append(
                r"&&&&&&&& \footnotesize \texttt{adaptive} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $(INSTANCES/GENERALIZATIONS)$ \\")
        result[-1] += r"\cline{6-14}" if i == len(m)-2 else r"\cline{8-14}"
    return "\n".join(result)

def make_not_first(m: List[List[str]]) -> str:
    "Make not first property"
    if not m:
        return ""
    result = []
    result.append(
            r"&&&&& \multirow{" + str(2*len(m)) + r"}{=}{\footnotesize DESCRIPTION} & \multirow{" + str(2*len(m)) + r"}{*}{\footnotesize $PROPERTYSIZE$} & \multirow{2}{*}{\footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], m[0])) + r"$} & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
    result.append(
            r"&&&&&&&& \footnotesize \texttt{adaptive} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $(INSTANCES/GENERALIZATIONS)$ \\")
    result[-1] += r"\cline{8-14}"
    for i, e in enumerate(m[1:]):
        result.append(
                r"&&&&&&& \multirow{2}{*}{\footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], e)) + r"$} & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
        result.append(
                r"&&&&&&&& \footnotesize \texttt{adaptive} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $(INSTANCES/GENERALIZATIONS)$ \\")
        result[-1] += r"\cline{6-14}" if i == len(m)-2 else r"\cline{8-14}"
    return "\n".join(result)

def make_first_single(m: List[List[str]]) -> str:
    if not m:
        return ""
    result = []
    result.append(
            r"\multirow{-1}{=}{NAME} & \multirow{-1}{*}{\footnotesize $INITIAL$} & \multirow{-1}{*}{\footnotesize $TRANSITION$} & \multirow{-1}{*}{\footnotesize $ALPHABET$} & \multirow{-1}{*}{\footnotesize $\times$} & \multirow{" + str(len(m)) + r"}{=}{\footnotesize DESCRIPTION} & \multirow{" + str(len(m)) + r"}{*}{\footnotesize $PROPERTYSIZE$} & \footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], m[0])) + r"$ & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
    for i, e in enumerate(m[1:]):
        result.append(
                r"&&&&&&& \footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], e)) + r"$ & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
    result[-1] += r"\cline{8-14}"
    return "\n".join(result)

def make_not_first_single(m: List[List[str]]) -> str:
    "Make not first property"
    if not m:
        return ""
    result = []
    result.append(
            r"&&&&& \multirow{" + str(len(m)) + r"}{=}{\footnotesize DESCRIPTION} & \multirow{" + str(len(m)) + r"}{*}{\footnotesize $PROPERTYSIZE$} & \footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], m[0])) + r"$ & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
    for i, e in enumerate(m[1:]):
        result.append(
                r"&&&&&&& \footnotesize $" + ", ".join(map(lambda x: interpretations_map[x], e)) + r"$ & \footnotesize \texttt{learn} & \footnotesize $RESULT$ & \footnotesize $TIME$~(UNIT) & \footnotesize $(STATEMENTS/ABSTRACTION)$ & \footnotesize $USEDALPHABETSIZE$  & \footnotesize $INSTANCES$ \\")
    result[-1] += r"\cline{8-14}"
    return "\n".join(result)

@mod.action_class
class Actions:
    def make_first(m: List[List[str]]) -> str:
        "Make first property"
        return make_first(m)

    def make_first_single(m: List[List[str]]) -> str:
        "Make first_single property"
        return make_first_single(m)

    def make_bare_first() -> str:
        "Make first for only single interpretations"
        return make_first([["trap"], ["sattrap"], ["siphon"], ["satsiphon"], ["flow"]])

    def make_bare_first_single() -> str:
        "Make first_single for only single interpretations"
        return make_first_single([["trap"], ["sattrap"], ["siphon"], ["satsiphon"], ["flow"]])

    def make_bare_not_first() -> str:
        "Make not first for only single interpretations"
        return make_not_first([["trap"], ["sattrap"], ["siphon"], ["satsiphon"], ["flow"]])

    def make_bare_not_first_single() -> str:
        "Make not first_single for only single interpretations"
        return make_not_first_single([["trap"], ["sattrap"], ["siphon"], ["satsiphon"], ["flow"]])

    def make_not_first(m: List[List[str]]) -> str:
        "Make not first property"
        return make_not_first(m)

    def make_not_first_single(m: List[List[str]]) -> str:
        "Make not first_single property"
        return make_not_first_single(m)
