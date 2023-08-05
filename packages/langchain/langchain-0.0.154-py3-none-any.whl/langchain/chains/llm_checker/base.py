"""Chain for question-answering with self-verification."""
from __future__ import annotations

import warnings
from typing import Any, Dict, List, Optional

from pydantic import Extra, root_validator

from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.chains.llm_checker.prompt import (
    CHECK_ASSERTIONS_PROMPT,
    CREATE_DRAFT_ANSWER_PROMPT,
    LIST_ASSERTIONS_PROMPT,
    REVISED_ANSWER_PROMPT,
)
from langchain.chains.sequential import SequentialChain
from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate


def _load_question_to_checked_assertions_chain(
    llm: BaseLLM,
    create_draft_answer_prompt: PromptTemplate,
    list_assertions_prompt: PromptTemplate,
    check_assertions_prompt: PromptTemplate,
    revised_answer_prompt: PromptTemplate,
) -> SequentialChain:
    create_draft_answer_chain = LLMChain(
        llm=llm,
        prompt=create_draft_answer_prompt,
        output_key="statement",
    )
    list_assertions_chain = LLMChain(
        llm=llm,
        prompt=list_assertions_prompt,
        output_key="assertions",
    )
    check_assertions_chain = LLMChain(
        llm=llm,
        prompt=check_assertions_prompt,
        output_key="checked_assertions",
    )
    revised_answer_chain = LLMChain(
        llm=llm,
        prompt=revised_answer_prompt,
        output_key="revised_statement",
    )
    chains = [
        create_draft_answer_chain,
        list_assertions_chain,
        check_assertions_chain,
        revised_answer_chain,
    ]
    question_to_checked_assertions_chain = SequentialChain(
        chains=chains,
        input_variables=["question"],
        output_variables=["revised_statement"],
        verbose=True,
    )
    return question_to_checked_assertions_chain


class LLMCheckerChain(Chain):
    """Chain for question-answering with self-verification.

    Example:
        .. code-block:: python

            from langchain import OpenAI, LLMCheckerChain
            llm = OpenAI(temperature=0.7)
            checker_chain = LLMCheckerChain.from_llm(llm)
    """

    question_to_checked_assertions_chain: SequentialChain

    llm: Optional[BaseLLM] = None
    """[Deprecated] LLM wrapper to use."""
    create_draft_answer_prompt: PromptTemplate = CREATE_DRAFT_ANSWER_PROMPT
    """[Deprecated]"""
    list_assertions_prompt: PromptTemplate = LIST_ASSERTIONS_PROMPT
    """[Deprecated]"""
    check_assertions_prompt: PromptTemplate = CHECK_ASSERTIONS_PROMPT
    """[Deprecated]"""
    revised_answer_prompt: PromptTemplate = REVISED_ANSWER_PROMPT
    """[Deprecated] Prompt to use when questioning the documents."""
    input_key: str = "query"  #: :meta private:
    output_key: str = "result"  #: :meta private:

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid
        arbitrary_types_allowed = True

    @root_validator(pre=True)
    def raise_deprecation(cls, values: Dict) -> Dict:
        if "llm" in values:
            warnings.warn(
                "Directly instantiating an LLMCheckerChain with an llm is deprecated. "
                "Please instantiate with question_to_checked_assertions_chain "
                "or using the from_llm class method."
            )
            if (
                "question_to_checked_assertions_chain" not in values
                and values["llm"] is not None
            ):
                question_to_checked_assertions_chain = (
                    _load_question_to_checked_assertions_chain(
                        values["llm"],
                        values.get(
                            "create_draft_answer_prompt", CREATE_DRAFT_ANSWER_PROMPT
                        ),
                        values.get("list_assertions_prompt", LIST_ASSERTIONS_PROMPT),
                        values.get("check_assertions_prompt", CHECK_ASSERTIONS_PROMPT),
                        values.get("revised_answer_prompt", REVISED_ANSWER_PROMPT),
                    )
                )
                values[
                    "question_to_checked_assertions_chain"
                ] = question_to_checked_assertions_chain
        return values

    @property
    def input_keys(self) -> List[str]:
        """Return the singular input key.

        :meta private:
        """
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        """Return the singular output key.

        :meta private:
        """
        return [self.output_key]

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        question = inputs[self.input_key]

        output = self.question_to_checked_assertions_chain(
            {"question": question}, callbacks=_run_manager.get_child()
        )
        return {self.output_key: output["revised_statement"]}

    @property
    def _chain_type(self) -> str:
        return "llm_checker_chain"

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        create_draft_answer_prompt: PromptTemplate = CREATE_DRAFT_ANSWER_PROMPT,
        list_assertions_prompt: PromptTemplate = LIST_ASSERTIONS_PROMPT,
        check_assertions_prompt: PromptTemplate = CHECK_ASSERTIONS_PROMPT,
        revised_answer_prompt: PromptTemplate = REVISED_ANSWER_PROMPT,
        **kwargs: Any,
    ) -> LLMCheckerChain:
        question_to_checked_assertions_chain = (
            _load_question_to_checked_assertions_chain(
                llm,
                create_draft_answer_prompt,
                list_assertions_prompt,
                check_assertions_prompt,
                revised_answer_prompt,
            )
        )
        return cls(
            question_to_checked_assertions_chain=question_to_checked_assertions_chain,
            **kwargs,
        )
